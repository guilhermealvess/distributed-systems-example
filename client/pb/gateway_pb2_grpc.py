# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import pb.gateway_pb2 as gateway__pb2


class ServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetMenu = channel.unary_unary(
                '/gateway.Server/GetMenu',
                request_serializer=gateway__pb2.MenuRequest.SerializeToString,
                response_deserializer=gateway__pb2.MenuResponse.FromString,
                )
        self.CreateOrder = channel.unary_unary(
                '/gateway.Server/CreateOrder',
                request_serializer=gateway__pb2.OrderRequest.SerializeToString,
                response_deserializer=gateway__pb2.OrderResponse.FromString,
                )
        self.CloseAccount = channel.unary_unary(
                '/gateway.Server/CloseAccount',
                request_serializer=gateway__pb2.CloseAccountRequest.SerializeToString,
                response_deserializer=gateway__pb2.CloseAccountResponse.FromString,
                )


class ServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetMenu(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CloseAccount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetMenu': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMenu,
                    request_deserializer=gateway__pb2.MenuRequest.FromString,
                    response_serializer=gateway__pb2.MenuResponse.SerializeToString,
            ),
            'CreateOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateOrder,
                    request_deserializer=gateway__pb2.OrderRequest.FromString,
                    response_serializer=gateway__pb2.OrderResponse.SerializeToString,
            ),
            'CloseAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.CloseAccount,
                    request_deserializer=gateway__pb2.CloseAccountRequest.FromString,
                    response_serializer=gateway__pb2.CloseAccountResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gateway.Server', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Server(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetMenu(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gateway.Server/GetMenu',
            gateway__pb2.MenuRequest.SerializeToString,
            gateway__pb2.MenuResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gateway.Server/CreateOrder',
            gateway__pb2.OrderRequest.SerializeToString,
            gateway__pb2.OrderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CloseAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gateway.Server/CloseAccount',
            gateway__pb2.CloseAccountRequest.SerializeToString,
            gateway__pb2.CloseAccountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
