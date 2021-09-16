import grpc
from concurrent import futures

import pb.service_pb2, pb.service_pb2_grpc
from sandwiche_service import SandwicheService


class SandwicheService(pb.service_pb2_grpc.SandwicheServiceServicer):
    def FindSandwiches(self, request, context):
        sandwiches = SandwicheService.findSandwiches()
        response = list(map(lambda x: pb.service_pb2.Sandwiche(
            id=x['id'],
            name=x['name'],
            price=x['price'],
            preparationTime=x['preparationTime'],
            ingredients=x['ingredients']
        ), sandwiches))
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb.gateway_pb2_grpc.add_ServerServicer_to_server(SandwicheService(), server)
    server.add_insecure_port('[::]:5001')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
