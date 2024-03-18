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
from ..schemas.inventory import *

__all__ = ["InventoryRequest"]


class InventoryRequestCls(ApiRequestBaseCls):
    def __init__(self):
        super(InventoryRequestCls, self).__init__()
        self.SERVICE_PORT = 19102
        self.SERVICE_NAME = "inventory"
        self.module_mapping[self.SERVICE_NAME] = self

    async def AddPoint(self, body: AddPointSchema) -> Tuple[int, Dict]:
        """
        导入点位
        根据地图组给的点位文件, 并新增QC、SC等虚拟点位
        """
        return await self.request(
            request=async_post,
            api="/api/position/AddPoint",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def AddPoint_sync(self, body: AddPointSchema) -> Tuple[int, Dict]:
        """
        导入点位
        根据地图组给的点位文件, 并新增QC、SC等虚拟点位
        """
        return self.request_sync(
            request=requests.post,
            api="/api/position/AddPoint",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def GetPointsHeading(
        self, body: PositionWithoutTierSchema
    ) -> Tuple[int, ResponseSuccess]:
        """
        获取点位Heading
        获取1层的点位和其对应的2个heading
        """
        return await self.request(
            request=async_post,
            api="/api/position/GetPointsHeading",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=ResponseSuccess,
        )

    def GetPointsHeading_sync(
        self, body: PositionWithoutTierSchema
    ) -> Tuple[int, ResponseSuccess]:
        """
        获取点位Heading
        获取1层的点位和其对应的2个heading
        """
        return self.request_sync(
            request=requests.post,
            api="/api/position/GetPointsHeading",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=ResponseSuccess,
        )

    async def GetAvailableTier(self, body: GetAvailableTierSchema) -> Tuple[int, Dict]:
        """
        获取可用的层
        返回一个可以放箱的层数, None表示不可放
        """
        return await self.request(
            request=async_post,
            api="/api/position/GetAvailableTier",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def GetAvailableTier_sync(self, body: GetAvailableTierSchema) -> Tuple[int, Dict]:
        """
        获取可用的层
        返回一个可以放箱的层数, None表示不可放
        """
        return self.request_sync(
            request=requests.post,
            api="/api/position/GetAvailableTier",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def GetContainerPoints(
        self, body: GetContainerPointsSchema
    ) -> Tuple[int, Dict]:
        """
        查询箱子和点位
        Api Description
        """
        return await self.request(
            request=async_post,
            api="/api/container/GetContainerPoints",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def GetContainerPoints_sync(
        self, body: GetContainerPointsSchema
    ) -> Tuple[int, Dict]:
        """
        查询箱子和点位
        Api Description
        """
        return self.request_sync(
            request=requests.post,
            api="/api/container/GetContainerPoints",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def InventoryUpdate(self, body: InventoryUpdateSchema) -> Tuple[int, Dict]:
        """
        箱子增删改
        对箱子进行增、删、抓、放、upsert操作
        """
        return await self.request(
            request=async_post,
            api="/api/container/InventoryUpdate",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def InventoryUpdate_sync(self, body: InventoryUpdateSchema) -> Tuple[int, Dict]:
        """
        箱子增删改
        对箱子进行增、删、抓、放、upsert操作
        """
        return self.request_sync(
            request=requests.post,
            api="/api/container/InventoryUpdate",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def ContainerCheck(self, body: ContainerCheckSchema) -> Tuple[int, Dict]:
        """
        箱子校验
        对增、抓、放操作进行校验
        """
        return await self.request(
            request=async_post,
            api="/api/container/ContainerCheck",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def ContainerCheck_sync(self, body: ContainerCheckSchema) -> Tuple[int, Dict]:
        """
        箱子校验
        对增、抓、放操作进行校验
        """
        return self.request_sync(
            request=requests.post,
            api="/api/container/ContainerCheck",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def ImportAreaContainers(
        self, body: ImportContainersSchema
    ) -> Tuple[int, Dict]:
        """
        批量导入固定区域箱子
        对某个区域进行批量导箱
        """
        return await self.request(
            request=async_post,
            api="/api/container/ImportAreaContainers",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def ImportAreaContainers_sync(
        self, body: ImportContainersSchema
    ) -> Tuple[int, Dict]:
        """
        批量导入固定区域箱子
        对某个区域进行批量导箱
        """
        return self.request_sync(
            request=requests.post,
            api="/api/container/ImportAreaContainers",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def ImportContainers(self, body: ImportContainersSchema) -> Tuple[int, Dict]:
        """
        批量导入箱子
        先清空当前所有箱子, 再导入所有箱子
        """
        return await self.request(
            request=async_post,
            api="/api/container/ImportContainers",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def ImportContainers_sync(self, body: ImportContainersSchema) -> Tuple[int, Dict]:
        """
        批量导入箱子
        先清空当前所有箱子, 再导入所有箱子
        """
        return self.request_sync(
            request=requests.post,
            api="/api/container/ImportContainers",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def RemoveContainers(self, body: RemoveContainerSchema) -> Tuple[int, Dict]:
        """
        批量删除箱子
        根据传参批量删除箱子, 默认全删
        """
        return await self.request(
            request=async_post,
            api="/api/container/RemoveContainers",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def RemoveContainers_sync(self, body: RemoveContainerSchema) -> Tuple[int, Dict]:
        """
        批量删除箱子
        根据传参批量删除箱子, 默认全删
        """
        return self.request_sync(
            request=requests.post,
            api="/api/container/RemoveContainers",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def EditContainers(self, body: EditContainerSchema) -> Tuple[int, Dict]:
        """
        编辑箱子信息
        针对GUI使用, 使用箱子的unique_id, 编辑箱号、朝向, 以及更改点位
        """
        return await self.request(
            request=async_post,
            api="/api/container/EditContainers",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def EditContainers_sync(self, body: EditContainerSchema) -> Tuple[int, Dict]:
        """
        编辑箱子信息
        针对GUI使用, 使用箱子的unique_id, 编辑箱号、朝向, 以及更改点位
        """
        return self.request_sync(
            request=requests.post,
            api="/api/container/EditContainers",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def LimitLow(self, body: LimitLowSchema) -> Tuple[int, Dict]:
        """
        最低高度查询
        查询某个路径上的最低的箱子的高度
        """
        return await self.request(
            request=async_post,
            api="/api/container/LimitLow",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def LimitLow_sync(self, body: LimitLowSchema) -> Tuple[int, Dict]:
        """
        最低高度查询
        查询某个路径上的最低的箱子的高度
        """
        return self.request_sync(
            request=requests.post,
            api="/api/container/LimitLow",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def EventListen(self, body: EventListenSchema) -> Tuple[int, Dict]:
        """
        箱子监听
        监听某个位置的箱子, 并推送给Task Executor
        """
        return await self.request(
            request=async_post,
            api="/api/container/EventListen",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def EventListen_sync(self, body: EventListenSchema) -> Tuple[int, Dict]:
        """
        箱子监听
        监听某个位置的箱子, 并推送给Task Executor
        """
        return self.request_sync(
            request=requests.post,
            api="/api/container/EventListen",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def ContainerQuery(self, body: ContainerQuerySchema) -> Tuple[int, Dict]:
        """
        箱子针对性查询
        查询特定场景下的箱子信息, 一般不包含点位
        """
        return await self.request(
            request=async_post,
            api="/api/container/ContainerQuery",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def ContainerQuery_sync(self, body: ContainerQuerySchema) -> Tuple[int, Dict]:
        """
        箱子针对性查询
        查询特定场景下的箱子信息, 一般不包含点位
        """
        return self.request_sync(
            request=requests.post,
            api="/api/container/ContainerQuery",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def ContainerTaskCheck(self, body: TaskCheckSchema) -> Tuple[int, Dict]:
        """
        箱子任务校验
        Api Description
        """
        return await self.request(
            request=async_post,
            api="/api/container/ContainerTaskCheck",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def ContainerTaskCheck_sync(self, body: TaskCheckSchema) -> Tuple[int, Dict]:
        """
        箱子任务校验
        Api Description
        """
        return self.request_sync(
            request=requests.post,
            api="/api/container/ContainerTaskCheck",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def CommonInfo(self, body: ContainerCommonInfoSchema) -> Tuple[int, Dict]:
        """
        箱子通用信息
        包括朝向、ISO等, 参数为orientation、iso
        """
        return await self.request(
            request=async_post,
            api="/api/container/CommonInfo",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def CommonInfo_sync(self, body: ContainerCommonInfoSchema) -> Tuple[int, Dict]:
        """
        箱子通用信息
        包括朝向、ISO等, 参数为orientation、iso
        """
        return self.request_sync(
            request=requests.post,
            api="/api/container/CommonInfo",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def TGInitNotify(self, body: TGInitNotifySchema) -> Tuple[int, Dict]:
        """
        TG到达通知
        TG到达通知, 根据TG类型动态添加TG点位
        """
        return await self.request(
            request=async_post,
            api="/api/TGInitNotify",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def TGInitNotify_sync(self, body: TGInitNotifySchema) -> Tuple[int, Dict]:
        """
        TG到达通知
        TG到达通知, 根据TG类型动态添加TG点位
        """
        return self.request_sync(
            request=requests.post,
            api="/api/TGInitNotify",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def QcLeaveNotify(self, body: QcLeaveNotifySchema) -> Tuple[int, Dict]:
        """
        QC离开通知
        FMS需要根据坐标将QC的虚拟点位转换为逻辑点位
        """
        return await self.request(
            request=async_post,
            api="/api/QcLeaveNotify",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def QcLeaveNotify_sync(self, body: QcLeaveNotifySchema) -> Tuple[int, Dict]:
        """
        QC离开通知
        FMS需要根据坐标将QC的虚拟点位转换为逻辑点位
        """
        return self.request_sync(
            request=requests.post,
            api="/api/QcLeaveNotify",
            body={
                "data": body,
            },
            resp_model=None,
        )


InventoryRequest = InventoryRequestCls()
