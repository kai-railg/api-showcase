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

from ..schemas.task_scheduler import *

FMS_IP_ADDRESS = f"http://{os.environ.get('FMS_IP_ADDRESS', '127.0.0.1')}"


class Task_SchedulerRequest(object):
    url = FMS_IP_ADDRESS + ":" + "26102"
    
    @classmethod
    async def receive_mi(cls, body: MovementInstructions) -> Tuple[int, Dict]:
        """
        Process Movement Instructions
        
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/receive_mi/"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /receive_mi/, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def remove(cls) -> Tuple[int, Dict]:
        """
        Process Remove
        
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/remove"
            ),
            
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /remove, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def dc(cls, body: DependencyCheck) -> Tuple[int, Dict]:
        """
        Process Movement Instructions
        
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/receive_mi/dc"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /receive_mi/dc, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def cancel(cls, body: MovementCancel) -> Tuple[int, Dict]:
        """
        Process Movement Cancel Instructions
        
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/receive_mi/cancel"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /receive_mi/cancel, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def receive_mi_update_post(cls, body: MovementInstructions) -> Tuple[int, Dict]:
        """
        Process Movement Instruction Update
        
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/receive_mi/update"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /receive_mi/update, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def receive_action_code(cls, body: VehicleOrder) -> Tuple[int, Dict]:
        """
        Process Code
        
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/receive_action_code"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /receive_action_code, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def order_update(cls, body: TOSOrderUpdate) -> Tuple[int, Dict]:
        """
        Process Tos Side Order Update
        
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/tos_interface/order_update"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /tos_interface/order_update, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def check_sc(cls) -> Tuple[int, Dict]:
        """
        Monitor Sc Status
        
        """
        resp = await async_get(
            url=parse.urljoin(
                cls.url, "/monitor/check_sc"
            ),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /monitor/check_sc, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def check_sc_details(cls, sc_id: str) -> Tuple[int, Dict]:
        """
        Get Sc Data Status
        
        """
        resp = await async_get(
            url=parse.urljoin(
                cls.url, "/monitor/check_sc_details/{sc_id}"
            ),
            params=dict(sc_id=sc_id)
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /monitor/check_sc_details/{sc_id}, response: {resp.text}")
        return resp.status, resp.json()
        