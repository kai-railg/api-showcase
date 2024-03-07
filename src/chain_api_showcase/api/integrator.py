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

    async def insert(self, body: object) -> Tuple[int, Dict]:
        """
        Insert
        向任务队列插入新任务
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/task/insert"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/task/insert, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def insert_sync(self, body: object) -> Tuple[int, Dict]:
        """
        Insert
        向任务队列插入新任务
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/task/insert"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/task/insert, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def clear(self, body: object) -> Tuple[int, Dict]:
        """
        Task Clear
        清空任务队列
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/task/clear"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/task/clear, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def clear_sync(self, body: object) -> Tuple[int, Dict]:
        """
        Task Clear
        清空任务队列
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/task/clear"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/task/clear, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def get_all(self, body: object) -> Tuple[int, Dict]:
        """
        Task Get All
        获取任务队列
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/task/get_all"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/task/get_all, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def get_all_sync(self, body: object) -> Tuple[int, Dict]:
        """
        Task Get All
        获取任务队列
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/task/get_all"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/task/get_all, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def rotate(self, body: object) -> Tuple[int, Dict]:
        """
        Rotate
        倒箱门
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/rotate"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/rotate, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def rotate_sync(self, body: object) -> Tuple[int, Dict]:
        """
        Rotate
        倒箱门
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/rotate"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/rotate, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def complete(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        Complete
        手动complete
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/complete"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/complete, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def complete_sync(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        Complete
        手动complete
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/complete"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/complete, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def exclusiveZone(self) -> Tuple[int, Dict]:
        """
        Rotate
        车辆是否处于reefer和TG
        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/exclusiveZone"),
            timeout=self.timeout,
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/exclusiveZone, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def exclusiveZone_sync(self) -> Tuple[int, Dict]:
        """
        Rotate
        车辆是否处于reefer和TG
        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/api/exclusiveZone"),
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/exclusiveZone, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def shuffle(self, body: object) -> Tuple[int, Dict]:
        """
        Shuffle
        处理shuffle
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/shuffle"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /shuffle, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def shuffle_sync(self, body: object) -> Tuple[int, Dict]:
        """
        Shuffle
        处理shuffle
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/shuffle"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /shuffle, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def start(self, body: object) -> Tuple[int, Dict]:
        """
        Start
        启动任务
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
        return resp.status, resp.json()

    def start_sync(self, body: object) -> Tuple[int, Dict]:
        """
        Start
        启动任务
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
        return resp.status_code, resp.json()

    async def start_teleop(self, body: object) -> Tuple[int, Dict]:
        """
        Start Teleop
        远控
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/start_teleop"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/start_teleop, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def start_teleop_sync(self, body: object) -> Tuple[int, Dict]:
        """
        Start Teleop
        远控
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/start_teleop"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/start_teleop, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def report(self, body: object) -> Tuple[int, Dict]:
        """
        Report
        上报任务状态
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/task_report/report"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/task_report/report, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def report_sync(self, body: object) -> Tuple[int, Dict]:
        """
        Report
        上报任务状态
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/task_report/report"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/task_report/report, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()


IntegratorRequest = IntegratorRequestCls()
