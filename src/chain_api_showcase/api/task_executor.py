# -*- coding: utf-8 -*-

from typing import Union, Tuple, Dict
from urllib import parse

import requests
from pydantic import BaseModel
from chain_http.async_client import (
    get as async_get,
    post as async_post,
    put as async_put,
    delete as async_delete,
    AsyncHttpResponse,
)

from .api_base import ApiRequestBaseCls
from ..schemas.task_executor import *

__all__ = ["TaskExecutorRequest"]


class TaskExecutorRequestCls(ApiRequestBaseCls):
    def __init__(self):
        super(TaskExecutorRequestCls, self).__init__()
        self.SERVICE_PORT = 8100
        self.SERVICE_NAME = "task_executor"
        self.module_mapping[self.SERVICE_NAME] = self

    async def message_event_start_post(
        self, body: VehicleOrderSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Start Process
        流程启动
        """
        return await self.request(
            request=async_post,
            api="/message_event/start",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def message_event_start_post_sync(
        self, body: VehicleOrderSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Start Process
        流程启动
        """
        return self.request_sync(
            request=requests.post,
            api="/message_event/start",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def abort(
        self, vehicle_id: str, cancel_reason: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Abort Process
        中止流程
        """
        return await self.request(
            request=async_post,
            api="/message_event/abort",
            body={"params": dict(vehicle_id=vehicle_id, cancel_reason=cancel_reason)},
            resp_model=CreateSuccessSchema,
        )

    def abort_sync(
        self, vehicle_id: str, cancel_reason: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Abort Process
        中止流程
        """
        return self.request_sync(
            request=requests.post,
            api="/message_event/abort",
            body={"params": dict(vehicle_id=vehicle_id, cancel_reason=cancel_reason)},
            resp_model=CreateSuccessSchema,
        )

    async def rch(self, body: RchSchema) -> Tuple[int, CreateSuccessSchema]:
        """
        Rch

        """
        return await self.request(
            request=async_post,
            api="/message_event/rch",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def rch_sync(self, body: RchSchema) -> Tuple[int, CreateSuccessSchema]:
        """
        Rch

        """
        return self.request_sync(
            request=requests.post,
            api="/message_event/rch",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def update_qc_task(
        self, body: UpdateQcTaskSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Update Task

        """
        return await self.request(
            request=async_post,
            api="/message_event/update_qc_task",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def update_qc_task_sync(
        self, body: UpdateQcTaskSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Update Task

        """
        return self.request_sync(
            request=requests.post,
            api="/message_event/update_qc_task",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def event(
        self, body: EventListenerInSchema, event_type: ReceiveTaskType
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Event Listener

        """
        return await self.request(
            request=async_post,
            api="/message_event/event",
            body={
                "data": body.model_dump_json(),
                "params": dict(event_type=event_type),
            },
            resp_model=CreateSuccessSchema,
        )

    def event_sync(
        self, body: EventListenerInSchema, event_type: ReceiveTaskType
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Event Listener

        """
        return self.request_sync(
            request=requests.post,
            api="/message_event/event",
            body={
                "data": body.model_dump_json(),
                "params": dict(event_type=event_type),
            },
            resp_model=CreateSuccessSchema,
        )

    async def cancel_camunda_process(
        self, body: CancelCamundaSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Cancel Camunda Process

        """
        return await self.request(
            request=async_post,
            api="/message_event/cancel_camunda_process",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def cancel_camunda_process_sync(
        self, body: CancelCamundaSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Cancel Camunda Process

        """
        return self.request_sync(
            request=requests.post,
            api="/message_event/cancel_camunda_process",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def boundary_event(self, body: BoundaryEventSchema) -> Tuple[int, Dict]:
        """
        Boundary Event
        触发流程图中的 MESSAGE BOUNDARY EVENT 节点
        """
        return await self.request(
            request=async_post,
            api="/message_event/boundary_event",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def boundary_event_sync(self, body: BoundaryEventSchema) -> Tuple[int, Dict]:
        """
        Boundary Event
        触发流程图中的 MESSAGE BOUNDARY EVENT 节点
        """
        return self.request_sync(
            request=requests.post,
            api="/message_event/boundary_event",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def skip(
        self, vehicle_id: str, target_node: str, current_task_id: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        节点跳跃

        """
        return await self.request(
            request=async_post,
            api="/process_instance/skip",
            body={
                "params": dict(
                    vehicle_id=vehicle_id,
                    target_node=target_node,
                    current_task_id=current_task_id,
                )
            },
            resp_model=CreateSuccessSchema,
        )

    def skip_sync(
        self, vehicle_id: str, target_node: str, current_task_id: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        节点跳跃

        """
        return self.request_sync(
            request=requests.post,
            api="/process_instance/skip",
            body={
                "params": dict(
                    vehicle_id=vehicle_id,
                    target_node=target_node,
                    current_task_id=current_task_id,
                )
            },
            resp_model=CreateSuccessSchema,
        )

    async def activity(self, vehicle_id: str) -> Tuple[int, GetActivityNode]:
        """
        获取当前节点Name

        """
        return await self.request(
            request=async_get,
            api="/process_instance/activity",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=GetActivityNode,
        )

    def activity_sync(self, vehicle_id: str) -> Tuple[int, GetActivityNode]:
        """
        获取当前节点Name

        """
        return self.request_sync(
            request=requests.get,
            api="/process_instance/activity",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=GetActivityNode,
        )

    async def service_task(
        self, body: ServiceTaskInSchema
    ) -> Tuple[int, ServiceTaskOutSchema]:
        """ """
        return await self.request(
            request=async_post,
            api="/service_task",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=ServiceTaskOutSchema,
        )

    def service_task_sync(
        self, body: ServiceTaskInSchema
    ) -> Tuple[int, ServiceTaskOutSchema]:
        """ """
        return self.request_sync(
            request=requests.post,
            api="/service_task",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=ServiceTaskOutSchema,
        )

    async def cycle_event(
        self, body: CycleEventSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
            循环事件注册与取消
            1. 用来支持循环事件的注册和取消
        2. 注册的时候需要携带事件的名称，事件的类型，事件的回调地址，事件的回调方法
        3. 通过task info存储事件列表，列表支持去重
        4. 通过camunda循环调用触发事件，然后task executor 通知注册方
        5. 用法如下
                from chain_api_showcase.api.task_executor import TaskExecutorRequest
                from chain_api_showcase.schemas.task_executor import CycleEventSchema

                status, resp = await TaskExecutorRequest.cycle_event(
                    CycleEventSchema(
                        event_name="container_update",
                        event_type="publish",
                        callback_module_name="inventory",
                        callback_path="/api/event/KpiEventCallback",
                        callback_method="post"
                    )
                )
        """
        return await self.request(
            request=async_post,
            api="/event/cycle_event",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def cycle_event_sync(
        self, body: CycleEventSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
            循环事件注册与取消
            1. 用来支持循环事件的注册和取消
        2. 注册的时候需要携带事件的名称，事件的类型，事件的回调地址，事件的回调方法
        3. 通过task info存储事件列表，列表支持去重
        4. 通过camunda循环调用触发事件，然后task executor 通知注册方
        5. 用法如下
                from chain_api_showcase.api.task_executor import TaskExecutorRequest
                from chain_api_showcase.schemas.task_executor import CycleEventSchema

                status, resp = await TaskExecutorRequest.cycle_event(
                    CycleEventSchema(
                        event_name="container_update",
                        event_type="publish",
                        callback_module_name="inventory",
                        callback_path="/api/event/KpiEventCallback",
                        callback_method="post"
                    )
                )
        """
        return self.request_sync(
            request=requests.post,
            api="/event/cycle_event",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def event_driven(
        self, body: EventDrivenSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
            事件驱动的发布、订阅、取消
            1. 用来支持事件驱动的发布、订阅和取消, 注册者需要实现一个回调接口，并在注册的时候当作参数传入
        2. 注册的时候需要携带事件的名称，事件的类型，事件的回调地址，事件的回调方法
        3. 通过task info存储事件列表，列表支持去重
        4. 事件发布时，通过事件列表，根据 module_name 找到对应的url（需要在chain-api-showcase 库中生成对应的module_name）, 推送给订阅者
        5. 场景适用于：需要循环请求数据，但是数据变动不频繁，为了减少请求次数，可以使用事件驱动
        5. 用法如下
                from chain_api_showcase.api.task_executor import TaskExecutorRequest
                from chain_api_showcase.schemas.task_executor import EventDrivenSchema
                await TaskExecutorRequest.event_driven(
                    EventDrivenSchema(
                        event_name="container_update",
                        event_type="publish", # publish 发布事件, subscribe 订阅事件, cancel 取消注册
                        callback_module_name="inventory",
                        callback_path="/api/event/KpiEventCallback",
                        callback_method="post"
                    )
                )
        """
        return await self.request(
            request=async_post,
            api="/event/event_driven",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def event_driven_sync(
        self, body: EventDrivenSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
            事件驱动的发布、订阅、取消
            1. 用来支持事件驱动的发布、订阅和取消, 注册者需要实现一个回调接口，并在注册的时候当作参数传入
        2. 注册的时候需要携带事件的名称，事件的类型，事件的回调地址，事件的回调方法
        3. 通过task info存储事件列表，列表支持去重
        4. 事件发布时，通过事件列表，根据 module_name 找到对应的url（需要在chain-api-showcase 库中生成对应的module_name）, 推送给订阅者
        5. 场景适用于：需要循环请求数据，但是数据变动不频繁，为了减少请求次数，可以使用事件驱动
        5. 用法如下
                from chain_api_showcase.api.task_executor import TaskExecutorRequest
                from chain_api_showcase.schemas.task_executor import EventDrivenSchema
                await TaskExecutorRequest.event_driven(
                    EventDrivenSchema(
                        event_name="container_update",
                        event_type="publish", # publish 发布事件, subscribe 订阅事件, cancel 取消注册
                        callback_module_name="inventory",
                        callback_path="/api/event/KpiEventCallback",
                        callback_method="post"
                    )
                )
        """
        return self.request_sync(
            request=requests.post,
            api="/event/event_driven",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def abort_all_event_process(self) -> Tuple[int, CreateSuccessSchema]:
        """
        取消事件流程
        取消循环、订阅、事件驱动的camunda流程, 并清空任务列表
        """
        return await self.request(
            request=async_post,
            api="/event/abort_all_event_process",
            body={},
            resp_model=CreateSuccessSchema,
        )

    def abort_all_event_process_sync(self) -> Tuple[int, CreateSuccessSchema]:
        """
        取消事件流程
        取消循环、订阅、事件驱动的camunda流程, 并清空任务列表
        """
        return self.request_sync(
            request=requests.post,
            api="/event/abort_all_event_process",
            body={},
            resp_model=CreateSuccessSchema,
        )


TaskExecutorRequest = TaskExecutorRequestCls()
