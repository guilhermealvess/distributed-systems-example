import time, random
import grpc
from concurrent import futures

from database.database import Database
import pb.service_sandwiche_pb2, pb.service_sandwiche_pb2_grpc


class DepartmentSandwicheService:
    def __init__(self) -> None:
        self.collectionDb = 'sandwiches'

    def findSandwiches(self):
        db = Database()
        return db.findAll(self.collectionDb)

    def findSandwiche(self, id):
        return Database().findById(self.collectionDb, id)


class SandwicheService(pb.service_sandwiche_pb2_grpc.SandwicheServiceServicer):
    def FindSandwiches(self, request, context):
        departmentSandwicheService = DepartmentSandwicheService()
        sandwiches = departmentSandwicheService.findSandwiches()
        response = list(map(lambda s: pb.service_sandwiche_pb2.Sandwiche(
            id=str(s['_id']),
            name=s['name'],
            price=s['price'],
            preparationTime=s['preparationTime'],
            ingredients=s['ingredients']
        ), sandwiches))

        return pb.service_sandwiche_pb2.FindSandwichesResponse(sandwiches=response)

    def ExecuteOrder(self, request, context):
        foods = list()
        preparationTimeTotal = 0
        for id in request.id:
            sandwiche = DepartmentSandwicheService().findSandwiche(id)
            if sandwiche:
                preparationTime = sandwiche.get('preparationTime', random.randint(20,120))
                time.sleep(preparationTime/10)
                foods.append(sandwiche['name'])
                preparationTimeTotal += preparationTime

        return pb.service_sandwiche_pb2.OrderResponse(foods=foods, preparationTime=preparationTimeTotal)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb.service_sandwiche_pb2_grpc.add_SandwicheServiceServicer_to_server(SandwicheService(), server)
    
    port = 5001
    server.add_insecure_port('[::]:{}'.format(port))
    print('RUNNING IN PORT {} ...'.format(port))
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
