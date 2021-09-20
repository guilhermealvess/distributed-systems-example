import grpc
from concurrent import futures

import pb.gateway_pb2, pb.gateway_pb2_grpc
import pb.service_sandwiche_pb2, pb.service_sandwiche_pb2_grpc
import pb.service_drink_pb2, pb.service_drink_pb2_grpc
import pb.service_dish_made_pb2, pb.service_dish_made_pb2_grpc
import pb.service_dessert_pb2, pb.service_dessert_pb2_grpc

class Server(pb.gateway_pb2_grpc.ServerServicer):
    def GetMenu(self, request, context):
        with grpc.insecure_channel('localhost:5001') as channel:
            stub = pb.service_sandwiche_pb2_grpc.SandwicheServiceStub(channel)
            findSandwichesRequest = pb.service_sandwiche_pb2.FindSandwichesRequest(tableNumber=request.tableNumber)
            sand = stub.FindSandwiches(findSandwichesRequest)
            sandwiches_response = list(map(lambda s: pb.gateway_pb2.Sandwiche(
                id=s.id,
                name=s.name,
                price=s.price,
                preparationTime=s.preparationTime,
                ingredients=s.ingredients
            ), list(sand.sandwiches)))

        with grpc.insecure_channel('localhost:5002') as channel:
            stub = pb.service_drink_pb2_grpc.DrinkServiceStub(channel)
            findDrinksRequest = pb.service_drink_pb2.FindDrinksRequest(tableNumber=request.tableNumber)
            drink = stub.FindDrinks(findDrinksRequest)
            drinks_response = list(map(lambda d: pb.gateway_pb2.Drink(
                id=d.id,
                name=d.name,
                price=d.price,
            ), list(drink.drinks)))

        with grpc.insecure_channel('localhost:5003') as channel:
            stub = pb.service_dish_made_pb2_grpc.DishMadeServiceStub(channel)
            findDishMadesRequest = pb.service_dish_made_pb2.FindDishMadeRequest(tableNumber=request.tableNumber)
            dishMades = stub.FindDishMades(findDishMadesRequest)
            dishMades_response = list(map(lambda d: pb.gateway_pb2.DishMade(
                id=d.id,
                name=d.name,
                price=d.price,
                preparationTime=d.preparationTime,
                ingredients=d.ingredients
            ), list(dishMades)))

        with grpc.insecure_channel('localhost:5004') as channel:
            stub = pb.service_dessert_pb2_grpc.DessertServiceStub(channel)
            findDessertRequest = pb.service_dessert_pb2.FindDessertRequest(request.tableNumber)
            desserts = stub.FindDesserts(findDessertRequest)
            desserts_response = list(map(lambda d: pb.gateway_pb2.Dessert(
                id=d.id,
                name=d.name,
                price=d.price
            ), list(desserts)))

        return pb.gateway_pb2.MenuResponse(sandwiches=sandwiches_response, dishMades=dishMades_response, drinks=drinks_response, desserts=desserts_response)


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
