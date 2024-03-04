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

from ..schemas.task_executor import *

FMS_IP_ADDRESS = f"http://{os.environ.get('FMS_IP_ADDRESS', '127.0.0.1')}"


class Task_ExecutorRequest(object):
    url = FMS_IP_ADDRESS + ":" + "8100"
    
    @classmethod
    async def message_event_start_post(cls, body: VehicleOrderSchema) -> AsyncHttpResponse:
        """
        Start Process
        流程启动
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/message_event/start"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def abort(cls, vehicle_id: str, cancel_reason: str) -> AsyncHttpResponse:
        """
        Abort Process
        中止流程
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/message_event/abort"
            ),
            
            params=dict(vehicle_id=vehicle_id, cancel_reason=cancel_reason)
        )
         
    @classmethod
    async def rch(cls, body: RchSchema) -> AsyncHttpResponse:
        """
        Rch
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/message_event/rch"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def update_qc_task(cls, body: UpdateQcTaskSchema) -> AsyncHttpResponse:
        """
        Update Task
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/message_event/update_qc_task"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def event(cls, body: EventListenerInSchema,event_type: ReceiveTaskType) -> AsyncHttpResponse:
        """
        Event Listener
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/message_event/event"
            ),
            json=body.dict(),
            params=dict(event_type=event_type)
        )
         
    @classmethod
    async def cancel_camunda_process(cls, body: CancelCamundaSchema) -> AsyncHttpResponse:
        """
        Cancel Camunda Process
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/message_event/cancel_camunda_process"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def boundary_event(cls, body: BoundaryEventSchema) -> AsyncHttpResponse:
        """
        Boundary Event
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/message_event/boundary_event"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def skip(cls, vehicle_id: str, target_node: str, current_task_id: str) -> AsyncHttpResponse:
        """
        节点跳跃
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/process_instance/skip"
            ),
            
            params=dict(vehicle_id=vehicle_id, target_node=target_node, current_task_id=current_task_id)
        )
         
    @classmethod
    async def activity(cls, vehicle_id: str) -> AsyncHttpResponse:
        """
        获取当前节点Name
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/process_instance/activity"
            ),
            params=dict(vehicle_id=vehicle_id)
        )
         
    @classmethod
    async def service_task(cls, body: ServiceTaskInSchema) -> AsyncHttpResponse:
        """
        
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/service_task"
            ),
            json=body.dict(),
            
        )
         