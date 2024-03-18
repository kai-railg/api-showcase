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
from ..schemas.integrator import *

__all__ = ["IntegratorRequest"]


class IntegratorRequestCls(ApiRequestBaseCls):
    def __init__(self):
        super(IntegratorRequestCls, self).__init__()
        self.SERVICE_PORT = 10101
        self.SERVICE_NAME = "integrator"
        self.module_mapping[self.SERVICE_NAME] = self

    async def insert(self, body: object) -> Tuple[int, StdRes]:
        """
        Insert
        向任务队列插入新任务
        """
        return await self.request(
            request=async_post,
            api="/api/task/insert",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=StdRes,
        )

    def insert_sync(self, body: object) -> Tuple[int, StdRes]:
        """
        Insert
        向任务队列插入新任务
        """
        return self.request_sync(
            request=requests.post,
            api="/api/task/insert",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=StdRes,
        )

    async def clear(self, body: object) -> Tuple[int, StdRes]:
        """
        Task Clear
        清空任务队列
        """
        return await self.request(
            request=async_post,
            api="/api/task/clear",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=StdRes,
        )

    def clear_sync(self, body: object) -> Tuple[int, StdRes]:
        """
        Task Clear
        清空任务队列
        """
        return self.request_sync(
            request=requests.post,
            api="/api/task/clear",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=StdRes,
        )

    async def get_all(self, body: object) -> Tuple[int, StdRes]:
        """
        Task Get All
        获取任务队列
        """
        return await self.request(
            request=async_post,
            api="/api/task/get_all",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=StdRes,
        )

    def get_all_sync(self, body: object) -> Tuple[int, StdRes]:
        """
        Task Get All
        获取任务队列
        """
        return self.request_sync(
            request=requests.post,
            api="/api/task/get_all",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=StdRes,
        )

    async def rotate(self, body: object) -> Tuple[int, Dict]:
        """
        Rotate
        倒箱门
        """
        return await self.request(
            request=async_post,
            api="/api/rotate",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def rotate_sync(self, body: object) -> Tuple[int, Dict]:
        """
        Rotate
        倒箱门
        """
        return self.request_sync(
            request=requests.post,
            api="/api/rotate",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def complete(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        Complete
        手动complete
        """
        return await self.request(
            request=async_post,
            api="/api/complete",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=None,
        )

    def complete_sync(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        Complete
        手动complete
        """
        return self.request_sync(
            request=requests.post,
            api="/api/complete",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=None,
        )

    async def exclusiveZone(self) -> Tuple[int, Dict]:
        """
        Exclusive Zone
        车辆是否处于reefer和TG
        """
        return await self.request(
            request=async_get, api="/api/exclusiveZone", body={}, resp_model=None
        )

    def exclusiveZone_sync(self) -> Tuple[int, Dict]:
        """
        Exclusive Zone
        车辆是否处于reefer和TG
        """
        return self.request_sync(
            request=requests.get, api="/api/exclusiveZone", body={}, resp_model=None
        )

    async def check_block_used(self, vehicle_id: str) -> Tuple[int, StdRes]:
        """
        Check Block Used
        查询当前车辆dest是否locked
        """
        return await self.request(
            request=async_get,
            api="/api/check_block_used",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=StdRes,
        )

    def check_block_used_sync(self, vehicle_id: str) -> Tuple[int, StdRes]:
        """
        Check Block Used
        查询当前车辆dest是否locked
        """
        return self.request_sync(
            request=requests.get,
            api="/api/check_block_used",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=StdRes,
        )

    async def lock_block(self, vehicle_id: str) -> Tuple[int, StdRes]:
        """
        Lock Block

        """
        return await self.request(
            request=async_post,
            api="/api/lock_block",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=StdRes,
        )

    def lock_block_sync(self, vehicle_id: str) -> Tuple[int, StdRes]:
        """
        Lock Block

        """
        return self.request_sync(
            request=requests.post,
            api="/api/lock_block",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=StdRes,
        )

    async def release_block(self, vehicle_id: str) -> Tuple[int, StdRes]:
        """
        Release Block

        """
        return await self.request(
            request=async_post,
            api="/api/release_block",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=StdRes,
        )

    def release_block_sync(self, vehicle_id: str) -> Tuple[int, StdRes]:
        """
        Release Block

        """
        return self.request_sync(
            request=requests.post,
            api="/api/release_block",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=StdRes,
        )

    async def select_holding(self, vehicle_id: str) -> Tuple[int, StdRes]:
        """
        Select Holding
        holding点选择
        """
        return await self.request(
            request=async_get,
            api="/api/select_holding",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=StdRes,
        )

    def select_holding_sync(self, vehicle_id: str) -> Tuple[int, StdRes]:
        """
        Select Holding
        holding点选择
        """
        return self.request_sync(
            request=requests.get,
            api="/api/select_holding",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=StdRes,
        )

    async def telep(self, body: object) -> Tuple[int, StdRes]:
        """
        Telep
        异常处理
        """
        return await self.request(
            request=async_post,
            api="/api/telep",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=StdRes,
        )

    def telep_sync(self, body: object) -> Tuple[int, StdRes]:
        """
        Telep
        异常处理
        """
        return self.request_sync(
            request=requests.post,
            api="/api/telep",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=StdRes,
        )

    async def shuffle(self, body: object) -> Tuple[int, StdRes]:
        """
        Shuffle
        处理shuffle
        """
        return await self.request(
            request=async_post,
            api="/shuffle",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=StdRes,
        )

    def shuffle_sync(self, body: object) -> Tuple[int, StdRes]:
        """
        Shuffle
        处理shuffle
        """
        return self.request_sync(
            request=requests.post,
            api="/shuffle",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=StdRes,
        )

    async def start(self, body: object) -> Tuple[int, StdRes]:
        """
        Start
        启动任务
        """
        return await self.request(
            request=async_post,
            api="/message_event/start",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=StdRes,
        )

    def start_sync(self, body: object) -> Tuple[int, StdRes]:
        """
        Start
        启动任务
        """
        return self.request_sync(
            request=requests.post,
            api="/message_event/start",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=StdRes,
        )

    async def start_teleop(self, body: object) -> Tuple[int, StdRes]:
        """
        Start Teleop
        远控
        """
        return await self.request(
            request=async_post,
            api="/api/start_teleop",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=StdRes,
        )

    def start_teleop_sync(self, body: object) -> Tuple[int, StdRes]:
        """
        Start Teleop
        远控
        """
        return self.request_sync(
            request=requests.post,
            api="/api/start_teleop",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=StdRes,
        )

    async def event_callback(self, body: EventCallback) -> Tuple[int, StdRes]:
        """
        Event Callback
        事件回调接口
        """
        return await self.request(
            request=async_post,
            api="/api/event_callback",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=StdRes,
        )

    def event_callback_sync(self, body: EventCallback) -> Tuple[int, StdRes]:
        """
        Event Callback
        事件回调接口
        """
        return self.request_sync(
            request=requests.post,
            api="/api/event_callback",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=StdRes,
        )

    async def report(self, body: object) -> Tuple[int, Dict]:
        """
        Report
        上报任务状态
        """
        return await self.request(
            request=async_post,
            api="/api/task_report/report",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def report_sync(self, body: object) -> Tuple[int, Dict]:
        """
        Report
        上报任务状态
        """
        return self.request_sync(
            request=requests.post,
            api="/api/task_report/report",
            body={
                "data": body,
            },
            resp_model=None,
        )


IntegratorRequest = IntegratorRequestCls()
