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

from ..schemas.tos_interface import *

FMS_IP_ADDRESS = f"http://{os.environ.get('FMS_IP_ADDRESS', '127.0.0.1')}"


class Tos_InterfaceRequest(object):
    url = FMS_IP_ADDRESS + ":" + "18998"

    @classmethod
    async def fms_area_inventory_query_post(
        cls, body: AreaInventoryQuery
    ) -> Tuple[int, Dict]:
        """
        Area Inventory Query

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/fms/area/inventory/query/"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /fms/area/inventory/query/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def response(cls, body: WaCreatedResponse) -> Tuple[int, Dict]:
        """
        Wa Created Response

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/fms/wacreated/response/"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /fms/wacreated/response/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def fms_wacancelled_response_post(
        cls, body: WaCancelledResponse
    ) -> Tuple[int, Dict]:
        """
        Wa Cancelled Response

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/fms/wacancelled/response/"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /fms/wacancelled/response/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def fms_sc_status_post(cls, body: ScStatus) -> Tuple[int, Dict]:
        """
        Sc Status

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/fms/sc/status/"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /fms/sc/status/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def updated(cls, body: AreaAvailabilityUpdated) -> Tuple[int, Dict]:
        """
        Area Availability Updated

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/fms/area/availability/updated/"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /fms/area/availability/updated/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def fms_container_change_post(cls, body: ContainerUpdate) -> Tuple[int, Dict]:
        """
        Container Change

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/fms/container/change/"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /fms/container/change/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def message(cls, body: object) -> Tuple[int, Dict]:
        """
        Ail Message

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/ail/message/"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /ail/message/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def inventory_import_degree(
        cls, body: InventoryImportDegree
    ) -> Tuple[int, Dict]:
        """
        Inventory Import Degree

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/upload/inventory_import_degree/"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /upload/inventory_import_degree/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def login(cls, body: Login) -> Tuple[int, Dict]:
        """
        Login

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/upload/new/login/"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /upload/new/login/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def send(cls, body: ButtonSend) -> Tuple[int, Dict]:
        """
        New Button Send

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/upload/new/button/send/"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /upload/new/button/send/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def refresh(cls) -> Tuple[int, Dict]:
        """
        New Button Refresh

        """
        resp = await async_get(
            url=parse.urljoin(cls.url, "/upload/new/button/refresh/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /upload/new/button/refresh/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def finish_workinstruction_csv(cls) -> Tuple[int, Dict]:
        """
        Finish Workinstruction

        """
        resp = await async_get(
            url=parse.urljoin(cls.url, "/inventory_data/finish_workinstruction.csv"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /inventory_data/finish_workinstruction.csv, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def init_yard_csv(cls) -> Tuple[int, Dict]:
        """
        Init Yard

        """
        resp = await async_get(
            url=parse.urljoin(cls.url, "/inventory_data/init_yard.csv"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /inventory_data/init_yard.csv, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()
