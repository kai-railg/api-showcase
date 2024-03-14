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

    async def insert(self, body: object) -> Tuple[int, Dict]:
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
            resp_model=None,
        )

    def insert_sync(self, body: object) -> Tuple[int, Dict]:
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
            resp_model=None,
        )

    async def clear(self, body: object) -> Tuple[int, Dict]:
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
            resp_model=None,
        )

    def clear_sync(self, body: object) -> Tuple[int, Dict]:
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
            resp_model=None,
        )

    async def get_all(self, body: object) -> Tuple[int, Dict]:
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
            resp_model=None,
        )

    def get_all_sync(self, body: object) -> Tuple[int, Dict]:
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
            resp_model=None,
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
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    async def shuffle(self, body: object) -> Tuple[int, Dict]:
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
            resp_model=None,
        )

    def shuffle_sync(self, body: object) -> Tuple[int, Dict]:
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
            resp_model=None,
        )

    async def start(self, body: object) -> Tuple[int, Dict]:
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
            resp_model=None,
        )

    def start_sync(self, body: object) -> Tuple[int, Dict]:
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
            resp_model=None,
        )

    async def start_teleop(self, body: object) -> Tuple[int, Dict]:
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
            resp_model=None,
        )

    def start_teleop_sync(self, body: object) -> Tuple[int, Dict]:
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
            resp_model=None,
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
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )


IntegratorRequest = IntegratorRequestCls()
