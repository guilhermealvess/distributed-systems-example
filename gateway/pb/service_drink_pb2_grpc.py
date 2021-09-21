# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import pb.service_drink_pb2 as service__drink__pb2


class DrinkServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.FindDrinks = channel.unary_unary(
                '/drinkService.DrinkService/FindDrinks',
                request_serializer=service__drink__pb2.FindDrinksRequest.SerializeToString,
                response_deserializer=service__drink__pb2.FindDrinksResponse.FromString,
                )
        self.ExecuteOrder = channel.unary_unary(
                '/drinkService.DrinkService/ExecuteOrder',
                request_serializer=service__drink__pb2.OrderRequest.SerializeToString,
                response_deserializer=service__drink__pb2.OrderResponse.FromString,
                )


class DrinkServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def FindDrinks(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExecuteOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DrinkServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'FindDrinks': grpc.unary_unary_rpc_method_handler(
                    servicer.FindDrinks,
                    request_deserializer=service__drink__pb2.FindDrinksRequest.FromString,
                    response_serializer=service__drink__pb2.FindDrinksResponse.SerializeToString,
            ),
            'ExecuteOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.ExecuteOrder,
                    request_deserializer=service__drink__pb2.OrderRequest.FromString,
                    response_serializer=service__drink__pb2.OrderResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'drinkService.DrinkService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DrinkService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def FindDrinks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/drinkService.DrinkService/FindDrinks',
            service__drink__pb2.FindDrinksRequest.SerializeToString,
            service__drink__pb2.FindDrinksResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/drinkService.DrinkService/ExecuteOrder',
            service__drink__pb2.OrderRequest.SerializeToString,
            service__drink__pb2.OrderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
