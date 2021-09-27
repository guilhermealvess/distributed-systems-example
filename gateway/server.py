import functools, operator
import grpc
from concurrent import futures
import json
from pymongo import collation

import redis

from database.database import Database
import pb.gateway_pb2, pb.gateway_pb2_grpc
import pb.service_sandwiche_pb2, pb.service_sandwiche_pb2_grpc
import pb.service_drink_pb2, pb.service_drink_pb2_grpc
import pb.service_dish_made_pb2, pb.service_dish_made_pb2_grpc
import pb.service_dessert_pb2, pb.service_dessert_pb2_grpc


class Cache:
    def __init__(self) -> None:
        self.cache = redis.Redis(host='0.0.0.0', port=6379)
    def setValue(self, key, data):
        self.cache.set(key, json.dumps(data))
    def getValue(self, key):
        return self.cache.get(key)
    def delete(self, key):
        self.cache.delete(key)


class GatewayService:
    def __init__(self) -> None:
        self.service_sandwiche = 'localhost:5001'
        self.service_drink = 'localhost:5002'
        self.service_dish_made = 'localhost:5003'
        self.service_dessert = 'localhost:5004'
        
    def getMenu(self, tableNumber):
        with grpc.insecure_channel(self.service_sandwiche) as channel:
            stub = pb.service_sandwiche_pb2_grpc.SandwicheServiceStub(channel)
            findSandwichesRequest = pb.service_sandwiche_pb2.FindSandwichesRequest(tableNumber=tableNumber)
            sand = stub.FindSandwiches(findSandwichesRequest)
            sandwiches_response = list(map(lambda s: pb.gateway_pb2.Sandwiche(
                id=s.id,
                name=s.name,
                price=s.price,
                preparationTime=s.preparationTime,
                ingredients=s.ingredients
            ), list(sand.sandwiches)))

        with grpc.insecure_channel(self.service_drink) as channel:
            stub = pb.service_drink_pb2_grpc.DrinkServiceStub(channel)
            findDrinksRequest = pb.service_drink_pb2.FindDrinksRequest(tableNumber=tableNumber)
            drink = stub.FindDrinks(findDrinksRequest)
            drinks_response = list(map(lambda d: pb.gateway_pb2.Drink(
                id=d.id,
                name=d.name,
                price=d.price,
            ), list(drink.drinks)))

        with grpc.insecure_channel(self.service_dish_made) as channel:
            stub = pb.service_dish_made_pb2_grpc.DishMadeServiceStub(channel)
            findDishMadesRequest = pb.service_dish_made_pb2.FindDishMadeRequest(tableNumber=tableNumber)
            dishMades = stub.FindDishMades(findDishMadesRequest)
            dishMades_response = list(map(lambda d: pb.gateway_pb2.DishMade(
                id=d.id,
                name=d.name,
                price=d.price,
                ingredients=d.ingredients
            ), list(dishMades.dishMades)))

        with grpc.insecure_channel(self.service_dessert) as channel:
            stub = pb.service_dessert_pb2_grpc.DessertServiceStub(channel)
            findDessertRequest = pb.service_dessert_pb2.FindDessertRequest(tableNumber=tableNumber)
            desserts = stub.FindDesserts(findDessertRequest)
            desserts_response = list(map(lambda d: pb.gateway_pb2.Dessert(
                id=d.id,
                name=d.name,
                price=d.price
            ), list(desserts.desserts)))

        return pb.gateway_pb2.MenuResponse(sandwiches=sandwiches_response, dishMades=dishMades_response, drinks=drinks_response, desserts=desserts_response)

    def createOrder(self, tableNumber, ids):
        foods = list()
        preparationTimeTotal = 0

        with grpc.insecure_channel(self.service_sandwiche) as channel:
            stub = pb.service_sandwiche_pb2_grpc.SandwicheServiceStub(channel)
            orderRequest = pb.service_sandwiche_pb2.OrderRequest(id=ids)
            response = stub.ExecuteOrder(orderRequest)
            preparationTimeTotal += response.preparationTime
            foods += response.foods

        with grpc.insecure_channel(self.service_drink) as channel:
            stub = pb.service_drink_pb2_grpc.DrinkServiceStub(channel)
            orderRequest = pb.service_drink_pb2.OrderRequest(id=ids)
            response = stub.ExecuteOrder(orderRequest)
            preparationTimeTotal += response.preparationTime
            foods += response.foods

        with grpc.insecure_channel(self.service_dish_made) as channel:
            stub = pb.service_dish_made_pb2_grpc.DishMadeServiceStub(channel)
            orderRequest = pb.service_dish_made_pb2.OrderRequest(id=ids)
            response = stub.ExecuteOrder(orderRequest)
            preparationTimeTotal += response.preparationTime
            foods += response.foods

        with grpc.insecure_channel(self.service_dessert) as channel:
            stub = pb.service_dessert_pb2_grpc.DessertServiceStub(channel)
            orderRequest = pb.service_dessert_pb2.OrderRequest(id=ids)
            response = stub.ExecuteOrder(orderRequest)
            preparationTimeTotal += response.preparationTime
            foods += response.foods

        key = str(tableNumber)
        Cache().setValue(key, list(ids))

        return pb.gateway_pb2.OrderResponse(foods=foods, preparationTime=preparationTimeTotal)

    def closeAccount(self, tableNumber):
        _collections = ['sandwiches', 'drinks', 'dishMade', 'dessert']
        data = Cache().getValue(str(tableNumber))
        prices = list()
        if data:
            for id in data:
                for col in _collections:
                    doc = Database().findById(col, id)
                    if doc:
                        prices.append(doc.get('price'))
                        break
            total = functools.reduce(operator.add, prices)
        else:
            total = 0
        Cache().delete(str(tableNumber))
        return pb.gateway_pb2.CloseAccountResponse(total=total)

class Server(pb.gateway_pb2_grpc.ServerServicer):
    def GetMenu(self, request, context):
        return GatewayService().getMenu(request.tableNumber)

    def CreateOrder(self, request, context):
        return GatewayService().createOrder(request.tableNumber, request.id)

    def CloseAccount(self, request, context):
        return GatewayService().closeAccount(request.tableNumber)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb.gateway_pb2_grpc.add_ServerServicer_to_server(Server(), server)
    port = 5000
    server.add_insecure_port('[::]:{}'.format(port))
    print('\nRUNNING IN PORT {} ...\n'.format(port))
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
