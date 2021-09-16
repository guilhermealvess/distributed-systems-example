import grpc
from concurrent import futures

import pb.gateway_pb2 as gateway
import pb.gateway_pb2_grpc
import pb.service_sandwiche_pb2
import pb.service_sandwiche_pb2_grpc


class Server(pb.gateway_pb2_grpc.ServerServicer):
    def GetMenu(self, request, context):
        #sandwiche = gateway.Sandwiche(id='123', name='X-Salada', price=25.99, preparationTime=120, ingredients=["Pão", "Alface"])
        #return gateway.MenuRepply(sandwiches=[sandwiche], dishMades=[], drinks=[], desserts=[])
        # dishMade = gateway.DishMade(id='123', name='X-Salada', price=25.99, preparationTime=120, ingredients=["Pão", "Alface"] )

        with grpc.insecure_channel('localhost:5001') as channel:
            stub = pb.service_sandwiche_pb2_grpc.SandwicheServiceStub(channel)
            findSandwichesRequest = pb.service_sandwiche_pb2.FindSandwichesRequest(tableNumber=request.tableNumber)
            sand = stub.FindSandwiches(findSandwichesRequest)
            return gateway.MenuRepply(sandwiches=sand, dishMades=[], drinks=[], desserts=[])


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb.gateway_pb2_grpc.add_ServerServicer_to_server(Server(), server)
    server.add_insecure_port('[::]:5000')
    print('RUNNING IN PORT 5000\n')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
