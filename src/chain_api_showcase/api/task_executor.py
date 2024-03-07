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
        resp = await async_post(
            url=parse.urljoin(self.url, "/message_event/start"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /message_event/start, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    def message_event_start_post_sync(
        self, body: VehicleOrderSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Start Process
        流程启动
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/message_event/start"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /message_event/start, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, CreateSuccessSchema.model_validate_json(resp)

    async def abort(
        self, vehicle_id: str, cancel_reason: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Abort Process
        中止流程
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/message_event/abort"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id, cancel_reason=cancel_reason),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /message_event/abort, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    def abort_sync(
        self, vehicle_id: str, cancel_reason: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Abort Process
        中止流程
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/message_event/abort"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id, cancel_reason=cancel_reason),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /message_event/abort, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, CreateSuccessSchema.model_validate_json(resp)

    async def rch(self, body: RchSchema) -> Tuple[int, CreateSuccessSchema]:
        """
        Rch

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/message_event/rch"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /message_event/rch, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    def rch_sync(self, body: RchSchema) -> Tuple[int, CreateSuccessSchema]:
        """
        Rch

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/message_event/rch"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /message_event/rch, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, CreateSuccessSchema.model_validate_json(resp)

    async def update_qc_task(
        self, body: UpdateQcTaskSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Update Task

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/message_event/update_qc_task"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /message_event/update_qc_task, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    def update_qc_task_sync(
        self, body: UpdateQcTaskSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Update Task

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/message_event/update_qc_task"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /message_event/update_qc_task, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, CreateSuccessSchema.model_validate_json(resp)

    async def event(
        self, body: EventListenerInSchema, event_type: ReceiveTaskType
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Event Listener

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/message_event/event"),
            timeout=self.timeout,
            json=body.dict(),
            params=dict(event_type=event_type),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /message_event/event, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    def event_sync(
        self, body: EventListenerInSchema, event_type: ReceiveTaskType
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Event Listener

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/message_event/event"),
            timeout=self.timeout,
            json=body.dict(),
            params=dict(event_type=event_type),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /message_event/event, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, CreateSuccessSchema.model_validate_json(resp)

    async def cancel_camunda_process(
        self, body: CancelCamundaSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Cancel Camunda Process

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/message_event/cancel_camunda_process"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /message_event/cancel_camunda_process, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    def cancel_camunda_process_sync(
        self, body: CancelCamundaSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Cancel Camunda Process

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/message_event/cancel_camunda_process"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /message_event/cancel_camunda_process, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, CreateSuccessSchema.model_validate_json(resp)

    async def boundary_event(self, body: BoundaryEventSchema) -> Tuple[int, Dict]:
        """
        Boundary Event
        触发流程图中的 MESSAGE BOUNDARY EVENT 节点
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/message_event/boundary_event"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /message_event/boundary_event, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def boundary_event_sync(self, body: BoundaryEventSchema) -> Tuple[int, Dict]:
        """
        Boundary Event
        触发流程图中的 MESSAGE BOUNDARY EVENT 节点
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/message_event/boundary_event"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /message_event/boundary_event, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def skip(
        self, vehicle_id: str, target_node: str, current_task_id: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        节点跳跃

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/process_instance/skip"),
            timeout=self.timeout,
            params=dict(
                vehicle_id=vehicle_id,
                target_node=target_node,
                current_task_id=current_task_id,
            ),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /process_instance/skip, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    def skip_sync(
        self, vehicle_id: str, target_node: str, current_task_id: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        节点跳跃

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/process_instance/skip"),
            timeout=self.timeout,
            params=dict(
                vehicle_id=vehicle_id,
                target_node=target_node,
                current_task_id=current_task_id,
            ),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /process_instance/skip, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, CreateSuccessSchema.model_validate_json(resp)

    async def activity(self, vehicle_id: str) -> Tuple[int, GetActivityNode]:
        """
        获取当前节点Name

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/process_instance/activity"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /process_instance/activity, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, GetActivityNode.model_validate_json(resp)

    def activity_sync(self, vehicle_id: str) -> Tuple[int, GetActivityNode]:
        """
        获取当前节点Name

        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/process_instance/activity"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /process_instance/activity, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, GetActivityNode.model_validate_json(resp)

    async def service_task(
        self, body: ServiceTaskInSchema
    ) -> Tuple[int, ServiceTaskOutSchema]:
        """ """
        resp = await async_post(
            url=parse.urljoin(self.url, "/service_task"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /service_task, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, ServiceTaskOutSchema.model_validate_json(resp)

    def service_task_sync(
        self, body: ServiceTaskInSchema
    ) -> Tuple[int, ServiceTaskOutSchema]:
        """ """
        resp = requests.post(
            url=parse.urljoin(self.url, "/service_task"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /service_task, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, ServiceTaskOutSchema.model_validate_json(resp)

    async def cycle_event(
        self, body: CycleEventSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        循环事件注册与取消
        用来支持循环事件的注册和取消通过task info存储事件列表，列表支持去重通过camunda循环事件的定义触发事件执行camunda事件的销毁：1. 任务列表为空2. 通过外部接口取消
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/event/cycle_event"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /event/cycle_event, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    def cycle_event_sync(
        self, body: CycleEventSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        循环事件注册与取消
        用来支持循环事件的注册和取消通过task info存储事件列表，列表支持去重通过camunda循环事件的定义触发事件执行camunda事件的销毁：1. 任务列表为空2. 通过外部接口取消
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/event/cycle_event"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /event/cycle_event, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, CreateSuccessSchema.model_validate_json(resp)

    async def event_driven(
        self, body: EventDrivenSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        事件驱动的发布、订阅、取消
        用来支持事件驱动的发布、订阅和取消通过task info存储事件列表，列表支持去重事件发布时，通过事件列表，根据 module_name 找到对应的url, 推送给订阅者场景适用如下： 需要监听 Inventory 箱子变化，注册 container_update 事件，inventory 箱子变化后会发布事件，订阅着收到事件后，调用相关接口重新获取inventory箱子信息
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/event/event_driven"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /event/event_driven, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    def event_driven_sync(
        self, body: EventDrivenSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        事件驱动的发布、订阅、取消
        用来支持事件驱动的发布、订阅和取消通过task info存储事件列表，列表支持去重事件发布时，通过事件列表，根据 module_name 找到对应的url, 推送给订阅者场景适用如下： 需要监听 Inventory 箱子变化，注册 container_update 事件，inventory 箱子变化后会发布事件，订阅着收到事件后，调用相关接口重新获取inventory箱子信息
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/event/event_driven"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /event/event_driven, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, CreateSuccessSchema.model_validate_json(resp)

    async def abort_all_event_process(self) -> Tuple[int, CreateSuccessSchema]:
        """
        取消事件流程
        取消循环、订阅、事件驱动的camunda流程, 并清空任务列表
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/event/abort_all_event_process"),
            timeout=self.timeout,
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /event/abort_all_event_process, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    def abort_all_event_process_sync(self) -> Tuple[int, CreateSuccessSchema]:
        """
        取消事件流程
        取消循环、订阅、事件驱动的camunda流程, 并清空任务列表
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/event/abort_all_event_process"),
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /event/abort_all_event_process, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, CreateSuccessSchema.model_validate_json(resp)


TaskExecutorRequest = TaskExecutorRequestCls()
