# chain-api-show

## Description

chai-api-show 模块旨在帮助您快速了解和使用当前项目中所有使用的 OpenAPI 文档。

该模块通过 OpenAPI 3.0 格式的 OpenAPI 文档，生成适用于多种 HTTP 请求工具和库的代码片段。

该模块使用pydantic模型生成了请求参数和返回参数的代码片段，以供您在实际开发中了解请求参数和返回值的结构，而无需阅读 OpenAPI 文档来了解这些结构。

同时支持了异步和同步函数调用。

支持nacos注册中心和单机模式，通过配置切换。

当前支持的模块: camunda, crane_info, device_info, gui_server, integrator, inventory, route_interface, task_executor, task_info, scheduler, tos_interface, vehicle_manager

## Features

- **循环事件注册**: task_executor 模块定义了事件循环注册，用于支持注册后有参数的和固定频率的接口回调，循环事件由camunda驱动。
- **驱动事件注册**: task_executor 模块定义了驱动事件注册，用于实现http版本的发布订阅机制，订阅方需要进行注册和事件通知接口。

## Getting Started

```shell
git clone ssh://git@devgit.westwell.cc:10080/kai.wang/chain-api-showcase.git
cd chai-api-show
pip install -r requirements.txt
python3 main.py