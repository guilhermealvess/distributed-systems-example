import grpc
from concurrent import futures
import json

import redis

import pb.gateway_pb2, pb.gateway_pb2_grpc
import pb.service_sandwiche_pb2, pb.service_sandwiche_pb2_grpc
import pb.service_drink_pb2, pb.service_drink_pb2_grpc
import pb.service_dish_made_pb2, pb.service_dish_made_pb2_grpc
import pb.service_dessert_pb2, pb.service_dessert_pb2_grpc


class Cache:
    def __init__(self) -> None:
        self.cache = redis.Redis(host='0.0.0.0', port=6379)

    def setValue(self, key, data):
        self.cache.set(json.dumps(data))

    def getValue(self, key):
        return json.loads(self.getValue(key))


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

        Cache.setValue(str(tableNumber), json.loads(ids))

        return pb.gateway_pb2.OrderResponse(foods=foods, preparationTime=preparationTimeTotal)
            

class Server(pb.gateway_pb2_grpc.ServerServicer):
    def GetMenu(self, request, context):
        return GatewayService().getMenu(request.tableNumber)

    def CreateOrder(self, request, context):
        return GatewayService().createOrder(request.tableNumber, request.id)

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
