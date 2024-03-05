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

from ..schemas.integrator import *

FMS_IP_ADDRESS = f"http://{os.environ.get('FMS_IP_ADDRESS', '127.0.0.1')}"


class IntegratorRequest(object):
    url = FMS_IP_ADDRESS + ":" + "10101"
    
    @classmethod
    async def insert(cls, body: object) -> Tuple[int, Dict]:
        """
        Insert
        向任务队列插入新任务
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/task/insert"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/task/insert, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def clear(cls, body: object) -> Tuple[int, Dict]:
        """
        Task Clear
        清空任务队列
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/task/clear"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/task/clear, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def get_all(cls, body: object) -> Tuple[int, Dict]:
        """
        Task Get All
        获取任务队列
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/task/get_all"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/task/get_all, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def rotate(cls, body: object) -> Tuple[int, Dict]:
        """
        Rotate
        倒箱门
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/rotate"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/rotate, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def shuffle(cls, body: object) -> Tuple[int, Dict]:
        """
        Shuffle
        处理shuffle
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/shuffle"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /shuffle, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def start(cls, body: object) -> Tuple[int, Dict]:
        """
        Start
        启动任务
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/message_event/start"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /message_event/start, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def start_teleop(cls, body: object) -> Tuple[int, Dict]:
        """
        Start Teleop
        远控
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/start_teleop"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/start_teleop, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def report(cls, body: object) -> Tuple[int, Dict]:
        """
        Report
        上报任务状态
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/task_report/report"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/task_report/report, response: {resp.text}")
        return resp.status, resp.json()
        