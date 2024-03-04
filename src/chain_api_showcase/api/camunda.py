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

from ..schemas.camunda import *

FMS_IP_ADDRESS = f"http://{os.environ.get('FMS_IP_ADDRESS', '127.0.0.1')}"


class CamundaRequest(object):
    url = FMS_IP_ADDRESS + ":" + "8099"
    
    @classmethod
    async def startProcess(cls, body: StartProcessRequest) -> AsyncHttpResponse:
        """
        None
        发起流程
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/camundaProcess/startProcess"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def setVariablesByBisKey(cls, body: VariableRequest) -> AsyncHttpResponse:
        """
        None
        根据业务主键设置流程变量
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/camundaProcess/setVariablesByBisKey"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def searchCurrentActiveMessageEvents(cls, body: ActInfoRequest) -> AsyncHttpResponse:
        """
        None
        获取当前活动receiveEvents
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/camundaProcess/searchCurrentActiveMessageEvents"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def searchCurrentActInfo(cls, body: ActInfoRequest) -> AsyncHttpResponse:
        """
        None
        获取当前流程节点定义
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/camundaProcess/searchCurrentActInfo"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def receivedTaskMessageEvent(cls, body: ReceivedTaskRequest) -> AsyncHttpResponse:
        """
        None
        推动receiveTask
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/camundaProcess/receivedTaskMessageEvent"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def receivedMessageEvent(cls, body: ReceivedMessageEvent) -> AsyncHttpResponse:
        """
        None
        信封事件驱动
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/camundaProcess/receivedMessageEvent"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def receivedCommon(cls, body: ReceivedCommonRequest) -> AsyncHttpResponse:
        """
        None
        接口驱动receiveTask流程继续
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/camundaProcess/receivedCommon"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def completeUserTask(cls, body: ReceivedCommonRequest) -> AsyncHttpResponse:
        """
        None
        驱动userTask
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/camundaProcess/completeUserTask"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def cancelProcess(cls, body: CancelProcessRequest) -> AsyncHttpResponse:
        """
        None
        取消流程
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/camundaProcess/cancelProcess"
            ),
            json=body.dict(),
            
        )
         