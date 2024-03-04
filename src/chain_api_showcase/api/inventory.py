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

from ..schemas.inventory import *

FMS_IP_ADDRESS = f"http://{os.environ.get('FMS_IP_ADDRESS', '127.0.0.1')}"


class InventoryRequest(object):
    url = FMS_IP_ADDRESS + ":" + "19102"
    
    @classmethod
    async def AddPoint(cls, body: AddPointSchema) -> AsyncHttpResponse:
        """
        导入点位
        根据地图组给的点位文件, 并新增QC、SC等虚拟点位
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/position/AddPoint"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def GetPointsHeading(cls, body: PositionWithoutTierSchema) -> AsyncHttpResponse:
        """
        获取点位Heading
        获取1层的点位和其对应的2个heading
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/position/GetPointsHeading"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def GetAvailableTier(cls, body: GetAvailableTierSchema) -> AsyncHttpResponse:
        """
        获取可用的层
        返回一个可以放箱的层数, None表示不可放
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/position/GetAvailableTier"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def GetContainerPoints(cls, body: GetContainerPointsSchema) -> AsyncHttpResponse:
        """
        查询箱子和点位
        Api Description
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/container/GetContainerPoints"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def InventoryUpdate(cls, body: InventoryUpdateSchema) -> AsyncHttpResponse:
        """
        箱子增删改
        对箱子进行增、删、抓、放、upsert操作
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/container/InventoryUpdate"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def ContainerCheck(cls, body: ContainerCheckSchema) -> AsyncHttpResponse:
        """
        箱子校验
        对增、抓、放操作进行校验
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/container/ContainerCheck"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def ImportAreaContainers(cls, body: ImportContainersSchema) -> AsyncHttpResponse:
        """
        批量导入固定区域箱子
        对某个区域进行批量导箱
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/container/ImportAreaContainers"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def ImportContainers(cls, body: ImportContainersSchema) -> AsyncHttpResponse:
        """
        批量导入箱子
        先清空当前所有箱子, 再导入所有箱子
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/container/ImportContainers"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def RemoveContainers(cls, body: RemoveContainerSchema) -> AsyncHttpResponse:
        """
        批量删除箱子
        根据传参批量删除箱子, 默认全删
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/container/RemoveContainers"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def EditContainers(cls, body: EditContainerSchema) -> AsyncHttpResponse:
        """
        编辑箱子信息
        针对GUI使用, 使用箱子的unique_id, 编辑箱号、朝向, 以及更改点位
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/container/EditContainers"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def LimitLow(cls, body: LimitLowSchema) -> AsyncHttpResponse:
        """
        最低高度查询
        查询某个路径上的最低的箱子的高度
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/container/LimitLow"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def ContainerQuery(cls, body: ContainerQuerySchema) -> AsyncHttpResponse:
        """
        箱子针对性查询
        查询特定场景下的箱子信息, 一般不包含点位
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/container/ContainerQuery"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def ContainerTaskCheck(cls, body: TaskCheckSchema) -> AsyncHttpResponse:
        """
        箱子任务校验
        Api Description
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/container/ContainerTaskCheck"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def CommonInfo(cls, body: ContainerCommonInfoSchema) -> AsyncHttpResponse:
        """
        箱子通用信息
        包括朝向、ISO等, 参数为orientation、iso
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/container/CommonInfo"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def TGInitNotify(cls, body: TGInitNotifySchema) -> AsyncHttpResponse:
        """
        TG到达通知
        TG到达通知, 根据TG类型动态添加TG点位
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/TGInitNotify"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def QcLeaveNotify(cls, body: QcLeaveNotifySchema) -> AsyncHttpResponse:
        """
        QC离开通知
        FMS需要根据坐标将QC的虚拟点位转换为逻辑点位
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/QcLeaveNotify"
            ),
            json=body.dict(),
            
        )
         