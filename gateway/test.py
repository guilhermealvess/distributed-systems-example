import grpc
from google.protobuf.json_format import MessageToJson
import json
from pprint import pprint

import pb.service_sandwiche_pb2
import pb.service_sandwiche_pb2_grpc


""" with grpc.insecure_channel('localhost:5001', options=(('grpc.enable_http_proxy', 0),)) as channel:
    stub = pb.service_sandwiche_pb2_grpc.SandwicheServiceStub(channel)

    request = pb.service_sandwiche_pb2.FindSandwichesRequest(tableNumber=9)
    response = stub.FindSandwiches(request)

    json_obj = json.loads(MessageToJson(response))
    pprint(json_obj)
 """

with grpc.insecure_channel('localhost:5001') as channel:
    stub = pb.service_sandwiche_pb2_grpc.SandwicheServiceStub(channel)

    request = pb.service_sandwiche_pb2.OrderRequest(id=["6148a57673a8ca711ce825cb", "6148a57673a8ca711ce825cc"])
    response = stub.ExecuteOrder(request)

    json_obj = json.loads(MessageToJson(response))
    pprint(json_obj)