# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import pb.service_sandwiche_pb2 as service__sandwiche__pb2


class SandwicheServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.FindSandwiches = channel.unary_unary(
                '/sandwicheService.SandwicheService/FindSandwiches',
                request_serializer=service__sandwiche__pb2.FindSandwichesRequest.SerializeToString,
                response_deserializer=service__sandwiche__pb2.FindSandwichesResponse.FromString,
                )


class SandwicheServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def FindSandwiches(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SandwicheServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'FindSandwiches': grpc.unary_unary_rpc_method_handler(
                    servicer.FindSandwiches,
                    request_deserializer=service__sandwiche__pb2.FindSandwichesRequest.FromString,
                    response_serializer=service__sandwiche__pb2.FindSandwichesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sandwicheService.SandwicheService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SandwicheService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def FindSandwiches(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sandwicheService.SandwicheService/FindSandwiches',
            service__sandwiche__pb2.FindSandwichesRequest.SerializeToString,
            service__sandwiche__pb2.FindSandwichesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
