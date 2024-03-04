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

from ..schemas.device_info import *

FMS_IP_ADDRESS = f"http://{os.environ.get('FMS_IP_ADDRESS', '127.0.0.1')}"


class Device_InfoRequest(object):
    url = FMS_IP_ADDRESS + ":" + "11000"
    
    @classmethod
    async def api_deviceInfo_maintain_status_post(cls, ) -> AsyncHttpResponse:
        """
        Service Status
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/maintain/status"
            ),
            
            
        )
         
    @classmethod
    async def api_deviceInfo_maintain_start_tracemalloc_get(cls, ) -> AsyncHttpResponse:
        """
        Service Status
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/maintain/start_tracemalloc"
            ),
            
        )
         
    @classmethod
    async def api_deviceInfo_maintain_stop_tracemalloc_get(cls, ) -> AsyncHttpResponse:
        """
        Service Status
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/maintain/stop_tracemalloc"
            ),
            
        )
         
    @classmethod
    async def api_deviceInfo_maintain_get_tracemalloc_get(cls, ) -> AsyncHttpResponse:
        """
        Service Status
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/maintain/get_tracemalloc"
            ),
            
        )
         
    @classmethod
    async def deleteVehicle(cls, vehicle_id: str) -> AsyncHttpResponse:
        """
        删除某个车辆的所有信息
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/maintain/deleteVehicle"
            ),
            
            params=dict(vehicle_id=vehicle_id)
        )
         
    @classmethod
    async def deleteTg(cls, ) -> AsyncHttpResponse:
        """
        删除拖挂信息
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/maintain/deleteTg"
            ),
            
            
        )
         
    @classmethod
    async def vehicleDetails(cls, vehicle_id: str) -> AsyncHttpResponse:
        """
        获取车辆详情
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/vehicleDetails"
            ),
            params=dict(vehicle_id=vehicle_id)
        )
         
    @classmethod
    async def api_deviceInfo_vehicleStatus_vehicleDetails_post(cls, vehicle_id: str, vehicle_type: VehicleType, vin: str, color: str, manufacturer: str, engine_type: str) -> AsyncHttpResponse:
        """
        设置车辆详情
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/vehicleDetails"
            ),
            
            params=dict(vehicle_id=vehicle_id, vehicle_type=vehicle_type, vin=vin, color=color, manufacturer=manufacturer, engine_type=engine_type)
        )
         
    @classmethod
    async def LoginStatus(cls, vehicle_id: str) -> AsyncHttpResponse:
        """
        获取单车登录状态
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/LoginStatus"
            ),
            params=dict(vehicle_id=vehicle_id)
        )
         
    @classmethod
    async def api_deviceInfo_vehicleStatus_LoginStatus_post(cls, body: SetLoginStatusPost) -> AsyncHttpResponse:
        """
        设置单车登录状态
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/LoginStatus"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def api_deviceInfo_vehicleStatus_mode_get(cls, vehicle_id: str) -> AsyncHttpResponse:
        """
        获取单车模式
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/mode"
            ),
            params=dict(vehicle_id=vehicle_id)
        )
         
    @classmethod
    async def api_deviceInfo_vehicleStatus_mode_post(cls, body: SetModePost) -> AsyncHttpResponse:
        """
        设置单车模式
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/mode"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def bsm(cls, vehicle_id: str) -> AsyncHttpResponse:
        """
        获取单车坐标
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/bsm"
            ),
            params=dict(vehicle_id=vehicle_id)
        )
         
    @classmethod
    async def soc(cls, vehicle_id: str) -> AsyncHttpResponse:
        """
        获取单车电量
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/soc"
            ),
            params=dict(vehicle_id=vehicle_id)
        )
         
    @classmethod
    async def api_deviceInfo_vehicleStatus_soc_post(cls, body: SetSocPost) -> AsyncHttpResponse:
        """
        设置单车电量
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/soc"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def longPath(cls, vehicle_id: str) -> AsyncHttpResponse:
        """
        获取长路径
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/longPath"
            ),
            params=dict(vehicle_id=vehicle_id)
        )
         
    @classmethod
    async def api_deviceInfo_vehicleStatus_longPath_post(cls, body: SetLongPath) -> AsyncHttpResponse:
        """
        设置长路径
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/longPath"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def shortPath(cls, vehicle_id: str) -> AsyncHttpResponse:
        """
        获取短路径
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/shortPath"
            ),
            params=dict(vehicle_id=vehicle_id)
        )
         
    @classmethod
    async def api_deviceInfo_vehicleStatus_shortPath_post(cls, body: SetShortPath) -> AsyncHttpResponse:
        """
        设置短路径
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/shortPath"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def suspend(cls, vehicle_id: str) -> AsyncHttpResponse:
        """
        获取单车急停状态
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/suspend"
            ),
            params=dict(vehicle_id=vehicle_id)
        )
         
    @classmethod
    async def api_deviceInfo_vehicleStatus_suspend_post(cls, body: object) -> AsyncHttpResponse:
        """
        设置单车急停状态
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/suspend"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def api_deviceInfo_vehicleStatus_trailerStatus_get(cls, vehicle_id: str) -> AsyncHttpResponse:
        """
        获取单车拖挂状态
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/trailerStatus"
            ),
            params=dict(vehicle_id=vehicle_id)
        )
         
    @classmethod
    async def api_deviceInfo_vehicleStatus_trailerStatus_post(cls, body: SetTrailerStatusPost) -> AsyncHttpResponse:
        """
        设置单车拖挂状态
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/trailerStatus"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def ghostVehicle(cls, vehicle_id: str) -> AsyncHttpResponse:
        """
        获取幽灵车状态
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/ghostVehicle"
            ),
            params=dict(vehicle_id=vehicle_id)
        )
         
    @classmethod
    async def api_deviceInfo_vehicleStatus_ghostVehicle_post(cls, body: SetGhostVehiclePost) -> AsyncHttpResponse:
        """
        设置幽灵车状态
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/ghostVehicle"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def api_deviceInfo_vehicleStatus_ghostVehicleCancel_post(cls, body: SetGhostVehicleCancelPost) -> AsyncHttpResponse:
        """
        设置幽灵车取消状态
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/ghostVehicleCancel"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def getVehicleChassis(cls, vehicle_id: str) -> AsyncHttpResponse:
        """
        获取车辆底盘信息
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/getVehicleChassis"
            ),
            params=dict(vehicle_id=vehicle_id)
        )
         
    @classmethod
    async def getVehicleAscChassis(cls, vehicle_id: str) -> AsyncHttpResponse:
        """
        获取跨运车底盘信息
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/getVehicleAscChassis"
            ),
            params=dict(vehicle_id=vehicle_id)
        )
         
    @classmethod
    async def getVehiclesys(cls, vehicle_id: str) -> AsyncHttpResponse:
        """
        获取车辆系统信息
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/getVehiclesys"
            ),
            params=dict(vehicle_id=vehicle_id)
        )
         
    @classmethod
    async def api_deviceInfo_vehicleStatus_SetOperation_post(cls, body: object) -> AsyncHttpResponse:
        """
        设置Operation状态
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/SetOperation"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def Operation(cls, vehicle_id: str) -> AsyncHttpResponse:
        """
        获取Operation状态
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/Operation"
            ),
            params=dict(vehicle_id=vehicle_id)
        )
         
    @classmethod
    async def SuspendReasonReport(cls, body: ReportSuspend) -> AsyncHttpResponse:
        """
        报告车辆停止原因
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/SuspendReasonReport"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def SuspendReason(cls, vehicle_id: str) -> AsyncHttpResponse:
        """
        获取车辆停止原因
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/SuspendReason"
            ),
            params=dict(vehicle_id=vehicle_id)
        )
         
    @classmethod
    async def StopTime(cls, body: ReportStopTime) -> AsyncHttpResponse:
        """
        报告车辆停车时长
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/StopTime"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def CurrentStatus(cls, ) -> AsyncHttpResponse:
        """
        获取所有车辆的当前状态信息
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/CurrentStatus"
            ),
            
        )
         
    @classmethod
    async def BtnStatus(cls, vehicle_id: str) -> AsyncHttpResponse:
        """
        获取急停，左驻车，右驻车的按钮状态
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/BtnStatus"
            ),
            params=dict(vehicle_id=vehicle_id)
        )
         
    @classmethod
    async def api_deviceInfo_vehicleStatus_BtnStatus_post(cls, body: BtnStatusSchemas,vehicle_id: str) -> AsyncHttpResponse:
        """
        设置急停，左驻车，右驻车的按钮状态
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/BtnStatus"
            ),
            json=body.dict(),
            params=dict(vehicle_id=vehicle_id)
        )
         
    @classmethod
    async def craneStatus(cls, device_id: str, vehicle_id: str, lane: str, block: str, stack: str) -> AsyncHttpResponse:
        """
        获取 Crane 状态
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/craneStatus/"
            ),
            params=dict(device_id=device_id, vehicle_id=vehicle_id, lane=lane, block=block, stack=stack)
        )
         
    @classmethod
    async def lane(cls, lane: str) -> AsyncHttpResponse:
        """
        获取车道Y
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/craneStatus/lane"
            ),
            params=dict(lane=lane)
        )
         
    @classmethod
    async def craneList(cls, feild_get: str) -> AsyncHttpResponse:
        """
        获取 Crane 列表
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/craneStatus/craneList"
            ),
            params=dict(feild_get=feild_get)
        )
         
    @classmethod
    async def plcStatus(cls, device_id: str) -> AsyncHttpResponse:
        """
        获取 Plc 状态
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/plcStatus"
            ),
            params=dict(device_id=device_id)
        )
         
    @classmethod
    async def SetPileInfoReport(cls, body: SetPileInfoSchemas) -> AsyncHttpResponse:
        """
        设置充电桩信息
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/PileInfo/SetPileInfoReport"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def getPileInfoReport(cls, body: GetPileInfoSchemas) -> AsyncHttpResponse:
        """
        获取充电桩
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/PileInfo/getPileInfoReport"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def SetPileInfoAllCodeReport(cls, body: SetPileInfoAllSchemas) -> AsyncHttpResponse:
        """
        设置所有充电桩开关
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/PileInfo/SetPileInfoAllCodeReport"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def GetPileInfoAllCodeReport(cls, ) -> AsyncHttpResponse:
        """
        获取所有充电桩开关
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/PileInfo/GetPileInfoAllCodeReport"
            ),
            
        )
         
    @classmethod
    async def PileMessage(cls, body: PileMessageSchemas) -> AsyncHttpResponse:
        """
        充电故障原因
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/PileInfo/PileMessage"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def PileMessageGet(cls, ) -> AsyncHttpResponse:
        """
        充电故障原因查询
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/PileInfo/PileMessageGet"
            ),
            
        )
         
    @classmethod
    async def arriveTg(cls, body: object) -> AsyncHttpResponse:
        """
        外集卡到达 Tg 区域
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/externalTruck/arriveTg"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def leaveTg(cls, body: object) -> AsyncHttpResponse:
        """
        外集卡离开 Tg 区域
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/externalTruck/leaveTg"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def SetmultiCarEmergencyStop(cls, body: object) -> AsyncHttpResponse:
        """
        设置物理急停状态
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/emergency_status/SetmultiCarEmergencyStop"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def GetmultiCarEmergencyStop(cls, ) -> AsyncHttpResponse:
        """
        获取物理急停状态
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/emergency_status/GetmultiCarEmergencyStop"
            ),
            
        )
         