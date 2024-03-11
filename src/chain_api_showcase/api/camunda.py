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
from ..schemas.camunda import *

__all__ = ["CamundaRequest"]


class CamundaRequestCls(ApiRequestBaseCls):
    def __init__(self):
        super(CamundaRequestCls, self).__init__()
        self.SERVICE_PORT = 8099
        self.SERVICE_NAME = "camunda"
        self.module_mapping[self.SERVICE_NAME] = self

    async def startProcess(self, body: StartProcessRequest) -> Tuple[int, Dict]:
        """
        None
        发起流程
        """
        return await self.request(
            request=async_post,
            api="/api/camundaProcess/startProcess",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def startProcess_sync(self, body: StartProcessRequest) -> Tuple[int, Dict]:
        """
        None
        发起流程
        """
        return self.request_sync(
            request=requests.post,
            api="/api/camundaProcess/startProcess",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    async def setVariablesByBisKey(self, body: VariableRequest) -> Tuple[int, Dict]:
        """
        None
        根据业务主键设置流程变量
        """
        return await self.request(
            request=async_post,
            api="/api/camundaProcess/setVariablesByBisKey",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def setVariablesByBisKey_sync(self, body: VariableRequest) -> Tuple[int, Dict]:
        """
        None
        根据业务主键设置流程变量
        """
        return self.request_sync(
            request=requests.post,
            api="/api/camundaProcess/setVariablesByBisKey",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    async def searchCurrentActiveMessageEvents(
        self, body: ActInfoRequest
    ) -> Tuple[int, Dict]:
        """
        None
        获取当前活动receiveEvents
        """
        return await self.request(
            request=async_post,
            api="/api/camundaProcess/searchCurrentActiveMessageEvents",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def searchCurrentActiveMessageEvents_sync(
        self, body: ActInfoRequest
    ) -> Tuple[int, Dict]:
        """
        None
        获取当前活动receiveEvents
        """
        return self.request_sync(
            request=requests.post,
            api="/api/camundaProcess/searchCurrentActiveMessageEvents",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    async def searchCurrentActInfo(self, body: ActInfoRequest) -> Tuple[int, Dict]:
        """
        None
        获取当前流程节点定义
        """
        return await self.request(
            request=async_post,
            api="/api/camundaProcess/searchCurrentActInfo",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def searchCurrentActInfo_sync(self, body: ActInfoRequest) -> Tuple[int, Dict]:
        """
        None
        获取当前流程节点定义
        """
        return self.request_sync(
            request=requests.post,
            api="/api/camundaProcess/searchCurrentActInfo",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    async def receivedTaskMessageEvent(
        self, body: ReceivedTaskRequest
    ) -> Tuple[int, Dict]:
        """
        None
        推动receiveTask
        """
        return await self.request(
            request=async_post,
            api="/api/camundaProcess/receivedTaskMessageEvent",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def receivedTaskMessageEvent_sync(
        self, body: ReceivedTaskRequest
    ) -> Tuple[int, Dict]:
        """
        None
        推动receiveTask
        """
        return self.request_sync(
            request=requests.post,
            api="/api/camundaProcess/receivedTaskMessageEvent",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    async def receivedMessageEvent(
        self, body: ReceivedMessageEvent
    ) -> Tuple[int, Dict]:
        """
        None
        信封事件驱动
        """
        return await self.request(
            request=async_post,
            api="/api/camundaProcess/receivedMessageEvent",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def receivedMessageEvent_sync(self, body: ReceivedMessageEvent) -> Tuple[int, Dict]:
        """
        None
        信封事件驱动
        """
        return self.request_sync(
            request=requests.post,
            api="/api/camundaProcess/receivedMessageEvent",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    async def receivedCommon(self, body: ReceivedCommonRequest) -> Tuple[int, Dict]:
        """
        None
        接口驱动receiveTask流程继续
        """
        return await self.request(
            request=async_post,
            api="/api/camundaProcess/receivedCommon",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def receivedCommon_sync(self, body: ReceivedCommonRequest) -> Tuple[int, Dict]:
        """
        None
        接口驱动receiveTask流程继续
        """
        return self.request_sync(
            request=requests.post,
            api="/api/camundaProcess/receivedCommon",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    async def completeUserTask(self, body: ReceivedCommonRequest) -> Tuple[int, Dict]:
        """
        None
        驱动userTask
        """
        return await self.request(
            request=async_post,
            api="/api/camundaProcess/completeUserTask",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def completeUserTask_sync(self, body: ReceivedCommonRequest) -> Tuple[int, Dict]:
        """
        None
        驱动userTask
        """
        return self.request_sync(
            request=requests.post,
            api="/api/camundaProcess/completeUserTask",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    async def cancelProcess(self, body: CancelProcessRequest) -> Tuple[int, Dict]:
        """
        None
        取消流程
        """
        return await self.request(
            request=async_post,
            api="/api/camundaProcess/cancelProcess",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def cancelProcess_sync(self, body: CancelProcessRequest) -> Tuple[int, Dict]:
        """
        None
        取消流程
        """
        return self.request_sync(
            request=requests.post,
            api="/api/camundaProcess/cancelProcess",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )


CamundaRequest = CamundaRequestCls()
