import grpc
from google.protobuf.json_format import MessageToJson
import json
from pprint import pprint

import pb.gateway_pb2, pb.gateway_pb2_grpc


""" with grpc.insecure_channel('localhost:5000') as channel:
    stub = pb.gateway_pb2_grpc.ServerStub(channel)
    request = pb.gateway_pb2.MenuRequest(tableNumber = 9)
    response = stub.GetMenu(request)
    json_obj = json.loads(MessageToJson(response))
    pprint(json_obj) """

with grpc.insecure_channel('localhost:5000') as channel:
    stub = pb.gateway_pb2_grpc.ServerStub(channel)
    request = pb.gateway_pb2.OrderRequest(id=[
        "614f792b837ceb4deaafcbe8",                     #Sandwiches
        "614f792b837ceb4deaafcbe9",                     #Sandwiches
        "614f792b837ceb4deaafcbf5",                     #drink
        "614f792b837ceb4deaafcbfd",                     #dessert
        "614f792b837ceb4deaafcbfe"                      #dessert
        ], tableNumber=2)
    response = stub.CreateOrder(request)
    json_obj = json.loads(MessageToJson(response))
    pprint(json_obj)

with grpc.insecure_channel('localhost:5000') as channel:
    stub = pb.gateway_pb2_grpc.ServerStub(channel)
    request = pb.gateway_pb2.CloseAccountRequest(tableNumber=2)
    response = stub.CloseAccount(request)
    json_obj = json.loads(MessageToJson(response))
    pprint(json_obj)