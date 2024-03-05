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

from ..schemas.camunda import *

FMS_IP_ADDRESS = f"http://{os.environ.get('FMS_IP_ADDRESS', '127.0.0.1')}"


class CamundaRequest(object):
    url = FMS_IP_ADDRESS + ":" + "8099"
    
    @classmethod
    async def startProcess(cls, body: StartProcessRequest) -> Tuple[int, Dict]:
        """
        None
        发起流程
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/camundaProcess/startProcess"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/camundaProcess/startProcess, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def setVariablesByBisKey(cls, body: VariableRequest) -> Tuple[int, Dict]:
        """
        None
        根据业务主键设置流程变量
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/camundaProcess/setVariablesByBisKey"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/camundaProcess/setVariablesByBisKey, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def searchCurrentActiveMessageEvents(cls, body: ActInfoRequest) -> Tuple[int, Dict]:
        """
        None
        获取当前活动receiveEvents
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/camundaProcess/searchCurrentActiveMessageEvents"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/camundaProcess/searchCurrentActiveMessageEvents, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def searchCurrentActInfo(cls, body: ActInfoRequest) -> Tuple[int, Dict]:
        """
        None
        获取当前流程节点定义
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/camundaProcess/searchCurrentActInfo"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/camundaProcess/searchCurrentActInfo, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def receivedTaskMessageEvent(cls, body: ReceivedTaskRequest) -> Tuple[int, Dict]:
        """
        None
        推动receiveTask
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/camundaProcess/receivedTaskMessageEvent"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/camundaProcess/receivedTaskMessageEvent, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def receivedMessageEvent(cls, body: ReceivedMessageEvent) -> Tuple[int, Dict]:
        """
        None
        信封事件驱动
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/camundaProcess/receivedMessageEvent"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/camundaProcess/receivedMessageEvent, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def receivedCommon(cls, body: ReceivedCommonRequest) -> Tuple[int, Dict]:
        """
        None
        接口驱动receiveTask流程继续
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/camundaProcess/receivedCommon"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/camundaProcess/receivedCommon, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def completeUserTask(cls, body: ReceivedCommonRequest) -> Tuple[int, Dict]:
        """
        None
        驱动userTask
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/camundaProcess/completeUserTask"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/camundaProcess/completeUserTask, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def cancelProcess(cls, body: CancelProcessRequest) -> Tuple[int, Dict]:
        """
        None
        取消流程
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/camundaProcess/cancelProcess"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/camundaProcess/cancelProcess, response: {resp.text}")
        return resp.status, resp.json()
        