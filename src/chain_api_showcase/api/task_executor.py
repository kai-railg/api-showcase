# -*- coding: utf-8 -*-

import os
from typing import Union, Tuple, Dict
from urllib import parse

from pydantic import BaseModel
from chain_http.async_client import (
    get as async_get,
    post as async_post,
    AsyncHttpResponse,
)

from ..schemas.task_executor import *

FMS_IP_ADDRESS = f"http://{os.environ.get('FMS_IP_ADDRESS', '127.0.0.1')}"


class Task_ExecutorRequest(object):
    url = FMS_IP_ADDRESS + ":" + "8100"

    @classmethod
    async def message_event_start_post(
        cls, body: VehicleOrderSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Start Process
        流程启动
        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/message_event/start"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /message_event/start, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def abort(
        cls, vehicle_id: str, cancel_reason: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Abort Process
        中止流程
        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/message_event/abort"),
            params=dict(vehicle_id=vehicle_id, cancel_reason=cancel_reason),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /message_event/abort, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def rch(cls, body: RchSchema) -> Tuple[int, CreateSuccessSchema]:
        """
        Rch

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/message_event/rch"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /message_event/rch, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def update_qc_task(
        cls, body: UpdateQcTaskSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Update Task

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/message_event/update_qc_task"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /message_event/update_qc_task, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def event(
        cls, body: EventListenerInSchema, event_type: ReceiveTaskType
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Event Listener

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/message_event/event"),
            json=body.dict(),
            params=dict(event_type=event_type),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /message_event/event, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def cancel_camunda_process(
        cls, body: CancelCamundaSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Cancel Camunda Process

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/message_event/cancel_camunda_process"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /message_event/cancel_camunda_process, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def boundary_event(cls, body: BoundaryEventSchema) -> Tuple[int, Dict]:
        """
        Boundary Event
        触发流程图中的 MESSAGE BOUNDARY EVENT 节点
        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/message_event/boundary_event"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /message_event/boundary_event, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def skip(
        cls, vehicle_id: str, target_node: str, current_task_id: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        节点跳跃

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/process_instance/skip"),
            params=dict(
                vehicle_id=vehicle_id,
                target_node=target_node,
                current_task_id=current_task_id,
            ),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /process_instance/skip, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def activity(cls, vehicle_id: str) -> Tuple[int, GetActivityNode]:
        """
        获取当前节点Name

        """
        resp = await async_get(
            url=parse.urljoin(cls.url, "/process_instance/activity"),
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /process_instance/activity, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, GetActivityNode.model_validate_json(resp)

    @classmethod
    async def service_task(
        cls, body: ServiceTaskInSchema
    ) -> Tuple[int, ServiceTaskOutSchema]:
        """ """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/service_task"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /service_task, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, ServiceTaskOutSchema.model_validate_json(resp)

    @classmethod
    async def cycle_event(
        cls, body: CycleEventSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Event Process
        循环事件注册与取消
        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/event/cycle_event"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /event/cycle_event, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def subscribe_event(
        cls, body: SubscribeEventSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Subscribe Event
        订阅事件的注册与取消
        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/event/subscribe_event"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /event/subscribe_event, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def abort_all_event_process(cls) -> Tuple[int, CreateSuccessSchema]:
        """
        Abort All Event Process
        取消事件流程
        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/event/abort_all_event_process"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /event/abort_all_event_process, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)
