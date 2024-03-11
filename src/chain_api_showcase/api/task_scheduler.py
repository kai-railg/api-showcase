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
from ..schemas.task_scheduler import *

__all__ = ["TaskSchedulerRequest"]


class TaskSchedulerRequestCls(ApiRequestBaseCls):
    def __init__(self):
        super(TaskSchedulerRequestCls, self).__init__()
        self.SERVICE_PORT = 26102
        self.SERVICE_NAME = "task_scheduler"
        self.module_mapping[self.SERVICE_NAME] = self

    async def receive_mi(
        self, body: MovementInstructions
    ) -> Tuple[int, MovementCreatedResponse]:
        """
        Process Movement Instructions

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/receive_mi/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /receive_mi/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, MovementCreatedResponse.model_validate_json(resp)

    def receive_mi_sync(
        self, body: MovementInstructions
    ) -> Tuple[int, MovementCreatedResponse]:
        """
        Process Movement Instructions

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/receive_mi/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /receive_mi/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, MovementCreatedResponse.model_validate_json(resp)

    async def remove(self) -> Tuple[int, Dict]:
        """
        Process Remove

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/remove"),
            timeout=self.timeout,
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /remove, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def remove_sync(self) -> Tuple[int, Dict]:
        """
        Process Remove

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/remove"),
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /remove, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def dc(self, body: DependencyCheck) -> Tuple[int, DependencyCheckResponse]:
        """
        Process Movement Instructions

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/receive_mi/dc"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /receive_mi/dc, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, DependencyCheckResponse.model_validate_json(resp)

    def dc_sync(self, body: DependencyCheck) -> Tuple[int, DependencyCheckResponse]:
        """
        Process Movement Instructions

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/receive_mi/dc"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /receive_mi/dc, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, DependencyCheckResponse.model_validate_json(resp)

    async def cancel(self, body: MovementCancel) -> Tuple[int, MovementCancelResponse]:
        """
        Process Movement Cancel Instructions

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/receive_mi/cancel"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /receive_mi/cancel, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, MovementCancelResponse.model_validate_json(resp)

    def cancel_sync(self, body: MovementCancel) -> Tuple[int, MovementCancelResponse]:
        """
        Process Movement Cancel Instructions

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/receive_mi/cancel"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /receive_mi/cancel, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, MovementCancelResponse.model_validate_json(resp)

    async def receive_mi_update_post(
        self, body: MovementInstructions
    ) -> Tuple[int, MovementUpdateResponse]:
        """
        Process Movement Instruction Update

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/receive_mi/update"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /receive_mi/update, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, MovementUpdateResponse.model_validate_json(resp)

    def receive_mi_update_post_sync(
        self, body: MovementInstructions
    ) -> Tuple[int, MovementUpdateResponse]:
        """
        Process Movement Instruction Update

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/receive_mi/update"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /receive_mi/update, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, MovementUpdateResponse.model_validate_json(resp)

    async def receive_action_code(
        self, body: VehicleOrder
    ) -> Tuple[int, ActionCodeResponse]:
        """
        Process Code

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/receive_action_code"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /receive_action_code, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, ActionCodeResponse.model_validate_json(resp)

    def receive_action_code_sync(
        self, body: VehicleOrder
    ) -> Tuple[int, ActionCodeResponse]:
        """
        Process Code

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/receive_action_code"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /receive_action_code, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, ActionCodeResponse.model_validate_json(resp)

    async def order_update(self, body: TOSOrderUpdate) -> Tuple[int, Dict]:
        """
        Process Tos Side Order Update

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/tos_interface/order_update"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /tos_interface/order_update, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def order_update_sync(self, body: TOSOrderUpdate) -> Tuple[int, Dict]:
        """
        Process Tos Side Order Update

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/tos_interface/order_update"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /tos_interface/order_update, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def check_sc(self) -> Tuple[int, Dict]:
        """
        Monitor Sc Status

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/monitor/check_sc"),
            timeout=self.timeout,
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /monitor/check_sc, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def check_sc_sync(self) -> Tuple[int, Dict]:
        """
        Monitor Sc Status

        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/monitor/check_sc"),
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /monitor/check_sc, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def check_sc_details(self, sc_id: str) -> Tuple[int, Dict]:
        """
        Get Sc Data Status

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/monitor/check_sc_details/{sc_id}"),
            timeout=self.timeout,
            params=dict(sc_id=sc_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /monitor/check_sc_details/{sc_id}, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def check_sc_details_sync(self, sc_id: str) -> Tuple[int, Dict]:
        """
        Get Sc Data Status

        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/monitor/check_sc_details/{sc_id}"),
            timeout=self.timeout,
            params=dict(sc_id=sc_id),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /monitor/check_sc_details/{sc_id}, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()


TaskSchedulerRequest = TaskSchedulerRequestCls()
