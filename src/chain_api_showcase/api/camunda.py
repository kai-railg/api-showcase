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
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/camundaProcess/startProcess"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/camundaProcess/startProcess, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def startProcess_sync(self, body: StartProcessRequest) -> Tuple[int, Dict]:
        """
        None
        发起流程
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/camundaProcess/startProcess"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/camundaProcess/startProcess, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def setVariablesByBisKey(self, body: VariableRequest) -> Tuple[int, Dict]:
        """
        None
        根据业务主键设置流程变量
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/camundaProcess/setVariablesByBisKey"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/camundaProcess/setVariablesByBisKey, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def setVariablesByBisKey_sync(self, body: VariableRequest) -> Tuple[int, Dict]:
        """
        None
        根据业务主键设置流程变量
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/camundaProcess/setVariablesByBisKey"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/camundaProcess/setVariablesByBisKey, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def searchCurrentActiveMessageEvents(
        self, body: ActInfoRequest
    ) -> Tuple[int, Dict]:
        """
        None
        获取当前活动receiveEvents
        """
        resp = await async_post(
            url=parse.urljoin(
                self.url, "/api/camundaProcess/searchCurrentActiveMessageEvents"
            ),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/camundaProcess/searchCurrentActiveMessageEvents, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def searchCurrentActiveMessageEvents_sync(
        self, body: ActInfoRequest
    ) -> Tuple[int, Dict]:
        """
        None
        获取当前活动receiveEvents
        """
        resp = requests.post(
            url=parse.urljoin(
                self.url, "/api/camundaProcess/searchCurrentActiveMessageEvents"
            ),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/camundaProcess/searchCurrentActiveMessageEvents, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def searchCurrentActInfo(self, body: ActInfoRequest) -> Tuple[int, Dict]:
        """
        None
        获取当前流程节点定义
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/camundaProcess/searchCurrentActInfo"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/camundaProcess/searchCurrentActInfo, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def searchCurrentActInfo_sync(self, body: ActInfoRequest) -> Tuple[int, Dict]:
        """
        None
        获取当前流程节点定义
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/camundaProcess/searchCurrentActInfo"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/camundaProcess/searchCurrentActInfo, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def receivedTaskMessageEvent(
        self, body: ReceivedTaskRequest
    ) -> Tuple[int, Dict]:
        """
        None
        推动receiveTask
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/camundaProcess/receivedTaskMessageEvent"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/camundaProcess/receivedTaskMessageEvent, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def receivedTaskMessageEvent_sync(
        self, body: ReceivedTaskRequest
    ) -> Tuple[int, Dict]:
        """
        None
        推动receiveTask
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/camundaProcess/receivedTaskMessageEvent"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/camundaProcess/receivedTaskMessageEvent, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def receivedMessageEvent(
        self, body: ReceivedMessageEvent
    ) -> Tuple[int, Dict]:
        """
        None
        信封事件驱动
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/camundaProcess/receivedMessageEvent"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/camundaProcess/receivedMessageEvent, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def receivedMessageEvent_sync(self, body: ReceivedMessageEvent) -> Tuple[int, Dict]:
        """
        None
        信封事件驱动
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/camundaProcess/receivedMessageEvent"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/camundaProcess/receivedMessageEvent, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def receivedCommon(self, body: ReceivedCommonRequest) -> Tuple[int, Dict]:
        """
        None
        接口驱动receiveTask流程继续
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/camundaProcess/receivedCommon"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/camundaProcess/receivedCommon, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def receivedCommon_sync(self, body: ReceivedCommonRequest) -> Tuple[int, Dict]:
        """
        None
        接口驱动receiveTask流程继续
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/camundaProcess/receivedCommon"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/camundaProcess/receivedCommon, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def completeUserTask(self, body: ReceivedCommonRequest) -> Tuple[int, Dict]:
        """
        None
        驱动userTask
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/camundaProcess/completeUserTask"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/camundaProcess/completeUserTask, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def completeUserTask_sync(self, body: ReceivedCommonRequest) -> Tuple[int, Dict]:
        """
        None
        驱动userTask
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/camundaProcess/completeUserTask"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/camundaProcess/completeUserTask, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def cancelProcess(self, body: CancelProcessRequest) -> Tuple[int, Dict]:
        """
        None
        取消流程
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/camundaProcess/cancelProcess"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/camundaProcess/cancelProcess, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def cancelProcess_sync(self, body: CancelProcessRequest) -> Tuple[int, Dict]:
        """
        None
        取消流程
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/camundaProcess/cancelProcess"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/camundaProcess/cancelProcess, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()


CamundaRequest = CamundaRequestCls()
