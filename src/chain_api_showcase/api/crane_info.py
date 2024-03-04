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

from ..schemas.crane_info import *

FMS_IP_ADDRESS = f"http://{os.environ.get('FMS_IP_ADDRESS', '127.0.0.1')}"


class Crane_InfoRequest(object):
    url = FMS_IP_ADDRESS + ":" + "8014"
    
    @classmethod
    async def asc_cps_info_report(cls, body: CPSInfoRequestModel) -> AsyncHttpResponse:
        """
        Asc Cps Info Report
        CPS数据
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/asc_cps_info_report"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def plc(cls, body: PlcDataRequestModel) -> AsyncHttpResponse:
        """
        Plc
        接收TE发过来的opcua数据
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/plc"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def application_lane_handler(cls, body: ApplicationLaneRequestModel) -> AsyncHttpResponse:
        """
        
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/application_lane_handler"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def qc_holding_info(cls, body: QCPointRequestModel) -> AsyncHttpResponse:
        """
        
        选择qc holding point 等待区
:return:
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/qc_holding_info"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def query_container_point(cls, body: ContainerPointRequestModel) -> AsyncHttpResponse:
        """
        
        为inventory提供卸船箱子点位
:return:
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/query_container_point"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def qc_position(cls, body: UpdateQCPositionModel) -> AsyncHttpResponse:
        """
        
        更新qc x
:return:
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/qc_position"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def qc_signal(cls, body: QCSignalRequestModel) -> AsyncHttpResponse:
        """
        
        创建或释放qc锁闭区
:return:
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/qc_signal"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def qc_holding_status(cls, body: QCHoldingRequestModel) -> AsyncHttpResponse:
        """
        
        {
  "messageName": "QC",
  "messageUniqueID": "",
  "messageTimestamp":"",
  "deviceId": 1,
  "lane": 1
}
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/qc_holding_status"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def api_response_mixed_area_post(cls, body: MixedAreaRequestModel) -> AsyncHttpResponse:
        """
        
        {"messageNumber":8,
"value":True
}
airlock，跨运车在里面申请开门num 8,ceg:atuo 门发10， 手动门发9
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/response_mixed_area"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def api_engine_post(cls, body: EngineRequestModel) -> AsyncHttpResponse:
        """
        
        {
"sc":"SC01",
"value":True,
"node":engine
}
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/engine"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def update_plc_data(cls, body: UpdatePlcDataModel) -> AsyncHttpResponse:
        """
        
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/update_plc_data"
            ),
            json=body.dict(),
            
        )
         