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
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/position/AddPoint"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/position/AddPoint, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def AddPoint_sync(self, body: AddPointSchema) -> Tuple[int, Dict]:
        """
        导入点位
        根据地图组给的点位文件, 并新增QC、SC等虚拟点位
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/position/AddPoint"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/position/AddPoint, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def GetPointsHeading(
        self, body: PositionWithoutTierSchema
    ) -> Tuple[int, ResponseSuccess]:
        """
        获取点位Heading
        获取1层的点位和其对应的2个heading
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/position/GetPointsHeading"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/position/GetPointsHeading, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, ResponseSuccess.model_validate_json(resp)

    def GetPointsHeading_sync(
        self, body: PositionWithoutTierSchema
    ) -> Tuple[int, ResponseSuccess]:
        """
        获取点位Heading
        获取1层的点位和其对应的2个heading
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/position/GetPointsHeading"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/position/GetPointsHeading, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, ResponseSuccess.model_validate_json(resp)

    async def GetAvailableTier(self, body: GetAvailableTierSchema) -> Tuple[int, Dict]:
        """
        获取可用的层
        返回一个可以放箱的层数, None表示不可放
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/position/GetAvailableTier"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/position/GetAvailableTier, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def GetAvailableTier_sync(self, body: GetAvailableTierSchema) -> Tuple[int, Dict]:
        """
        获取可用的层
        返回一个可以放箱的层数, None表示不可放
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/position/GetAvailableTier"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/position/GetAvailableTier, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def GetContainerPoints(
        self, body: GetContainerPointsSchema
    ) -> Tuple[int, Dict]:
        """
        查询箱子和点位
        Api Description
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/container/GetContainerPoints"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/container/GetContainerPoints, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def GetContainerPoints_sync(
        self, body: GetContainerPointsSchema
    ) -> Tuple[int, Dict]:
        """
        查询箱子和点位
        Api Description
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/container/GetContainerPoints"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/container/GetContainerPoints, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def InventoryUpdate(self, body: InventoryUpdateSchema) -> Tuple[int, Dict]:
        """
        箱子增删改
        对箱子进行增、删、抓、放、upsert操作
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/container/InventoryUpdate"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/container/InventoryUpdate, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def InventoryUpdate_sync(self, body: InventoryUpdateSchema) -> Tuple[int, Dict]:
        """
        箱子增删改
        对箱子进行增、删、抓、放、upsert操作
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/container/InventoryUpdate"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/container/InventoryUpdate, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def ContainerCheck(self, body: ContainerCheckSchema) -> Tuple[int, Dict]:
        """
        箱子校验
        对增、抓、放操作进行校验
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/container/ContainerCheck"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/container/ContainerCheck, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def ContainerCheck_sync(self, body: ContainerCheckSchema) -> Tuple[int, Dict]:
        """
        箱子校验
        对增、抓、放操作进行校验
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/container/ContainerCheck"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/container/ContainerCheck, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def ImportAreaContainers(
        self, body: ImportContainersSchema
    ) -> Tuple[int, Dict]:
        """
        批量导入固定区域箱子
        对某个区域进行批量导箱
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/container/ImportAreaContainers"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/container/ImportAreaContainers, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def ImportAreaContainers_sync(
        self, body: ImportContainersSchema
    ) -> Tuple[int, Dict]:
        """
        批量导入固定区域箱子
        对某个区域进行批量导箱
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/container/ImportAreaContainers"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/container/ImportAreaContainers, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def ImportContainers(self, body: ImportContainersSchema) -> Tuple[int, Dict]:
        """
        批量导入箱子
        先清空当前所有箱子, 再导入所有箱子
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/container/ImportContainers"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/container/ImportContainers, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def ImportContainers_sync(self, body: ImportContainersSchema) -> Tuple[int, Dict]:
        """
        批量导入箱子
        先清空当前所有箱子, 再导入所有箱子
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/container/ImportContainers"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/container/ImportContainers, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def RemoveContainers(self, body: RemoveContainerSchema) -> Tuple[int, Dict]:
        """
        批量删除箱子
        根据传参批量删除箱子, 默认全删
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/container/RemoveContainers"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/container/RemoveContainers, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def RemoveContainers_sync(self, body: RemoveContainerSchema) -> Tuple[int, Dict]:
        """
        批量删除箱子
        根据传参批量删除箱子, 默认全删
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/container/RemoveContainers"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/container/RemoveContainers, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def EditContainers(self, body: EditContainerSchema) -> Tuple[int, Dict]:
        """
        编辑箱子信息
        针对GUI使用, 使用箱子的unique_id, 编辑箱号、朝向, 以及更改点位
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/container/EditContainers"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/container/EditContainers, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def EditContainers_sync(self, body: EditContainerSchema) -> Tuple[int, Dict]:
        """
        编辑箱子信息
        针对GUI使用, 使用箱子的unique_id, 编辑箱号、朝向, 以及更改点位
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/container/EditContainers"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/container/EditContainers, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def LimitLow(self, body: LimitLowSchema) -> Tuple[int, Dict]:
        """
        最低高度查询
        查询某个路径上的最低的箱子的高度
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/container/LimitLow"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/container/LimitLow, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def LimitLow_sync(self, body: LimitLowSchema) -> Tuple[int, Dict]:
        """
        最低高度查询
        查询某个路径上的最低的箱子的高度
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/container/LimitLow"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/container/LimitLow, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def ContainerQuery(self, body: ContainerQuerySchema) -> Tuple[int, Dict]:
        """
        箱子针对性查询
        查询特定场景下的箱子信息, 一般不包含点位
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/container/ContainerQuery"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/container/ContainerQuery, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def ContainerQuery_sync(self, body: ContainerQuerySchema) -> Tuple[int, Dict]:
        """
        箱子针对性查询
        查询特定场景下的箱子信息, 一般不包含点位
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/container/ContainerQuery"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/container/ContainerQuery, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def ContainerTaskCheck(self, body: TaskCheckSchema) -> Tuple[int, Dict]:
        """
        箱子任务校验
        Api Description
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/container/ContainerTaskCheck"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/container/ContainerTaskCheck, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def ContainerTaskCheck_sync(self, body: TaskCheckSchema) -> Tuple[int, Dict]:
        """
        箱子任务校验
        Api Description
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/container/ContainerTaskCheck"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/container/ContainerTaskCheck, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def CommonInfo(self, body: ContainerCommonInfoSchema) -> Tuple[int, Dict]:
        """
        箱子通用信息
        包括朝向、ISO等, 参数为orientation、iso
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/container/CommonInfo"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/container/CommonInfo, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def CommonInfo_sync(self, body: ContainerCommonInfoSchema) -> Tuple[int, Dict]:
        """
        箱子通用信息
        包括朝向、ISO等, 参数为orientation、iso
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/container/CommonInfo"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/container/CommonInfo, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def TGInitNotify(self, body: TGInitNotifySchema) -> Tuple[int, Dict]:
        """
        TG到达通知
        TG到达通知, 根据TG类型动态添加TG点位
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/TGInitNotify"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/TGInitNotify, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def TGInitNotify_sync(self, body: TGInitNotifySchema) -> Tuple[int, Dict]:
        """
        TG到达通知
        TG到达通知, 根据TG类型动态添加TG点位
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/TGInitNotify"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/TGInitNotify, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def QcLeaveNotify(self, body: QcLeaveNotifySchema) -> Tuple[int, Dict]:
        """
        QC离开通知
        FMS需要根据坐标将QC的虚拟点位转换为逻辑点位
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/QcLeaveNotify"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/QcLeaveNotify, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def QcLeaveNotify_sync(self, body: QcLeaveNotifySchema) -> Tuple[int, Dict]:
        """
        QC离开通知
        FMS需要根据坐标将QC的虚拟点位转换为逻辑点位
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/QcLeaveNotify"),
            timeout=self.timeout,
            json=body.dict(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/QcLeaveNotify, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def KpiEventCallback(self) -> Tuple[int, Dict]:
        """
        KPI事件回调
        KPI事件回调, 用于更新KPI信息
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/event/KpiEventCallback"),
            timeout=self.timeout,
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/event/KpiEventCallback, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def KpiEventCallback_sync(self) -> Tuple[int, Dict]:
        """
        KPI事件回调
        KPI事件回调, 用于更新KPI信息
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/event/KpiEventCallback"),
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/event/KpiEventCallback, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()


InventoryRequest = InventoryRequestCls()
