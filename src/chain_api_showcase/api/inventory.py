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

from ..schemas.inventory import *

FMS_IP_ADDRESS = f"http://{os.environ.get('FMS_IP_ADDRESS', '127.0.0.1')}"


class InventoryRequest(object):
    url = FMS_IP_ADDRESS + ":" + "19102"

    @classmethod
    async def AddPoint(cls, body: AddPointSchema) -> Tuple[int, Dict]:
        """
        导入点位
        根据地图组给的点位文件, 并新增QC、SC等虚拟点位
        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/position/AddPoint"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/position/AddPoint, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def GetPointsHeading(
        cls, body: PositionWithoutTierSchema
    ) -> Tuple[int, ResponseSuccess]:
        """
        获取点位Heading
        获取1层的点位和其对应的2个heading
        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/position/GetPointsHeading"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/position/GetPointsHeading, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, ResponseSuccess.model_validate_json(resp)

    @classmethod
    async def GetAvailableTier(cls, body: GetAvailableTierSchema) -> Tuple[int, Dict]:
        """
        获取可用的层
        返回一个可以放箱的层数, None表示不可放
        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/position/GetAvailableTier"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/position/GetAvailableTier, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def GetContainerPoints(
        cls, body: GetContainerPointsSchema
    ) -> Tuple[int, Dict]:
        """
        查询箱子和点位
        Api Description
        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/container/GetContainerPoints"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/container/GetContainerPoints, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def InventoryUpdate(cls, body: InventoryUpdateSchema) -> Tuple[int, Dict]:
        """
        箱子增删改
        对箱子进行增、删、抓、放、upsert操作
        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/container/InventoryUpdate"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/container/InventoryUpdate, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def ContainerCheck(cls, body: ContainerCheckSchema) -> Tuple[int, Dict]:
        """
        箱子校验
        对增、抓、放操作进行校验
        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/container/ContainerCheck"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/container/ContainerCheck, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def ImportAreaContainers(
        cls, body: ImportContainersSchema
    ) -> Tuple[int, Dict]:
        """
        批量导入固定区域箱子
        对某个区域进行批量导箱
        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/container/ImportAreaContainers"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/container/ImportAreaContainers, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def ImportContainers(cls, body: ImportContainersSchema) -> Tuple[int, Dict]:
        """
        批量导入箱子
        先清空当前所有箱子, 再导入所有箱子
        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/container/ImportContainers"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/container/ImportContainers, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def RemoveContainers(cls, body: RemoveContainerSchema) -> Tuple[int, Dict]:
        """
        批量删除箱子
        根据传参批量删除箱子, 默认全删
        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/container/RemoveContainers"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/container/RemoveContainers, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def EditContainers(cls, body: EditContainerSchema) -> Tuple[int, Dict]:
        """
        编辑箱子信息
        针对GUI使用, 使用箱子的unique_id, 编辑箱号、朝向, 以及更改点位
        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/container/EditContainers"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/container/EditContainers, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def LimitLow(cls, body: LimitLowSchema) -> Tuple[int, Dict]:
        """
        最低高度查询
        查询某个路径上的最低的箱子的高度
        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/container/LimitLow"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/container/LimitLow, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def ContainerQuery(cls, body: ContainerQuerySchema) -> Tuple[int, Dict]:
        """
        箱子针对性查询
        查询特定场景下的箱子信息, 一般不包含点位
        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/container/ContainerQuery"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/container/ContainerQuery, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def ContainerTaskCheck(cls, body: TaskCheckSchema) -> Tuple[int, Dict]:
        """
        箱子任务校验
        Api Description
        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/container/ContainerTaskCheck"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/container/ContainerTaskCheck, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def CommonInfo(cls, body: ContainerCommonInfoSchema) -> Tuple[int, Dict]:
        """
        箱子通用信息
        包括朝向、ISO等, 参数为orientation、iso
        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/container/CommonInfo"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/container/CommonInfo, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def TGInitNotify(cls, body: TGInitNotifySchema) -> Tuple[int, Dict]:
        """
        TG到达通知
        TG到达通知, 根据TG类型动态添加TG点位
        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/TGInitNotify"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/TGInitNotify, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def QcLeaveNotify(cls, body: QcLeaveNotifySchema) -> Tuple[int, Dict]:
        """
        QC离开通知
        FMS需要根据坐标将QC的虚拟点位转换为逻辑点位
        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/QcLeaveNotify"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/QcLeaveNotify, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()
