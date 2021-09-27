import time, random
from concurrent import futures

import grpc

import pb.service_dessert_pb2, pb.service_dessert_pb2_grpc
from database.database import Database


class DessertService:
    def __init__(self) -> None:
        self.collectionDb = 'dessert'

    def findDesserts(self):
        return Database().findAll(self.collectionDb)

    def findDessertById(self, id):
        return Database().findById(self.collectionDb, id)


class DessertServer(pb.service_dessert_pb2_grpc.DessertServiceServicer):
    def FindDesserts(self, request, context):
        desserts = DessertService().findDesserts()
        response = list(map(lambda d: pb.service_dessert_pb2.Dessert(
            id=str(d['_id']),
            name=d['name'],
            price=d['price']
        ), desserts))
        return pb.service_dessert_pb2.FindDessertResponse(desserts=response)

    def ExecuteOrder(self, request, context):
        foods = list()
        preparationTimeTotal = 0
        for id in request.id:
            dessert = DessertService().findDessertById(id)
            if dessert:
                preparationTime = dessert.get('preparationTime', random.randint(20,120))
                time.sleep(preparationTime/10)
                foods.append(dessert['name'])
                preparationTimeTotal += preparationTime
        print(foods)
        return pb.service_dessert_pb2.OrderResponse(foods=foods, preparationTime=preparationTimeTotal)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb.service_dessert_pb2_grpc.add_DessertServiceServicer_to_server(DessertServer(), server)

    port = 5004
    server.add_insecure_port('[::]:{}'.format(port))
    print('RUNNING IN PORT {} ...'.format(port))
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()