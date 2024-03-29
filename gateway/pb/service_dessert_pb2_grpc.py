# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import pb.service_dessert_pb2 as service__dessert__pb2


class DessertServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.FindDesserts = channel.unary_unary(
                '/dessertService.DessertService/FindDesserts',
                request_serializer=service__dessert__pb2.FindDessertRequest.SerializeToString,
                response_deserializer=service__dessert__pb2.FindDessertResponse.FromString,
                )
        self.ExecuteOrder = channel.unary_unary(
                '/dessertService.DessertService/ExecuteOrder',
                request_serializer=service__dessert__pb2.OrderRequest.SerializeToString,
                response_deserializer=service__dessert__pb2.OrderResponse.FromString,
                )


class DessertServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def FindDesserts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExecuteOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DessertServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'FindDesserts': grpc.unary_unary_rpc_method_handler(
                    servicer.FindDesserts,
                    request_deserializer=service__dessert__pb2.FindDessertRequest.FromString,
                    response_serializer=service__dessert__pb2.FindDessertResponse.SerializeToString,
            ),
            'ExecuteOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.ExecuteOrder,
                    request_deserializer=service__dessert__pb2.OrderRequest.FromString,
                    response_serializer=service__dessert__pb2.OrderResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dessertService.DessertService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DessertService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def FindDesserts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dessertService.DessertService/FindDesserts',
            service__dessert__pb2.FindDessertRequest.SerializeToString,
            service__dessert__pb2.FindDessertResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExecuteOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dessertService.DessertService/ExecuteOrder',
            service__dessert__pb2.OrderRequest.SerializeToString,
            service__dessert__pb2.OrderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
