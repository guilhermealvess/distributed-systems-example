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
        "61491d8ec4787a66624569d0",
        "61491d8ec4787a66624569d7",
        "61491d8ec4787a66624569dc",
        "61491d8ec4787a66624569d8",
        "61491d8ec4787a66624569e4"], tableNumber=2)
    response = stub.CreateOrder(request)
    json_obj = json.loads(MessageToJson(response))
    pprint(json_obj)