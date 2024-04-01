# -*- coding: utf-8 -*-
"""
@Version ： python3.9
@Time    ： 2024/3/28 15:18
@Author  ： kai.wang
@Email   :  kai.wang@westwell-lab.com
"""
import time
import types
from concurrent import futures
import grpc
from protobuf.hello_world import hello_world_pb2, hello_world_pb2_grpc


def func_decorator(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        res.timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t1))
        res.duration = int((time.time() - t1) * 1000)
        return res

    return wrapper


def iter_func_decorator(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        for item in func(*args, **kwargs):
            item.timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t1))
            item.duration = int((time.time() - t1) * 1000)
            yield item

    return wrapper


class HelloWorldService(hello_world_pb2_grpc.HelloWordServicer):
    @func_decorator
    def SayHello(self, request, context):
        return hello_world_pb2.HelloReply(message='Hello, %s!' % request.name)

    @func_decorator
    def SayHello1(self, request_iterator, context):
        for request in request_iterator:
            return hello_world_pb2.HelloReply(message='Hello, %s!' % request.name)

    @iter_func_decorator
    def SayHello2(self, request, context):
        for i in range(3):
            yield hello_world_pb2.HelloReply(message='Hello, %s!' % request.name)

    @iter_func_decorator
    def SayHello3(self, request_iterator, context):
        for request in request_iterator:
            yield hello_world_pb2.HelloReply(message='Hello, %s!' % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_world_pb2_grpc.add_HelloWordServicer_to_server(HelloWorldService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
