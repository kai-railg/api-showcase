# -*- coding: utf-8 -*-
"""
@Version ： python3.9
@Time    ： 2024/3/28 15:18
@Author  ： kai.wang
@Email   :  kai.wang@westwell-lab.com
"""

import grpc
from protobuf.hello_world import hello_world_pb2_grpc, hello_world_pb2


def run():
    # 注意这里的端口号要和服务端的一致
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = hello_world_pb2_grpc.HelloWordStub(channel)
        response = stub.SayHello(hello_world_pb2.HelloRequest(name='you'))
        print("hello world 0 received: " + response.message)
        print(response)

        resp1 = stub.SayHello1(
            iter([
                hello_world_pb2.HelloRequest(name=name) for name in ["you", "are", "u"]
            ])
        )
        print(resp1)
        print("hello world 1 received: " + resp1.message)

        resp2 = stub.SayHello2(
            hello_world_pb2.HelloRequest(name="you")
        )
        for r2 in resp2:
            print(r2)

            print("hello world 1 received: " + r2.message)

        resp3 = stub.SayHello3(
            iter([
                hello_world_pb2.HelloRequest(name=name) for name in ["you", "are", "u"]
            ])
        )
        for r3 in resp3:
            print(r3)
            print("hello world 1 received: " + r3.message)


if __name__ == '__main__':
    run()
