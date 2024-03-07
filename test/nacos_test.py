# -*- coding: utf-8 -*-
"""
@Version ： python3.9
@Time    ： 2024/3/7 10:54 AM
@Author  ： kai.wang
@Email   :  kai.wang@westwell-lab.com
"""

import asyncio
from chain_http import aio_http
from chain_nacos.service_manager import ServiceManager

# 新建一个 ServiceManager 对象，参数为 nacos 的地址
service = ServiceManager("http://10.6.64.99:8848")

# 把自己注册到 nacos 中，比如 device_info 提供了 http 和 grpc 两个服务
service.register("device_info_http", "10.103.40.10", 11000)
service.register("device_info_grpc", "10.103.40.10", 10003)


# 调用别的服务，指定服务名, 随机获取一个实例的 host 和 port
# get_random_instance 会请求一次 nacos, 避免每次重新请求的方法可以参考 "监听服务变化" 一节
async def get_task_status():
    device_info_ins = service.get_random_instance("device_info_http")
    host, port = device_info_ins["ip"], device_info_ins["port"]
    print(device_info_ins)
    url = f"http://{host}:{port}/api/taskInfo/maintain/status"

    service.listen_service("task_info")
    # service.deregister("device_info_http", "10.103.40.10", 11000)
    # service.deregister("device_info_grpc", "10.103.40.10", 10003)
    #
    # device_info_ins = service.get_random_instance("device_info_http")
    # print(device_info_ins)

asyncio.run(get_task_status())
