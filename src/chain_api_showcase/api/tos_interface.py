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
from ..schemas.tos_interface import *

__all__ = ["TosInterfaceRequest"]


class TosInterfaceRequestCls(ApiRequestBaseCls):
    def __init__(self):
        super(TosInterfaceRequestCls, self).__init__()
        self.SERVICE_PORT = 18998
        self.SERVICE_NAME = "tos_interface"
        self.module_mapping[self.SERVICE_NAME] = self

    async def fms_area_inventory_query_post(
        self, body: AreaInventoryQuery
    ) -> Tuple[int, Dict]:
        """
        Area Inventory Query

        """
        return await self.request(
            request=async_post,
            api="/fms/area/inventory/query/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def fms_area_inventory_query_post_sync(
        self, body: AreaInventoryQuery
    ) -> Tuple[int, Dict]:
        """
        Area Inventory Query

        """
        return self.request_sync(
            request=requests.post,
            api="/fms/area/inventory/query/",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def response(self, body: WaCreatedResponse) -> Tuple[int, Dict]:
        """
        Wa Created Response

        """
        return await self.request(
            request=async_post,
            api="/fms/wacreated/response/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def response_sync(self, body: WaCreatedResponse) -> Tuple[int, Dict]:
        """
        Wa Created Response

        """
        return self.request_sync(
            request=requests.post,
            api="/fms/wacreated/response/",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def fms_wacancelled_response_post(
        self, body: WaCancelledResponse
    ) -> Tuple[int, Dict]:
        """
        Wa Cancelled Response

        """
        return await self.request(
            request=async_post,
            api="/fms/wacancelled/response/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def fms_wacancelled_response_post_sync(
        self, body: WaCancelledResponse
    ) -> Tuple[int, Dict]:
        """
        Wa Cancelled Response

        """
        return self.request_sync(
            request=requests.post,
            api="/fms/wacancelled/response/",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def fms_sc_status_post(self, body: ScStatus) -> Tuple[int, Dict]:
        """
        Sc Status

        """
        return await self.request(
            request=async_post,
            api="/fms/sc/status/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def fms_sc_status_post_sync(self, body: ScStatus) -> Tuple[int, Dict]:
        """
        Sc Status

        """
        return self.request_sync(
            request=requests.post,
            api="/fms/sc/status/",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def updated(self, body: AreaAvailabilityUpdated) -> Tuple[int, Dict]:
        """
        Area Availability Updated

        """
        return await self.request(
            request=async_post,
            api="/fms/area/availability/updated/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def updated_sync(self, body: AreaAvailabilityUpdated) -> Tuple[int, Dict]:
        """
        Area Availability Updated

        """
        return self.request_sync(
            request=requests.post,
            api="/fms/area/availability/updated/",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def fms_container_change_post(
        self, body: ContainerUpdate
    ) -> Tuple[int, Dict]:
        """
        Container Change

        """
        return await self.request(
            request=async_post,
            api="/fms/container/change/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def fms_container_change_post_sync(self, body: ContainerUpdate) -> Tuple[int, Dict]:
        """
        Container Change

        """
        return self.request_sync(
            request=requests.post,
            api="/fms/container/change/",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def message(self, body: object) -> Tuple[int, Dict]:
        """
        Ail Message

        """
        return await self.request(
            request=async_post,
            api="/ail/message/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def message_sync(self, body: object) -> Tuple[int, Dict]:
        """
        Ail Message

        """
        return self.request_sync(
            request=requests.post,
            api="/ail/message/",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def inventory_import_degree(
        self, body: InventoryImportDegree
    ) -> Tuple[int, Dict]:
        """
        Inventory Import Degree

        """
        return await self.request(
            request=async_post,
            api="/upload/inventory_import_degree/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def inventory_import_degree_sync(
        self, body: InventoryImportDegree
    ) -> Tuple[int, Dict]:
        """
        Inventory Import Degree

        """
        return self.request_sync(
            request=requests.post,
            api="/upload/inventory_import_degree/",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def login(self, body: Login) -> Tuple[int, Dict]:
        """
        Login

        """
        return await self.request(
            request=async_post,
            api="/upload/new/login/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def login_sync(self, body: Login) -> Tuple[int, Dict]:
        """
        Login

        """
        return self.request_sync(
            request=requests.post,
            api="/upload/new/login/",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def send(self, body: ButtonSend) -> Tuple[int, Dict]:
        """
        New Button Send

        """
        return await self.request(
            request=async_post,
            api="/upload/new/button/send/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def send_sync(self, body: ButtonSend) -> Tuple[int, Dict]:
        """
        New Button Send

        """
        return self.request_sync(
            request=requests.post,
            api="/upload/new/button/send/",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def refresh(self) -> Tuple[int, Dict]:
        """
        New Button Refresh

        """
        return await self.request(
            request=async_get,
            api="/upload/new/button/refresh/",
            body={},
            resp_model=None,
        )

    def refresh_sync(self) -> Tuple[int, Dict]:
        """
        New Button Refresh

        """
        return self.request_sync(
            request=requests.get,
            api="/upload/new/button/refresh/",
            body={},
            resp_model=None,
        )

    async def finish_workinstruction_csv(self) -> Tuple[int, Dict]:
        """
        Finish Workinstruction

        """
        return await self.request(
            request=async_get,
            api="/inventory_data/finish_workinstruction.csv",
            body={},
            resp_model=None,
        )

    def finish_workinstruction_csv_sync(self) -> Tuple[int, Dict]:
        """
        Finish Workinstruction

        """
        return self.request_sync(
            request=requests.get,
            api="/inventory_data/finish_workinstruction.csv",
            body={},
            resp_model=None,
        )

    async def init_yard_csv(self) -> Tuple[int, Dict]:
        """
        Init Yard

        """
        return await self.request(
            request=async_get,
            api="/inventory_data/init_yard.csv",
            body={},
            resp_model=None,
        )

    def init_yard_csv_sync(self) -> Tuple[int, Dict]:
        """
        Init Yard

        """
        return self.request_sync(
            request=requests.get,
            api="/inventory_data/init_yard.csv",
            body={},
            resp_model=None,
        )


TosInterfaceRequest = TosInterfaceRequestCls()
