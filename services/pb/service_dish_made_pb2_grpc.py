# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import pb.service_dish_made_pb2 as service__dish__made__pb2


class DishMadeServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.FindDishMades = channel.unary_unary(
                '/dishMadeService.DishMadeService/FindDishMades',
                request_serializer=service__dish__made__pb2.FindDishMadeRequest.SerializeToString,
                response_deserializer=service__dish__made__pb2.FindDishMadeResponse.FromString,
                )
        self.ExecuteOrder = channel.unary_unary(
                '/dishMadeService.DishMadeService/ExecuteOrder',
                request_serializer=service__dish__made__pb2.OrderRequest.SerializeToString,
                response_deserializer=service__dish__made__pb2.OrderResponse.FromString,
                )


class DishMadeServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def FindDishMades(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExecuteOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DishMadeServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'FindDishMades': grpc.unary_unary_rpc_method_handler(
                    servicer.FindDishMades,
                    request_deserializer=service__dish__made__pb2.FindDishMadeRequest.FromString,
                    response_serializer=service__dish__made__pb2.FindDishMadeResponse.SerializeToString,
            ),
            'ExecuteOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.ExecuteOrder,
                    request_deserializer=service__dish__made__pb2.OrderRequest.FromString,
                    response_serializer=service__dish__made__pb2.OrderResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dishMadeService.DishMadeService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DishMadeService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def FindDishMades(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dishMadeService.DishMadeService/FindDishMades',
            service__dish__made__pb2.FindDishMadeRequest.SerializeToString,
            service__dish__made__pb2.FindDishMadeResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/dishMadeService.DishMadeService/ExecuteOrder',
            service__dish__made__pb2.OrderRequest.SerializeToString,
            service__dish__made__pb2.OrderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
