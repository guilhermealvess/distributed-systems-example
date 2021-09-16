import time
import grpc
from concurrent import futures

from database.database import Database
import pb.service_sandwiche_pb2, pb.service_sandwiche_pb2_grpc


class DepartmentSandwicheService:
    def __init__(self) -> None:
        pass

    def findSandwiches(self):
        db = Database()
        return db.findAll('sandwiches')



class SandwicheService(pb.service_sandwiche_pb2_grpc.SandwicheServiceServicer):
    def FindSandwiches(self, request, context):
        departmentSandwicheService = DepartmentSandwicheService()
        sandwiches = departmentSandwicheService.findSandwiches()
        response = list(map(lambda x: pb.service_sandwiche_pb2.Sandwiche(
            id=str(x['_id']),
            name=x['name'],
            price=x['price'],
            preparationTime=x['preparationTime'],
            ingredients=x['ingredients']
        ), sandwiches))

        return pb.service_sandwiche_pb2.FindSandwichesResponse(sandwiches=response)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb.service_sandwiche_pb2_grpc.add_SandwicheServiceServicer_to_server(SandwicheService(), server)
    server.add_insecure_port('[::]:5001')
    print('RUNNING IN PORT 5001 ...')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
