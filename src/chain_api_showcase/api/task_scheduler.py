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
        return await self.request(
            request=async_post,
            api="/receive_mi/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=MovementCreatedResponse,
        )

    def receive_mi_sync(
        self, body: MovementInstructions
    ) -> Tuple[int, MovementCreatedResponse]:
        """
        Process Movement Instructions

        """
        return self.request_sync(
            request=requests.post,
            api="/receive_mi/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=MovementCreatedResponse,
        )

    async def remove(self) -> Tuple[int, Dict]:
        """
        Process Remove

        """
        return await self.request(
            request=async_post, api="/remove", body={}, resp_model=None
        )

    def remove_sync(self) -> Tuple[int, Dict]:
        """
        Process Remove

        """
        return self.request_sync(
            request=requests.post, api="/remove", body={}, resp_model=None
        )

    async def dc(self, body: DependencyCheck) -> Tuple[int, DependencyCheckResponse]:
        """
        Process Movement Instructions

        """
        return await self.request(
            request=async_post,
            api="/receive_mi/dc",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=DependencyCheckResponse,
        )

    def dc_sync(self, body: DependencyCheck) -> Tuple[int, DependencyCheckResponse]:
        """
        Process Movement Instructions

        """
        return self.request_sync(
            request=requests.post,
            api="/receive_mi/dc",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=DependencyCheckResponse,
        )

    async def cancel(self, body: MovementCancel) -> Tuple[int, MovementCancelResponse]:
        """
        Process Movement Cancel Instructions

        """
        return await self.request(
            request=async_post,
            api="/receive_mi/cancel",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=MovementCancelResponse,
        )

    def cancel_sync(self, body: MovementCancel) -> Tuple[int, MovementCancelResponse]:
        """
        Process Movement Cancel Instructions

        """
        return self.request_sync(
            request=requests.post,
            api="/receive_mi/cancel",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=MovementCancelResponse,
        )

    async def receive_mi_update_post(
        self, body: MovementInstructions
    ) -> Tuple[int, MovementUpdateResponse]:
        """
        Process Movement Instruction Update

        """
        return await self.request(
            request=async_post,
            api="/receive_mi/update",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=MovementUpdateResponse,
        )

    def receive_mi_update_post_sync(
        self, body: MovementInstructions
    ) -> Tuple[int, MovementUpdateResponse]:
        """
        Process Movement Instruction Update

        """
        return self.request_sync(
            request=requests.post,
            api="/receive_mi/update",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=MovementUpdateResponse,
        )

    async def receive_action_code(
        self, body: VehicleOrder
    ) -> Tuple[int, ActionCodeResponse]:
        """
        Process Code

        """
        return await self.request(
            request=async_post,
            api="/receive_action_code",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=ActionCodeResponse,
        )

    def receive_action_code_sync(
        self, body: VehicleOrder
    ) -> Tuple[int, ActionCodeResponse]:
        """
        Process Code

        """
        return self.request_sync(
            request=requests.post,
            api="/receive_action_code",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=ActionCodeResponse,
        )

    async def order_update(self, body: TOSOrderUpdate) -> Tuple[int, Dict]:
        """
        Process Tos Side Order Update

        """
        return await self.request(
            request=async_post,
            api="/tos_interface/order_update",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def order_update_sync(self, body: TOSOrderUpdate) -> Tuple[int, Dict]:
        """
        Process Tos Side Order Update

        """
        return self.request_sync(
            request=requests.post,
            api="/tos_interface/order_update",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    async def check_sc(self) -> Tuple[int, Dict]:
        """
        Monitor Sc Status

        """
        return await self.request(
            request=async_get, api="/monitor/check_sc", body={}, resp_model=None
        )

    def check_sc_sync(self) -> Tuple[int, Dict]:
        """
        Monitor Sc Status

        """
        return self.request_sync(
            request=requests.get, api="/monitor/check_sc", body={}, resp_model=None
        )

    async def check_sc_details(self, sc_id: str) -> Tuple[int, Dict]:
        """
        Get Sc Data Status

        """
        return await self.request(
            request=async_get,
            api="/monitor/check_sc_details/{sc_id}",
            body={"params": dict(sc_id=sc_id)},
            resp_model=None,
        )

    def check_sc_details_sync(self, sc_id: str) -> Tuple[int, Dict]:
        """
        Get Sc Data Status

        """
        return self.request_sync(
            request=requests.get,
            api="/monitor/check_sc_details/{sc_id}",
            body={"params": dict(sc_id=sc_id)},
            resp_model=None,
        )


TaskSchedulerRequest = TaskSchedulerRequestCls()
