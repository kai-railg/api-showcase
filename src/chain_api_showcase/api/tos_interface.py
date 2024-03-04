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

from ..schemas.tos_interface import *

FMS_IP_ADDRESS = f"http://{os.environ.get('FMS_IP_ADDRESS', '127.0.0.1')}"


class Tos_InterfaceRequest(object):
    url = FMS_IP_ADDRESS + ":" + "18998"
    
    @classmethod
    async def fms_area_inventory_query_post(cls, body: AreaInventoryQuery) -> AsyncHttpResponse:
        """
        Area Inventory Query
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/fms/area/inventory/query/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def response(cls, body: WaCreatedResponse) -> AsyncHttpResponse:
        """
        Wa Created Response
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/fms/wacreated/response/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def fms_wacancelled_response_post(cls, body: WaCancelledResponse) -> AsyncHttpResponse:
        """
        Wa Cancelled Response
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/fms/wacancelled/response/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def fms_sc_status_post(cls, body: ScStatus) -> AsyncHttpResponse:
        """
        Sc Status
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/fms/sc/status/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def updated(cls, body: AreaAvailabilityUpdated) -> AsyncHttpResponse:
        """
        Area Availability Updated
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/fms/area/availability/updated/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def fms_container_change_post(cls, body: ContainerUpdate) -> AsyncHttpResponse:
        """
        Container Change
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/fms/container/change/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def message(cls, body: object) -> AsyncHttpResponse:
        """
        Ail Message
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/ail/message/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def inventory_import_degree(cls, body: InventoryImportDegree) -> AsyncHttpResponse:
        """
        Inventory Import Degree
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/upload/inventory_import_degree/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def login(cls, body: Login) -> AsyncHttpResponse:
        """
        Login
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/upload/new/login/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def send(cls, body: ButtonSend) -> AsyncHttpResponse:
        """
        New Button Send
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/upload/new/button/send/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def refresh(cls, ) -> AsyncHttpResponse:
        """
        New Button Refresh
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/upload/new/button/refresh/"
            ),
            
        )
         
    @classmethod
    async def finish_workinstruction_csv(cls, ) -> AsyncHttpResponse:
        """
        Finish Workinstruction
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/inventory_data/finish_workinstruction.csv"
            ),
            
        )
         
    @classmethod
    async def init_yard_csv(cls, ) -> AsyncHttpResponse:
        """
        Init Yard
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/inventory_data/init_yard.csv"
            ),
            
        )
         