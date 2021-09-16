import grpc
from google.protobuf.json_format import MessageToJson
import json
from pprint import pprint

import pb.gateway_pb2
import pb.gateway_pb2_grpc


with grpc.insecure_channel('localhost:5000') as channel:
    stub = pb.gateway_pb2_grpc.ServerStub(channel)
    request = pb.gateway_pb2.MenuRequest(tableNumber = 9)
    response = stub.GetMenu(request)
    json_obj = json.loads(MessageToJson(response))
    pprint(json_obj)
