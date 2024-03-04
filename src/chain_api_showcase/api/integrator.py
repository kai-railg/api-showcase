# -*- coding: utf-8 -*-

import os
from typing import Union
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
    async def insert(cls, body: object) -> AsyncHttpResponse:
        """
        Insert
        向任务队列插入新任务
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/task/insert"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def clear(cls, body: object) -> AsyncHttpResponse:
        """
        Task Clear
        清空任务队列
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/task/clear"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def get_all(cls, body: object) -> AsyncHttpResponse:
        """
        Task Get All
        获取任务队列
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/task/get_all"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def rotate(cls, body: object) -> AsyncHttpResponse:
        """
        Rotate
        倒箱门
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/rotate"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def shuffle(cls, body: object) -> AsyncHttpResponse:
        """
        Shuffle
        处理shuffle
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/shuffle"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def start(cls, body: object) -> AsyncHttpResponse:
        """
        Start
        启动任务
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/message_event/start"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def start_teleop(cls, body: object) -> AsyncHttpResponse:
        """
        Start Teleop
        远控
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/start_teleop"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def report(cls, body: object) -> AsyncHttpResponse:
        """
        Report
        上报任务状态
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/task_report/report"
            ),
            json=body.dict(),
            
        )
         