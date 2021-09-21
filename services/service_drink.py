import time
import grpc
from concurrent import futures

from database.database import Database
import pb.service_drink_pb2, pb.service_drink_pb2_grpc


class DepartmentDrinkService:
    def findDrinks(self):
        db = Database()
        return db.findAll('drinks')


class DrinkServiceGRPC(pb.service_drink_pb2_grpc.DrinkServiceServicer):
    def FindDrinks(self, request, context):
        drinks = DepartmentDrinkService().findDrinks()
        res = list(map(lambda d: pb.service_drink_pb2.Drink(
            id=str(d['_id']),
            name=d['name'],
            price=d['price']
        ), drinks))

        return pb.service_drink_pb2.FindDrinksResponse(drinks=res)

    def ExecuteOrder(self, request, context):
        foods = list()
        preparationTimeTotal = 0
        for id in request.id:
            drink = DepartmentDrinkService().findDrinks(id)
            if drink:
                preparationTime = 10
                time.sleep(preparationTime/10)
                foods.append(drink['name'])
                preparationTimeTotal += preparationTime

        return pb.service_drink_pb2.OrderResponse(foods=foods, preparationTime=preparationTimeTotal)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb.service_drink_pb2_grpc.add_DrinkServiceServicer_to_server(DrinkServiceGRPC(), server)

    port = 5002
    server.add_insecure_port('[::]:{}'.format(port))
    print('RUNNING IN PORT {} ...'.format(port))
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()