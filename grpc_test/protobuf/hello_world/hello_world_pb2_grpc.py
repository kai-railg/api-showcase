# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protobuf.hello_world import hello_world_pb2 as src_dot_protobuf_dot_hello__world_dot_hello__world__pb2


class HelloWordStub(object):
    """定义gRPC服务
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayHello = channel.unary_unary(
                '/helloworld.HelloWord/SayHello',
                request_serializer=src_dot_protobuf_dot_hello__world_dot_hello__world__pb2.HelloRequest.SerializeToString,
                response_deserializer=src_dot_protobuf_dot_hello__world_dot_hello__world__pb2.HelloReply.FromString,
                )
        self.SayHello1 = channel.stream_unary(
                '/helloworld.HelloWord/SayHello1',
                request_serializer=src_dot_protobuf_dot_hello__world_dot_hello__world__pb2.HelloRequest.SerializeToString,
                response_deserializer=src_dot_protobuf_dot_hello__world_dot_hello__world__pb2.HelloReply.FromString,
                )
        self.SayHello2 = channel.unary_stream(
                '/helloworld.HelloWord/SayHello2',
                request_serializer=src_dot_protobuf_dot_hello__world_dot_hello__world__pb2.HelloRequest.SerializeToString,
                response_deserializer=src_dot_protobuf_dot_hello__world_dot_hello__world__pb2.HelloReply.FromString,
                )
        self.SayHello3 = channel.stream_stream(
                '/helloworld.HelloWord/SayHello3',
                request_serializer=src_dot_protobuf_dot_hello__world_dot_hello__world__pb2.HelloRequest.SerializeToString,
                response_deserializer=src_dot_protobuf_dot_hello__world_dot_hello__world__pb2.HelloReply.FromString,
                )


class HelloWordServicer(object):
    """定义gRPC服务
    """

    def SayHello(self, request, context):
        """定义一个RPC方法
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SayHello1(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SayHello2(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SayHello3(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HelloWordServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello,
                    request_deserializer=src_dot_protobuf_dot_hello__world_dot_hello__world__pb2.HelloRequest.FromString,
                    response_serializer=src_dot_protobuf_dot_hello__world_dot_hello__world__pb2.HelloReply.SerializeToString,
            ),
            'SayHello1': grpc.stream_unary_rpc_method_handler(
                    servicer.SayHello1,
                    request_deserializer=src_dot_protobuf_dot_hello__world_dot_hello__world__pb2.HelloRequest.FromString,
                    response_serializer=src_dot_protobuf_dot_hello__world_dot_hello__world__pb2.HelloReply.SerializeToString,
            ),
            'SayHello2': grpc.unary_stream_rpc_method_handler(
                    servicer.SayHello2,
                    request_deserializer=src_dot_protobuf_dot_hello__world_dot_hello__world__pb2.HelloRequest.FromString,
                    response_serializer=src_dot_protobuf_dot_hello__world_dot_hello__world__pb2.HelloReply.SerializeToString,
            ),
            'SayHello3': grpc.stream_stream_rpc_method_handler(
                    servicer.SayHello3,
                    request_deserializer=src_dot_protobuf_dot_hello__world_dot_hello__world__pb2.HelloRequest.FromString,
                    response_serializer=src_dot_protobuf_dot_hello__world_dot_hello__world__pb2.HelloReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'helloworld.HelloWord', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class HelloWord(object):
    """定义gRPC服务
    """

    @staticmethod
    def SayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld.HelloWord/SayHello',
            src_dot_protobuf_dot_hello__world_dot_hello__world__pb2.HelloRequest.SerializeToString,
            src_dot_protobuf_dot_hello__world_dot_hello__world__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SayHello1(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/helloworld.HelloWord/SayHello1',
            src_dot_protobuf_dot_hello__world_dot_hello__world__pb2.HelloRequest.SerializeToString,
            src_dot_protobuf_dot_hello__world_dot_hello__world__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SayHello2(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/helloworld.HelloWord/SayHello2',
            src_dot_protobuf_dot_hello__world_dot_hello__world__pb2.HelloRequest.SerializeToString,
            src_dot_protobuf_dot_hello__world_dot_hello__world__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SayHello3(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/helloworld.HelloWord/SayHello3',
            src_dot_protobuf_dot_hello__world_dot_hello__world__pb2.HelloRequest.SerializeToString,
            src_dot_protobuf_dot_hello__world_dot_hello__world__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
