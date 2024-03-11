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
from ..schemas.device_info import *

__all__ = ["DeviceInfoRequest"]


class DeviceInfoRequestCls(ApiRequestBaseCls):
    def __init__(self):
        super(DeviceInfoRequestCls, self).__init__()
        self.SERVICE_PORT = 11000
        self.SERVICE_NAME = "device_info"
        self.module_mapping[self.SERVICE_NAME] = self

    async def api_deviceInfo_maintain_status_post(self) -> Tuple[int, Dict]:
        """
        Service Status

        """
        return await self.request(
            request=async_post,
            api="/api/deviceInfo/maintain/status",
            body={},
            resp_model=None,
        )

    def api_deviceInfo_maintain_status_post_sync(self) -> Tuple[int, Dict]:
        """
        Service Status

        """
        return self.request_sync(
            request=requests.post,
            api="/api/deviceInfo/maintain/status",
            body={},
            resp_model=None,
        )

    async def api_deviceInfo_maintain_start_tracemalloc_get(self) -> Tuple[int, Dict]:
        """
        Service Status

        """
        return await self.request(
            request=async_get,
            api="/api/deviceInfo/maintain/start_tracemalloc",
            body={},
            resp_model=None,
        )

    def api_deviceInfo_maintain_start_tracemalloc_get_sync(self) -> Tuple[int, Dict]:
        """
        Service Status

        """
        return self.request_sync(
            request=requests.get,
            api="/api/deviceInfo/maintain/start_tracemalloc",
            body={},
            resp_model=None,
        )

    async def api_deviceInfo_maintain_stop_tracemalloc_get(self) -> Tuple[int, Dict]:
        """
        Service Status

        """
        return await self.request(
            request=async_get,
            api="/api/deviceInfo/maintain/stop_tracemalloc",
            body={},
            resp_model=None,
        )

    def api_deviceInfo_maintain_stop_tracemalloc_get_sync(self) -> Tuple[int, Dict]:
        """
        Service Status

        """
        return self.request_sync(
            request=requests.get,
            api="/api/deviceInfo/maintain/stop_tracemalloc",
            body={},
            resp_model=None,
        )

    async def api_deviceInfo_maintain_get_tracemalloc_get(self) -> Tuple[int, Dict]:
        """
        Service Status

        """
        return await self.request(
            request=async_get,
            api="/api/deviceInfo/maintain/get_tracemalloc",
            body={},
            resp_model=None,
        )

    def api_deviceInfo_maintain_get_tracemalloc_get_sync(self) -> Tuple[int, Dict]:
        """
        Service Status

        """
        return self.request_sync(
            request=requests.get,
            api="/api/deviceInfo/maintain/get_tracemalloc",
            body={},
            resp_model=None,
        )

    async def deleteVehicle(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        删除某个车辆的所有信息

        """
        return await self.request(
            request=async_post,
            api="/api/deviceInfo/maintain/deleteVehicle",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=None,
        )

    def deleteVehicle_sync(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        删除某个车辆的所有信息

        """
        return self.request_sync(
            request=requests.post,
            api="/api/deviceInfo/maintain/deleteVehicle",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=None,
        )

    async def deleteTg(self) -> Tuple[int, Dict]:
        """
        删除拖挂信息

        """
        return await self.request(
            request=async_post,
            api="/api/deviceInfo/maintain/deleteTg",
            body={},
            resp_model=None,
        )

    def deleteTg_sync(self) -> Tuple[int, Dict]:
        """
        删除拖挂信息

        """
        return self.request_sync(
            request=requests.post,
            api="/api/deviceInfo/maintain/deleteTg",
            body={},
            resp_model=None,
        )

    async def vehicleDetails(self, vehicle_id: str) -> Tuple[int, CreateSuccessSchema]:
        """
        获取车辆详情

        """
        return await self.request(
            request=async_get,
            api="/api/deviceInfo/vehicleStatus/vehicleDetails",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=CreateSuccessSchema,
        )

    def vehicleDetails_sync(self, vehicle_id: str) -> Tuple[int, CreateSuccessSchema]:
        """
        获取车辆详情

        """
        return self.request_sync(
            request=requests.get,
            api="/api/deviceInfo/vehicleStatus/vehicleDetails",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=CreateSuccessSchema,
        )

    async def api_deviceInfo_vehicleStatus_vehicleDetails_post(
        self,
        vehicle_id: str,
        vehicle_type: VehicleType,
        vin: str,
        color: str,
        manufacturer: str,
        engine_type: str,
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置车辆详情

        """
        return await self.request(
            request=async_post,
            api="/api/deviceInfo/vehicleStatus/vehicleDetails",
            body={
                "params": dict(
                    vehicle_id=vehicle_id,
                    vehicle_type=vehicle_type,
                    vin=vin,
                    color=color,
                    manufacturer=manufacturer,
                    engine_type=engine_type,
                )
            },
            resp_model=CreateSuccessSchema,
        )

    def api_deviceInfo_vehicleStatus_vehicleDetails_post_sync(
        self,
        vehicle_id: str,
        vehicle_type: VehicleType,
        vin: str,
        color: str,
        manufacturer: str,
        engine_type: str,
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置车辆详情

        """
        return self.request_sync(
            request=requests.post,
            api="/api/deviceInfo/vehicleStatus/vehicleDetails",
            body={
                "params": dict(
                    vehicle_id=vehicle_id,
                    vehicle_type=vehicle_type,
                    vin=vin,
                    color=color,
                    manufacturer=manufacturer,
                    engine_type=engine_type,
                )
            },
            resp_model=CreateSuccessSchema,
        )

    async def LoginStatus(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取单车登录状态

        """
        return await self.request(
            request=async_get,
            api="/api/deviceInfo/vehicleStatus/LoginStatus",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=None,
        )

    def LoginStatus_sync(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取单车登录状态

        """
        return self.request_sync(
            request=requests.get,
            api="/api/deviceInfo/vehicleStatus/LoginStatus",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=None,
        )

    async def api_deviceInfo_vehicleStatus_LoginStatus_post(
        self, body: SetLoginStatusPost
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置单车登录状态

        """
        return await self.request(
            request=async_post,
            api="/api/deviceInfo/vehicleStatus/LoginStatus",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def api_deviceInfo_vehicleStatus_LoginStatus_post_sync(
        self, body: SetLoginStatusPost
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置单车登录状态

        """
        return self.request_sync(
            request=requests.post,
            api="/api/deviceInfo/vehicleStatus/LoginStatus",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def api_deviceInfo_vehicleStatus_mode_get(
        self, vehicle_id: str
    ) -> Tuple[int, Dict]:
        """
        获取单车模式

        """
        return await self.request(
            request=async_get,
            api="/api/deviceInfo/vehicleStatus/mode",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=None,
        )

    def api_deviceInfo_vehicleStatus_mode_get_sync(
        self, vehicle_id: str
    ) -> Tuple[int, Dict]:
        """
        获取单车模式

        """
        return self.request_sync(
            request=requests.get,
            api="/api/deviceInfo/vehicleStatus/mode",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=None,
        )

    async def api_deviceInfo_vehicleStatus_mode_post(
        self, body: SetModePost
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置单车模式

        """
        return await self.request(
            request=async_post,
            api="/api/deviceInfo/vehicleStatus/mode",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def api_deviceInfo_vehicleStatus_mode_post_sync(
        self, body: SetModePost
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置单车模式

        """
        return self.request_sync(
            request=requests.post,
            api="/api/deviceInfo/vehicleStatus/mode",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def bsm(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取单车坐标

        """
        return await self.request(
            request=async_get,
            api="/api/deviceInfo/vehicleStatus/bsm",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=None,
        )

    def bsm_sync(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取单车坐标

        """
        return self.request_sync(
            request=requests.get,
            api="/api/deviceInfo/vehicleStatus/bsm",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=None,
        )

    async def api_deviceInfo_vehicleStatus_bsm_post(
        self, body: object
    ) -> Tuple[int, Dict]:
        """
        设置单车坐标

        """
        return await self.request(
            request=async_post,
            api="/api/deviceInfo/vehicleStatus/bsm",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def api_deviceInfo_vehicleStatus_bsm_post_sync(
        self, body: object
    ) -> Tuple[int, Dict]:
        """
        设置单车坐标

        """
        return self.request_sync(
            request=requests.post,
            api="/api/deviceInfo/vehicleStatus/bsm",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    async def soc(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取单车电量

        """
        return await self.request(
            request=async_get,
            api="/api/deviceInfo/vehicleStatus/soc",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=None,
        )

    def soc_sync(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取单车电量

        """
        return self.request_sync(
            request=requests.get,
            api="/api/deviceInfo/vehicleStatus/soc",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=None,
        )

    async def api_deviceInfo_vehicleStatus_soc_post(
        self, body: SetSocPost
    ) -> Tuple[int, Dict]:
        """
        设置单车电量

        """
        return await self.request(
            request=async_post,
            api="/api/deviceInfo/vehicleStatus/soc",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def api_deviceInfo_vehicleStatus_soc_post_sync(
        self, body: SetSocPost
    ) -> Tuple[int, Dict]:
        """
        设置单车电量

        """
        return self.request_sync(
            request=requests.post,
            api="/api/deviceInfo/vehicleStatus/soc",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    async def longPath(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取长路径

        """
        return await self.request(
            request=async_get,
            api="/api/deviceInfo/vehicleStatus/longPath",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=None,
        )

    def longPath_sync(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取长路径

        """
        return self.request_sync(
            request=requests.get,
            api="/api/deviceInfo/vehicleStatus/longPath",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=None,
        )

    async def api_deviceInfo_vehicleStatus_longPath_post(
        self, body: SetLongPath
    ) -> Tuple[int, Dict]:
        """
        设置长路径

        """
        return await self.request(
            request=async_post,
            api="/api/deviceInfo/vehicleStatus/longPath",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def api_deviceInfo_vehicleStatus_longPath_post_sync(
        self, body: SetLongPath
    ) -> Tuple[int, Dict]:
        """
        设置长路径

        """
        return self.request_sync(
            request=requests.post,
            api="/api/deviceInfo/vehicleStatus/longPath",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    async def shortPath(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取短路径

        """
        return await self.request(
            request=async_get,
            api="/api/deviceInfo/vehicleStatus/shortPath",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=None,
        )

    def shortPath_sync(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取短路径

        """
        return self.request_sync(
            request=requests.get,
            api="/api/deviceInfo/vehicleStatus/shortPath",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=None,
        )

    async def api_deviceInfo_vehicleStatus_shortPath_post(
        self, body: SetShortPath
    ) -> Tuple[int, Dict]:
        """
        设置短路径

        """
        return await self.request(
            request=async_post,
            api="/api/deviceInfo/vehicleStatus/shortPath",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def api_deviceInfo_vehicleStatus_shortPath_post_sync(
        self, body: SetShortPath
    ) -> Tuple[int, Dict]:
        """
        设置短路径

        """
        return self.request_sync(
            request=requests.post,
            api="/api/deviceInfo/vehicleStatus/shortPath",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    async def suspend(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取单车急停状态

        """
        return await self.request(
            request=async_get,
            api="/api/deviceInfo/vehicleStatus/suspend",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=None,
        )

    def suspend_sync(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取单车急停状态

        """
        return self.request_sync(
            request=requests.get,
            api="/api/deviceInfo/vehicleStatus/suspend",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=None,
        )

    async def api_deviceInfo_vehicleStatus_suspend_post(
        self, body: object
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置单车急停状态

        """
        return await self.request(
            request=async_post,
            api="/api/deviceInfo/vehicleStatus/suspend",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def api_deviceInfo_vehicleStatus_suspend_post_sync(
        self, body: object
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置单车急停状态

        """
        return self.request_sync(
            request=requests.post,
            api="/api/deviceInfo/vehicleStatus/suspend",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def api_deviceInfo_vehicleStatus_trailerStatus_get(
        self, vehicle_id: str
    ) -> Tuple[int, Dict]:
        """
        获取单车拖挂状态

        """
        return await self.request(
            request=async_get,
            api="/api/deviceInfo/vehicleStatus/trailerStatus",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=None,
        )

    def api_deviceInfo_vehicleStatus_trailerStatus_get_sync(
        self, vehicle_id: str
    ) -> Tuple[int, Dict]:
        """
        获取单车拖挂状态

        """
        return self.request_sync(
            request=requests.get,
            api="/api/deviceInfo/vehicleStatus/trailerStatus",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=None,
        )

    async def api_deviceInfo_vehicleStatus_trailerStatus_post(
        self, body: SetTrailerStatusPost
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置单车拖挂状态

        """
        return await self.request(
            request=async_post,
            api="/api/deviceInfo/vehicleStatus/trailerStatus",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def api_deviceInfo_vehicleStatus_trailerStatus_post_sync(
        self, body: SetTrailerStatusPost
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置单车拖挂状态

        """
        return self.request_sync(
            request=requests.post,
            api="/api/deviceInfo/vehicleStatus/trailerStatus",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def ghostVehicle(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取幽灵车状态

        """
        return await self.request(
            request=async_get,
            api="/api/deviceInfo/vehicleStatus/ghostVehicle",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=None,
        )

    def ghostVehicle_sync(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取幽灵车状态

        """
        return self.request_sync(
            request=requests.get,
            api="/api/deviceInfo/vehicleStatus/ghostVehicle",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=None,
        )

    async def api_deviceInfo_vehicleStatus_ghostVehicle_post(
        self, body: SetGhostVehiclePost
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置幽灵车状态

        """
        return await self.request(
            request=async_post,
            api="/api/deviceInfo/vehicleStatus/ghostVehicle",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def api_deviceInfo_vehicleStatus_ghostVehicle_post_sync(
        self, body: SetGhostVehiclePost
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置幽灵车状态

        """
        return self.request_sync(
            request=requests.post,
            api="/api/deviceInfo/vehicleStatus/ghostVehicle",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def api_deviceInfo_vehicleStatus_ghostVehicleCancel_post(
        self, body: SetGhostVehicleCancelPost
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置幽灵车取消状态

        """
        return await self.request(
            request=async_post,
            api="/api/deviceInfo/vehicleStatus/ghostVehicleCancel",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def api_deviceInfo_vehicleStatus_ghostVehicleCancel_post_sync(
        self, body: SetGhostVehicleCancelPost
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置幽灵车取消状态

        """
        return self.request_sync(
            request=requests.post,
            api="/api/deviceInfo/vehicleStatus/ghostVehicleCancel",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def getVehicleChassis(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取车辆底盘信息

        """
        return await self.request(
            request=async_get,
            api="/api/deviceInfo/vehicleStatus/getVehicleChassis",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=None,
        )

    def getVehicleChassis_sync(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取车辆底盘信息

        """
        return self.request_sync(
            request=requests.get,
            api="/api/deviceInfo/vehicleStatus/getVehicleChassis",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=None,
        )

    async def getVehicleAscChassis(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取跨运车底盘信息

        """
        return await self.request(
            request=async_get,
            api="/api/deviceInfo/vehicleStatus/getVehicleAscChassis",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=None,
        )

    def getVehicleAscChassis_sync(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取跨运车底盘信息

        """
        return self.request_sync(
            request=requests.get,
            api="/api/deviceInfo/vehicleStatus/getVehicleAscChassis",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=None,
        )

    async def getVehiclesys(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取车辆系统信息

        """
        return await self.request(
            request=async_get,
            api="/api/deviceInfo/vehicleStatus/getVehiclesys",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=None,
        )

    def getVehiclesys_sync(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取车辆系统信息

        """
        return self.request_sync(
            request=requests.get,
            api="/api/deviceInfo/vehicleStatus/getVehiclesys",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=None,
        )

    async def api_deviceInfo_vehicleStatus_SetOperation_post(
        self, body: object
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置Operation状态

        """
        return await self.request(
            request=async_post,
            api="/api/deviceInfo/vehicleStatus/SetOperation",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def api_deviceInfo_vehicleStatus_SetOperation_post_sync(
        self, body: object
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置Operation状态

        """
        return self.request_sync(
            request=requests.post,
            api="/api/deviceInfo/vehicleStatus/SetOperation",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def Operation(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取Operation状态

        """
        return await self.request(
            request=async_get,
            api="/api/deviceInfo/vehicleStatus/Operation",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=None,
        )

    def Operation_sync(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取Operation状态

        """
        return self.request_sync(
            request=requests.get,
            api="/api/deviceInfo/vehicleStatus/Operation",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=None,
        )

    async def SuspendReasonReport(self, body: ReportSuspend) -> Tuple[int, Dict]:
        """
        报告车辆停止原因

        """
        return await self.request(
            request=async_post,
            api="/api/deviceInfo/vehicleStatus/SuspendReasonReport",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def SuspendReasonReport_sync(self, body: ReportSuspend) -> Tuple[int, Dict]:
        """
        报告车辆停止原因

        """
        return self.request_sync(
            request=requests.post,
            api="/api/deviceInfo/vehicleStatus/SuspendReasonReport",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    async def SuspendReason(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取车辆停止原因

        """
        return await self.request(
            request=async_get,
            api="/api/deviceInfo/vehicleStatus/SuspendReason",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=None,
        )

    def SuspendReason_sync(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取车辆停止原因

        """
        return self.request_sync(
            request=requests.get,
            api="/api/deviceInfo/vehicleStatus/SuspendReason",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=None,
        )

    async def StopTime(self, body: ReportStopTime) -> Tuple[int, Dict]:
        """
        报告车辆停车时长

        """
        return await self.request(
            request=async_post,
            api="/api/deviceInfo/vehicleStatus/StopTime",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def StopTime_sync(self, body: ReportStopTime) -> Tuple[int, Dict]:
        """
        报告车辆停车时长

        """
        return self.request_sync(
            request=requests.post,
            api="/api/deviceInfo/vehicleStatus/StopTime",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    async def CurrentStatus(self) -> Tuple[int, Dict]:
        """
        获取所有车辆的当前状态信息

        """
        return await self.request(
            request=async_get,
            api="/api/deviceInfo/vehicleStatus/CurrentStatus",
            body={},
            resp_model=None,
        )

    def CurrentStatus_sync(self) -> Tuple[int, Dict]:
        """
        获取所有车辆的当前状态信息

        """
        return self.request_sync(
            request=requests.get,
            api="/api/deviceInfo/vehicleStatus/CurrentStatus",
            body={},
            resp_model=None,
        )

    async def BtnStatus(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取急停，左驻车，右驻车的按钮状态

        """
        return await self.request(
            request=async_get,
            api="/api/deviceInfo/vehicleStatus/BtnStatus",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=None,
        )

    def BtnStatus_sync(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取急停，左驻车，右驻车的按钮状态

        """
        return self.request_sync(
            request=requests.get,
            api="/api/deviceInfo/vehicleStatus/BtnStatus",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=None,
        )

    async def api_deviceInfo_vehicleStatus_BtnStatus_post(
        self, body: BtnStatusSchemas, vehicle_id: str
    ) -> Tuple[int, Dict]:
        """
        设置急停，左驻车，右驻车的按钮状态

        """
        return await self.request(
            request=async_post,
            api="/api/deviceInfo/vehicleStatus/BtnStatus",
            body={
                "data": body.model_dump_json(),
                "params": dict(vehicle_id=vehicle_id),
            },
            resp_model=None,
        )

    def api_deviceInfo_vehicleStatus_BtnStatus_post_sync(
        self, body: BtnStatusSchemas, vehicle_id: str
    ) -> Tuple[int, Dict]:
        """
        设置急停，左驻车，右驻车的按钮状态

        """
        return self.request_sync(
            request=requests.post,
            api="/api/deviceInfo/vehicleStatus/BtnStatus",
            body={
                "data": body.model_dump_json(),
                "params": dict(vehicle_id=vehicle_id),
            },
            resp_model=None,
        )

    async def craneStatus(
        self, device_id: str, vehicle_id: str, lane: str, block: str, stack: str
    ) -> Tuple[int, Dict]:
        """
        获取 Crane 状态

        """
        return await self.request(
            request=async_get,
            api="/api/deviceInfo/craneStatus/",
            body={
                "params": dict(
                    device_id=device_id,
                    vehicle_id=vehicle_id,
                    lane=lane,
                    block=block,
                    stack=stack,
                )
            },
            resp_model=None,
        )

    def craneStatus_sync(
        self, device_id: str, vehicle_id: str, lane: str, block: str, stack: str
    ) -> Tuple[int, Dict]:
        """
        获取 Crane 状态

        """
        return self.request_sync(
            request=requests.get,
            api="/api/deviceInfo/craneStatus/",
            body={
                "params": dict(
                    device_id=device_id,
                    vehicle_id=vehicle_id,
                    lane=lane,
                    block=block,
                    stack=stack,
                )
            },
            resp_model=None,
        )

    async def lane(self, lane: str) -> Tuple[int, Dict]:
        """
        获取车道Y

        """
        return await self.request(
            request=async_get,
            api="/api/deviceInfo/craneStatus/lane",
            body={"params": dict(lane=lane)},
            resp_model=None,
        )

    def lane_sync(self, lane: str) -> Tuple[int, Dict]:
        """
        获取车道Y

        """
        return self.request_sync(
            request=requests.get,
            api="/api/deviceInfo/craneStatus/lane",
            body={"params": dict(lane=lane)},
            resp_model=None,
        )

    async def craneList(self, feild_get: str = "min") -> Tuple[int, Dict]:
        """
        获取 Crane 列表

        """
        return await self.request(
            request=async_get,
            api="/api/deviceInfo/craneStatus/craneList",
            body={"params": dict(feild_get=feild_get)},
            resp_model=None,
        )

    def craneList_sync(self, feild_get: str = "min") -> Tuple[int, Dict]:
        """
        获取 Crane 列表

        """
        return self.request_sync(
            request=requests.get,
            api="/api/deviceInfo/craneStatus/craneList",
            body={"params": dict(feild_get=feild_get)},
            resp_model=None,
        )

    async def plcStatus(self, device_id: str = "all") -> Tuple[int, Dict]:
        """
        获取 Plc 状态

        """
        return await self.request(
            request=async_get,
            api="/api/deviceInfo/plcStatus",
            body={"params": dict(device_id=device_id)},
            resp_model=None,
        )

    def plcStatus_sync(self, device_id: str = "all") -> Tuple[int, Dict]:
        """
        获取 Plc 状态

        """
        return self.request_sync(
            request=requests.get,
            api="/api/deviceInfo/plcStatus",
            body={"params": dict(device_id=device_id)},
            resp_model=None,
        )

    async def SetPileInfoReport(
        self, body: SetPileInfoSchemas
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置充电桩信息

        """
        return await self.request(
            request=async_post,
            api="/api/deviceInfo/PileInfo/SetPileInfoReport",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def SetPileInfoReport_sync(
        self, body: SetPileInfoSchemas
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置充电桩信息

        """
        return self.request_sync(
            request=requests.post,
            api="/api/deviceInfo/PileInfo/SetPileInfoReport",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def getPileInfoReport(self, body: GetPileInfoSchemas) -> Tuple[int, Dict]:
        """
        获取充电桩

        """
        return await self.request(
            request=async_post,
            api="/api/deviceInfo/PileInfo/getPileInfoReport",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def getPileInfoReport_sync(self, body: GetPileInfoSchemas) -> Tuple[int, Dict]:
        """
        获取充电桩

        """
        return self.request_sync(
            request=requests.post,
            api="/api/deviceInfo/PileInfo/getPileInfoReport",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    async def SetPileInfoAllCodeReport(
        self, body: SetPileInfoAllSchemas
    ) -> Tuple[int, Dict]:
        """
        设置所有充电桩开关

        """
        return await self.request(
            request=async_post,
            api="/api/deviceInfo/PileInfo/SetPileInfoAllCodeReport",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def SetPileInfoAllCodeReport_sync(
        self, body: SetPileInfoAllSchemas
    ) -> Tuple[int, Dict]:
        """
        设置所有充电桩开关

        """
        return self.request_sync(
            request=requests.post,
            api="/api/deviceInfo/PileInfo/SetPileInfoAllCodeReport",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    async def GetPileInfoAllCodeReport(self) -> Tuple[int, Dict]:
        """
        获取所有充电桩开关

        """
        return await self.request(
            request=async_get,
            api="/api/deviceInfo/PileInfo/GetPileInfoAllCodeReport",
            body={},
            resp_model=None,
        )

    def GetPileInfoAllCodeReport_sync(self) -> Tuple[int, Dict]:
        """
        获取所有充电桩开关

        """
        return self.request_sync(
            request=requests.get,
            api="/api/deviceInfo/PileInfo/GetPileInfoAllCodeReport",
            body={},
            resp_model=None,
        )

    async def PileMessage(self, body: PileMessageSchemas) -> Tuple[int, Dict]:
        """
        充电故障原因

        """
        return await self.request(
            request=async_post,
            api="/api/deviceInfo/PileInfo/PileMessage",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def PileMessage_sync(self, body: PileMessageSchemas) -> Tuple[int, Dict]:
        """
        充电故障原因

        """
        return self.request_sync(
            request=requests.post,
            api="/api/deviceInfo/PileInfo/PileMessage",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    async def PileMessageGet(self) -> Tuple[int, Dict]:
        """
        充电故障原因查询

        """
        return await self.request(
            request=async_get,
            api="/api/deviceInfo/PileInfo/PileMessageGet",
            body={},
            resp_model=None,
        )

    def PileMessageGet_sync(self) -> Tuple[int, Dict]:
        """
        充电故障原因查询

        """
        return self.request_sync(
            request=requests.get,
            api="/api/deviceInfo/PileInfo/PileMessageGet",
            body={},
            resp_model=None,
        )

    async def arriveTg(self, body: object) -> Tuple[int, Dict]:
        """
        外集卡到达 Tg 区域

        """
        return await self.request(
            request=async_post,
            api="/api/deviceInfo/externalTruck/arriveTg",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def arriveTg_sync(self, body: object) -> Tuple[int, Dict]:
        """
        外集卡到达 Tg 区域

        """
        return self.request_sync(
            request=requests.post,
            api="/api/deviceInfo/externalTruck/arriveTg",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    async def leaveTg(self, body: object) -> Tuple[int, Dict]:
        """
        外集卡离开 Tg 区域

        """
        return await self.request(
            request=async_post,
            api="/api/deviceInfo/externalTruck/leaveTg",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def leaveTg_sync(self, body: object) -> Tuple[int, Dict]:
        """
        外集卡离开 Tg 区域

        """
        return self.request_sync(
            request=requests.post,
            api="/api/deviceInfo/externalTruck/leaveTg",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    async def SetmultiCarEmergencyStop(self, body: object) -> Tuple[int, Dict]:
        """
        设置物理急停状态

        """
        return await self.request(
            request=async_post,
            api="/api/deviceInfo/emergency_status/SetmultiCarEmergencyStop",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def SetmultiCarEmergencyStop_sync(self, body: object) -> Tuple[int, Dict]:
        """
        设置物理急停状态

        """
        return self.request_sync(
            request=requests.post,
            api="/api/deviceInfo/emergency_status/SetmultiCarEmergencyStop",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    async def GetmultiCarEmergencyStop(self) -> Tuple[int, Dict]:
        """
        获取物理急停状态

        """
        return await self.request(
            request=async_get,
            api="/api/deviceInfo/emergency_status/GetmultiCarEmergencyStop",
            body={},
            resp_model=None,
        )

    def GetmultiCarEmergencyStop_sync(self) -> Tuple[int, Dict]:
        """
        获取物理急停状态

        """
        return self.request_sync(
            request=requests.get,
            api="/api/deviceInfo/emergency_status/GetmultiCarEmergencyStop",
            body={},
            resp_model=None,
        )


DeviceInfoRequest = DeviceInfoRequestCls()
