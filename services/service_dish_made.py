import time

import grpc
from concurrent import futures

import pb.service_dish_made_pb2, pb.service_dish_made_pb2_grpc
from database.database import Database


class DishMadeService:
    def findDishMade(self):
        return Database().findAll('dishMades')


class DishMadeServer(pb.service_dish_made_pb2_grpc.DishMadeServiceServicer):
    def FindDishMades(self, request, context):
        dishMades = DishMadeService().findDishMade()
        response = list(map(lambda d: pb.service_dish_made_pb2.DishMade(
            id=str(d['_id']),
            name=d['name'],
            price=d['name'],
            preparationTime=d['preparationTime'],
            ingredients=d['ingredients']
        ), dishMades))
        return pb.service_dish_made_pb2.FindDishMadeResponse(dishMades=response)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb.service_dish_made_pb2_grpc.add_DishMadeServiceServicer_to_server(DishMadeServer(), server)

    port = 5003
    server.add_insecure_port('[::]:{}'.format(port))
    print('RUNNING IN PORT {} ...'.format(port))
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()