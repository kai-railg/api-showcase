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

from ..schemas.device_info import *

FMS_IP_ADDRESS = f"http://{os.environ.get('FMS_IP_ADDRESS', '127.0.0.1')}"


class Device_InfoRequest(object):
    url = FMS_IP_ADDRESS + ":" + "11000"
    
    @classmethod
    async def api_deviceInfo_maintain_status_post(cls) -> Tuple[int, Dict]:
        """
        Service Status
        
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/maintain/status"
            ),
            
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/maintain/status, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def api_deviceInfo_maintain_start_tracemalloc_get(cls) -> Tuple[int, Dict]:
        """
        Service Status
        
        """
        resp = await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/maintain/start_tracemalloc"
            ),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/maintain/start_tracemalloc, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def api_deviceInfo_maintain_stop_tracemalloc_get(cls) -> Tuple[int, Dict]:
        """
        Service Status
        
        """
        resp = await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/maintain/stop_tracemalloc"
            ),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/maintain/stop_tracemalloc, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def api_deviceInfo_maintain_get_tracemalloc_get(cls) -> Tuple[int, Dict]:
        """
        Service Status
        
        """
        resp = await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/maintain/get_tracemalloc"
            ),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/maintain/get_tracemalloc, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def deleteVehicle(cls, vehicle_id: str) -> Tuple[int, Dict]:
        """
        删除某个车辆的所有信息
        
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/maintain/deleteVehicle"
            ),
            
            params=dict(vehicle_id=vehicle_id)
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/maintain/deleteVehicle, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def deleteTg(cls) -> Tuple[int, Dict]:
        """
        删除拖挂信息
        
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/maintain/deleteTg"
            ),
            
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/maintain/deleteTg, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def vehicleDetails(cls, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取车辆详情
        
        """
        resp = await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/vehicleDetails"
            ),
            params=dict(vehicle_id=vehicle_id)
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/vehicleStatus/vehicleDetails, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def api_deviceInfo_vehicleStatus_vehicleDetails_post(cls, vehicle_id: str, vehicle_type: VehicleType, vin: str, color: str, manufacturer: str, engine_type: str) -> Tuple[int, Dict]:
        """
        设置车辆详情
        
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/vehicleDetails"
            ),
            
            params=dict(vehicle_id=vehicle_id, vehicle_type=vehicle_type, vin=vin, color=color, manufacturer=manufacturer, engine_type=engine_type)
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/vehicleStatus/vehicleDetails, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def LoginStatus(cls, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取单车登录状态
        
        """
        resp = await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/LoginStatus"
            ),
            params=dict(vehicle_id=vehicle_id)
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/vehicleStatus/LoginStatus, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def api_deviceInfo_vehicleStatus_LoginStatus_post(cls, body: SetLoginStatusPost) -> Tuple[int, Dict]:
        """
        设置单车登录状态
        
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/LoginStatus"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/vehicleStatus/LoginStatus, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def api_deviceInfo_vehicleStatus_mode_get(cls, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取单车模式
        
        """
        resp = await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/mode"
            ),
            params=dict(vehicle_id=vehicle_id)
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/vehicleStatus/mode, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def api_deviceInfo_vehicleStatus_mode_post(cls, body: SetModePost) -> Tuple[int, Dict]:
        """
        设置单车模式
        
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/mode"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/vehicleStatus/mode, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def bsm(cls, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取单车坐标
        
        """
        resp = await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/bsm"
            ),
            params=dict(vehicle_id=vehicle_id)
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/vehicleStatus/bsm, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def soc(cls, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取单车电量
        
        """
        resp = await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/soc"
            ),
            params=dict(vehicle_id=vehicle_id)
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/vehicleStatus/soc, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def api_deviceInfo_vehicleStatus_soc_post(cls, body: SetSocPost) -> Tuple[int, Dict]:
        """
        设置单车电量
        
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/soc"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/vehicleStatus/soc, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def longPath(cls, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取长路径
        
        """
        resp = await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/longPath"
            ),
            params=dict(vehicle_id=vehicle_id)
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/vehicleStatus/longPath, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def api_deviceInfo_vehicleStatus_longPath_post(cls, body: SetLongPath) -> Tuple[int, Dict]:
        """
        设置长路径
        
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/longPath"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/vehicleStatus/longPath, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def shortPath(cls, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取短路径
        
        """
        resp = await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/shortPath"
            ),
            params=dict(vehicle_id=vehicle_id)
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/vehicleStatus/shortPath, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def api_deviceInfo_vehicleStatus_shortPath_post(cls, body: SetShortPath) -> Tuple[int, Dict]:
        """
        设置短路径
        
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/shortPath"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/vehicleStatus/shortPath, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def suspend(cls, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取单车急停状态
        
        """
        resp = await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/suspend"
            ),
            params=dict(vehicle_id=vehicle_id)
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/vehicleStatus/suspend, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def api_deviceInfo_vehicleStatus_suspend_post(cls, body: object) -> Tuple[int, Dict]:
        """
        设置单车急停状态
        
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/suspend"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/vehicleStatus/suspend, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def api_deviceInfo_vehicleStatus_trailerStatus_get(cls, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取单车拖挂状态
        
        """
        resp = await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/trailerStatus"
            ),
            params=dict(vehicle_id=vehicle_id)
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/vehicleStatus/trailerStatus, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def api_deviceInfo_vehicleStatus_trailerStatus_post(cls, body: SetTrailerStatusPost) -> Tuple[int, Dict]:
        """
        设置单车拖挂状态
        
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/trailerStatus"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/vehicleStatus/trailerStatus, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def ghostVehicle(cls, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取幽灵车状态
        
        """
        resp = await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/ghostVehicle"
            ),
            params=dict(vehicle_id=vehicle_id)
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/vehicleStatus/ghostVehicle, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def api_deviceInfo_vehicleStatus_ghostVehicle_post(cls, body: SetGhostVehiclePost) -> Tuple[int, Dict]:
        """
        设置幽灵车状态
        
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/ghostVehicle"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/vehicleStatus/ghostVehicle, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def api_deviceInfo_vehicleStatus_ghostVehicleCancel_post(cls, body: SetGhostVehicleCancelPost) -> Tuple[int, Dict]:
        """
        设置幽灵车取消状态
        
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/ghostVehicleCancel"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/vehicleStatus/ghostVehicleCancel, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def getVehicleChassis(cls, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取车辆底盘信息
        
        """
        resp = await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/getVehicleChassis"
            ),
            params=dict(vehicle_id=vehicle_id)
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/vehicleStatus/getVehicleChassis, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def getVehicleAscChassis(cls, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取跨运车底盘信息
        
        """
        resp = await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/getVehicleAscChassis"
            ),
            params=dict(vehicle_id=vehicle_id)
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/vehicleStatus/getVehicleAscChassis, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def getVehiclesys(cls, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取车辆系统信息
        
        """
        resp = await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/getVehiclesys"
            ),
            params=dict(vehicle_id=vehicle_id)
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/vehicleStatus/getVehiclesys, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def api_deviceInfo_vehicleStatus_SetOperation_post(cls, body: object) -> Tuple[int, Dict]:
        """
        设置Operation状态
        
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/SetOperation"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/vehicleStatus/SetOperation, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def Operation(cls, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取Operation状态
        
        """
        resp = await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/Operation"
            ),
            params=dict(vehicle_id=vehicle_id)
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/vehicleStatus/Operation, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def SuspendReasonReport(cls, body: ReportSuspend) -> Tuple[int, Dict]:
        """
        报告车辆停止原因
        
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/SuspendReasonReport"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/vehicleStatus/SuspendReasonReport, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def SuspendReason(cls, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取车辆停止原因
        
        """
        resp = await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/SuspendReason"
            ),
            params=dict(vehicle_id=vehicle_id)
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/vehicleStatus/SuspendReason, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def StopTime(cls, body: ReportStopTime) -> Tuple[int, Dict]:
        """
        报告车辆停车时长
        
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/StopTime"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/vehicleStatus/StopTime, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def CurrentStatus(cls) -> Tuple[int, Dict]:
        """
        获取所有车辆的当前状态信息
        
        """
        resp = await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/CurrentStatus"
            ),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/vehicleStatus/CurrentStatus, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def BtnStatus(cls, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取急停，左驻车，右驻车的按钮状态
        
        """
        resp = await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/BtnStatus"
            ),
            params=dict(vehicle_id=vehicle_id)
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/vehicleStatus/BtnStatus, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def api_deviceInfo_vehicleStatus_BtnStatus_post(cls, body: BtnStatusSchemas,vehicle_id: str) -> Tuple[int, Dict]:
        """
        设置急停，左驻车，右驻车的按钮状态
        
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/BtnStatus"
            ),
            json=body.dict(),
            params=dict(vehicle_id=vehicle_id)
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/vehicleStatus/BtnStatus, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def craneStatus(cls, device_id: str, vehicle_id: str, lane: str, block: str, stack: str) -> Tuple[int, Dict]:
        """
        获取 Crane 状态
        
        """
        resp = await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/craneStatus/"
            ),
            params=dict(device_id=device_id, vehicle_id=vehicle_id, lane=lane, block=block, stack=stack)
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/craneStatus/, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def lane(cls, lane: str) -> Tuple[int, Dict]:
        """
        获取车道Y
        
        """
        resp = await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/craneStatus/lane"
            ),
            params=dict(lane=lane)
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/craneStatus/lane, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def craneList(cls, feild_get: str) -> Tuple[int, Dict]:
        """
        获取 Crane 列表
        
        """
        resp = await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/craneStatus/craneList"
            ),
            params=dict(feild_get=feild_get)
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/craneStatus/craneList, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def plcStatus(cls, device_id: str) -> Tuple[int, Dict]:
        """
        获取 Plc 状态
        
        """
        resp = await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/plcStatus"
            ),
            params=dict(device_id=device_id)
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/plcStatus, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def SetPileInfoReport(cls, body: SetPileInfoSchemas) -> Tuple[int, Dict]:
        """
        设置充电桩信息
        
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/PileInfo/SetPileInfoReport"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/PileInfo/SetPileInfoReport, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def getPileInfoReport(cls, body: GetPileInfoSchemas) -> Tuple[int, Dict]:
        """
        获取充电桩
        
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/PileInfo/getPileInfoReport"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/PileInfo/getPileInfoReport, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def SetPileInfoAllCodeReport(cls, body: SetPileInfoAllSchemas) -> Tuple[int, Dict]:
        """
        设置所有充电桩开关
        
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/PileInfo/SetPileInfoAllCodeReport"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/PileInfo/SetPileInfoAllCodeReport, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def GetPileInfoAllCodeReport(cls) -> Tuple[int, Dict]:
        """
        获取所有充电桩开关
        
        """
        resp = await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/PileInfo/GetPileInfoAllCodeReport"
            ),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/PileInfo/GetPileInfoAllCodeReport, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def PileMessage(cls, body: PileMessageSchemas) -> Tuple[int, Dict]:
        """
        充电故障原因
        
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/PileInfo/PileMessage"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/PileInfo/PileMessage, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def PileMessageGet(cls) -> Tuple[int, Dict]:
        """
        充电故障原因查询
        
        """
        resp = await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/PileInfo/PileMessageGet"
            ),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/PileInfo/PileMessageGet, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def arriveTg(cls, body: object) -> Tuple[int, Dict]:
        """
        外集卡到达 Tg 区域
        
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/externalTruck/arriveTg"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/externalTruck/arriveTg, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def leaveTg(cls, body: object) -> Tuple[int, Dict]:
        """
        外集卡离开 Tg 区域
        
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/externalTruck/leaveTg"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/externalTruck/leaveTg, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def SetmultiCarEmergencyStop(cls, body: object) -> Tuple[int, Dict]:
        """
        设置物理急停状态
        
        """
        resp = await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/emergency_status/SetmultiCarEmergencyStop"
            ),
            json=body.dict(),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/emergency_status/SetmultiCarEmergencyStop, response: {resp.text}")
        return resp.status, resp.json()
        
    @classmethod
    async def GetmultiCarEmergencyStop(cls) -> Tuple[int, Dict]:
        """
        获取物理急停状态
        
        """
        resp = await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/emergency_status/GetmultiCarEmergencyStop"
            ),
            
        )
        if resp.status != 200:
            print(f"Request failed: {resp.status}, url: {cls.url}, api: /api/deviceInfo/emergency_status/GetmultiCarEmergencyStop, response: {resp.text}")
        return resp.status, resp.json()
        