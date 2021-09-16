import grpc
from google.protobuf.json_format import MessageToJson
import json

import pb.gateway_pb2 as gateway
import pb.gateway_pb2_grpc as gatewayGRPC

with grpc.insecure_channel('localhost:5001') as channel:
    stub = gatewayGRPC.ServerStub(channel)
    request = gateway.MenuRequest(tableNumber = 9)
    response = stub.GetMenu(request)
    json_obj = json.loads(MessageToJson(response))
