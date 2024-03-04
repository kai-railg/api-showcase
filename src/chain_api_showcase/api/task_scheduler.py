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

from ..schemas.task_scheduler import *

FMS_IP_ADDRESS = f"http://{os.environ.get('FMS_IP_ADDRESS', '127.0.0.1')}"


class Task_SchedulerRequest(object):
    url = FMS_IP_ADDRESS + ":" + "26102"
    
    @classmethod
    async def receive_mi(cls, body: MovementInstructions) -> AsyncHttpResponse:
        """
        Process Movement Instructions
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/receive_mi/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def remove(cls, ) -> AsyncHttpResponse:
        """
        Process Remove
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/remove"
            ),
            
            
        )
         
    @classmethod
    async def dc(cls, body: DependencyCheck) -> AsyncHttpResponse:
        """
        Process Movement Instructions
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/receive_mi/dc"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def cancel(cls, body: MovementCancel) -> AsyncHttpResponse:
        """
        Process Movement Cancel Instructions
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/receive_mi/cancel"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def receive_mi_update_post(cls, body: MovementInstructions) -> AsyncHttpResponse:
        """
        Process Movement Instruction Update
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/receive_mi/update"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def receive_action_code(cls, body: VehicleOrder) -> AsyncHttpResponse:
        """
        Process Code
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/receive_action_code"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def order_update(cls, body: TOSOrderUpdate) -> AsyncHttpResponse:
        """
        Process Tos Side Order Update
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/tos_interface/order_update"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def check_sc(cls, ) -> AsyncHttpResponse:
        """
        Monitor Sc Status
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/monitor/check_sc"
            ),
            
        )
         
    @classmethod
    async def check_sc_details(cls, sc_id: str) -> AsyncHttpResponse:
        """
        Get Sc Data Status
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/monitor/check_sc_details/{sc_id}"
            ),
            params=dict(sc_id=sc_id)
        )
         