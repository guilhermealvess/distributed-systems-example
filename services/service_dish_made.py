import time, random

import grpc
from concurrent import futures

import pb.service_dish_made_pb2, pb.service_dish_made_pb2_grpc
from database.database import Database


class DishMadeService:
    def __init__(self) -> None:
        self.collectionDb = 'dishMade'

    def findDishMades(self):
        return Database().findAll(self.collectionDb)

    def findDishMadeBy(self, id):
        return Database().findById(self.collectionDb, id)


class DishMadeServer(pb.service_dish_made_pb2_grpc.DishMadeServiceServicer):
    def FindDishMades(self, request, context):
        dishMades = DishMadeService().findDishMades()
        print(dishMades)
        response = list(map(lambda d: pb.service_dish_made_pb2.DishMade(
            id=str(d['_id']),
            name=d['name'],
            price=d['price'],
            ingredients=d['ingredients']
        ), dishMades))
        return pb.service_dish_made_pb2.FindDishMadeResponse(dishMades=response)

    def ExecuteOrder(self, request, context):
        foods = list()
        preparationTimeTotal = 0
        for id in request.id:
            dishMade = DishMadeService().findDishMadeBy(id)
            if dishMade:
                preparationTime = dishMade.get('preparationTime', random.randint(20,120))
                time.sleep(preparationTime/10)
                foods.append(dishMade['name'])
                preparationTimeTotal += preparationTime

        return pb.service_dish_made_pb2.OrderResponse(foods=foods, preparationTime=preparationTimeTotal)



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