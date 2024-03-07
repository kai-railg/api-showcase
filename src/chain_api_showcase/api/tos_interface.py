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
        resp = await async_post(
            url=parse.urljoin(self.url, "/fms/area/inventory/query/"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /fms/area/inventory/query/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def fms_area_inventory_query_post_sync(
        self, body: AreaInventoryQuery
    ) -> Tuple[int, Dict]:
        """
        Area Inventory Query

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/fms/area/inventory/query/"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /fms/area/inventory/query/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def response(self, body: WaCreatedResponse) -> Tuple[int, Dict]:
        """
        Wa Created Response

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/fms/wacreated/response/"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /fms/wacreated/response/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def response_sync(self, body: WaCreatedResponse) -> Tuple[int, Dict]:
        """
        Wa Created Response

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/fms/wacreated/response/"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /fms/wacreated/response/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def fms_wacancelled_response_post(
        self, body: WaCancelledResponse
    ) -> Tuple[int, Dict]:
        """
        Wa Cancelled Response

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/fms/wacancelled/response/"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /fms/wacancelled/response/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def fms_wacancelled_response_post_sync(
        self, body: WaCancelledResponse
    ) -> Tuple[int, Dict]:
        """
        Wa Cancelled Response

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/fms/wacancelled/response/"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /fms/wacancelled/response/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def fms_sc_status_post(self, body: ScStatus) -> Tuple[int, Dict]:
        """
        Sc Status

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/fms/sc/status/"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /fms/sc/status/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def fms_sc_status_post_sync(self, body: ScStatus) -> Tuple[int, Dict]:
        """
        Sc Status

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/fms/sc/status/"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /fms/sc/status/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def updated(self, body: AreaAvailabilityUpdated) -> Tuple[int, Dict]:
        """
        Area Availability Updated

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/fms/area/availability/updated/"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /fms/area/availability/updated/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def updated_sync(self, body: AreaAvailabilityUpdated) -> Tuple[int, Dict]:
        """
        Area Availability Updated

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/fms/area/availability/updated/"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /fms/area/availability/updated/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def fms_container_change_post(
        self, body: ContainerUpdate
    ) -> Tuple[int, Dict]:
        """
        Container Change

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/fms/container/change/"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /fms/container/change/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def fms_container_change_post_sync(self, body: ContainerUpdate) -> Tuple[int, Dict]:
        """
        Container Change

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/fms/container/change/"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /fms/container/change/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def message(self, body: object) -> Tuple[int, Dict]:
        """
        Ail Message

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/ail/message/"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /ail/message/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def message_sync(self, body: object) -> Tuple[int, Dict]:
        """
        Ail Message

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/ail/message/"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /ail/message/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def inventory_import_degree(
        self, body: InventoryImportDegree
    ) -> Tuple[int, Dict]:
        """
        Inventory Import Degree

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/upload/inventory_import_degree/"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /upload/inventory_import_degree/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def inventory_import_degree_sync(
        self, body: InventoryImportDegree
    ) -> Tuple[int, Dict]:
        """
        Inventory Import Degree

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/upload/inventory_import_degree/"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /upload/inventory_import_degree/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def login(self, body: Login) -> Tuple[int, Dict]:
        """
        Login

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/upload/new/login/"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /upload/new/login/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def login_sync(self, body: Login) -> Tuple[int, Dict]:
        """
        Login

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/upload/new/login/"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /upload/new/login/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def send(self, body: ButtonSend) -> Tuple[int, Dict]:
        """
        New Button Send

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/upload/new/button/send/"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /upload/new/button/send/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def send_sync(self, body: ButtonSend) -> Tuple[int, Dict]:
        """
        New Button Send

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/upload/new/button/send/"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /upload/new/button/send/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def refresh(self) -> Tuple[int, Dict]:
        """
        New Button Refresh

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/upload/new/button/refresh/"),
            timeout=self.timeout,
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /upload/new/button/refresh/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def refresh_sync(self) -> Tuple[int, Dict]:
        """
        New Button Refresh

        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/upload/new/button/refresh/"),
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /upload/new/button/refresh/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def finish_workinstruction_csv(self) -> Tuple[int, Dict]:
        """
        Finish Workinstruction

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/inventory_data/finish_workinstruction.csv"),
            timeout=self.timeout,
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /inventory_data/finish_workinstruction.csv, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def finish_workinstruction_csv_sync(self) -> Tuple[int, Dict]:
        """
        Finish Workinstruction

        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/inventory_data/finish_workinstruction.csv"),
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /inventory_data/finish_workinstruction.csv, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def init_yard_csv(self) -> Tuple[int, Dict]:
        """
        Init Yard

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/inventory_data/init_yard.csv"),
            timeout=self.timeout,
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /inventory_data/init_yard.csv, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def init_yard_csv_sync(self) -> Tuple[int, Dict]:
        """
        Init Yard

        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/inventory_data/init_yard.csv"),
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /inventory_data/init_yard.csv, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()


TosInterfaceRequest = TosInterfaceRequestCls()
