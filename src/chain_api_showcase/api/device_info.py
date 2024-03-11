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
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/deviceInfo/maintain/status"),
            timeout=self.timeout,
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/maintain/status, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def api_deviceInfo_maintain_status_post_sync(self) -> Tuple[int, Dict]:
        """
        Service Status

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/deviceInfo/maintain/status"),
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/maintain/status, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def api_deviceInfo_maintain_start_tracemalloc_get(self) -> Tuple[int, Dict]:
        """
        Service Status

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/deviceInfo/maintain/start_tracemalloc"),
            timeout=self.timeout,
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/maintain/start_tracemalloc, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def api_deviceInfo_maintain_start_tracemalloc_get_sync(self) -> Tuple[int, Dict]:
        """
        Service Status

        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/api/deviceInfo/maintain/start_tracemalloc"),
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/maintain/start_tracemalloc, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def api_deviceInfo_maintain_stop_tracemalloc_get(self) -> Tuple[int, Dict]:
        """
        Service Status

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/deviceInfo/maintain/stop_tracemalloc"),
            timeout=self.timeout,
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/maintain/stop_tracemalloc, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def api_deviceInfo_maintain_stop_tracemalloc_get_sync(self) -> Tuple[int, Dict]:
        """
        Service Status

        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/api/deviceInfo/maintain/stop_tracemalloc"),
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/maintain/stop_tracemalloc, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def api_deviceInfo_maintain_get_tracemalloc_get(self) -> Tuple[int, Dict]:
        """
        Service Status

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/deviceInfo/maintain/get_tracemalloc"),
            timeout=self.timeout,
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/maintain/get_tracemalloc, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def api_deviceInfo_maintain_get_tracemalloc_get_sync(self) -> Tuple[int, Dict]:
        """
        Service Status

        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/api/deviceInfo/maintain/get_tracemalloc"),
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/maintain/get_tracemalloc, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def deleteVehicle(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        删除某个车辆的所有信息

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/deviceInfo/maintain/deleteVehicle"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/maintain/deleteVehicle, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def deleteVehicle_sync(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        删除某个车辆的所有信息

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/deviceInfo/maintain/deleteVehicle"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/maintain/deleteVehicle, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def deleteTg(self) -> Tuple[int, Dict]:
        """
        删除拖挂信息

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/deviceInfo/maintain/deleteTg"),
            timeout=self.timeout,
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/maintain/deleteTg, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def deleteTg_sync(self) -> Tuple[int, Dict]:
        """
        删除拖挂信息

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/deviceInfo/maintain/deleteTg"),
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/maintain/deleteTg, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def vehicleDetails(self, vehicle_id: str) -> Tuple[int, CreateSuccessSchema]:
        """
        获取车辆详情

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/vehicleDetails"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/vehicleDetails, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    def vehicleDetails_sync(self, vehicle_id: str) -> Tuple[int, CreateSuccessSchema]:
        """
        获取车辆详情

        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/vehicleDetails"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/vehicleDetails, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, CreateSuccessSchema.model_validate_json(resp)

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
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/vehicleDetails"),
            timeout=self.timeout,
            params=dict(
                vehicle_id=vehicle_id,
                vehicle_type=vehicle_type,
                vin=vin,
                color=color,
                manufacturer=manufacturer,
                engine_type=engine_type,
            ),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/vehicleDetails, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

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
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/vehicleDetails"),
            timeout=self.timeout,
            params=dict(
                vehicle_id=vehicle_id,
                vehicle_type=vehicle_type,
                vin=vin,
                color=color,
                manufacturer=manufacturer,
                engine_type=engine_type,
            ),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/vehicleDetails, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, CreateSuccessSchema.model_validate_json(resp)

    async def LoginStatus(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取单车登录状态

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/LoginStatus"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/LoginStatus, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def LoginStatus_sync(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取单车登录状态

        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/LoginStatus"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/LoginStatus, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def api_deviceInfo_vehicleStatus_LoginStatus_post(
        self, body: SetLoginStatusPost
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置单车登录状态

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/LoginStatus"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/LoginStatus, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    def api_deviceInfo_vehicleStatus_LoginStatus_post_sync(
        self, body: SetLoginStatusPost
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置单车登录状态

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/LoginStatus"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/LoginStatus, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, CreateSuccessSchema.model_validate_json(resp)

    async def api_deviceInfo_vehicleStatus_mode_get(
        self, vehicle_id: str
    ) -> Tuple[int, Dict]:
        """
        获取单车模式

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/mode"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/mode, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def api_deviceInfo_vehicleStatus_mode_get_sync(
        self, vehicle_id: str
    ) -> Tuple[int, Dict]:
        """
        获取单车模式

        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/mode"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/mode, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def api_deviceInfo_vehicleStatus_mode_post(
        self, body: SetModePost
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置单车模式

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/mode"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/mode, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    def api_deviceInfo_vehicleStatus_mode_post_sync(
        self, body: SetModePost
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置单车模式

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/mode"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/mode, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, CreateSuccessSchema.model_validate_json(resp)

    async def bsm(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取单车坐标

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/bsm"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/bsm, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def bsm_sync(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取单车坐标

        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/bsm"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/bsm, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def api_deviceInfo_vehicleStatus_bsm_post(
        self, body: object
    ) -> Tuple[int, Dict]:
        """
        设置单车坐标

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/bsm"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/bsm, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def api_deviceInfo_vehicleStatus_bsm_post_sync(
        self, body: object
    ) -> Tuple[int, Dict]:
        """
        设置单车坐标

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/bsm"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/bsm, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def soc(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取单车电量

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/soc"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/soc, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def soc_sync(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取单车电量

        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/soc"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/soc, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def api_deviceInfo_vehicleStatus_soc_post(
        self, body: SetSocPost
    ) -> Tuple[int, Dict]:
        """
        设置单车电量

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/soc"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/soc, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def api_deviceInfo_vehicleStatus_soc_post_sync(
        self, body: SetSocPost
    ) -> Tuple[int, Dict]:
        """
        设置单车电量

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/soc"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/soc, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def longPath(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取长路径

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/longPath"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/longPath, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def longPath_sync(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取长路径

        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/longPath"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/longPath, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def api_deviceInfo_vehicleStatus_longPath_post(
        self, body: SetLongPath
    ) -> Tuple[int, Dict]:
        """
        设置长路径

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/longPath"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/longPath, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def api_deviceInfo_vehicleStatus_longPath_post_sync(
        self, body: SetLongPath
    ) -> Tuple[int, Dict]:
        """
        设置长路径

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/longPath"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/longPath, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def shortPath(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取短路径

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/shortPath"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/shortPath, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def shortPath_sync(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取短路径

        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/shortPath"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/shortPath, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def api_deviceInfo_vehicleStatus_shortPath_post(
        self, body: SetShortPath
    ) -> Tuple[int, Dict]:
        """
        设置短路径

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/shortPath"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/shortPath, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def api_deviceInfo_vehicleStatus_shortPath_post_sync(
        self, body: SetShortPath
    ) -> Tuple[int, Dict]:
        """
        设置短路径

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/shortPath"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/shortPath, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def suspend(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取单车急停状态

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/suspend"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/suspend, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def suspend_sync(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取单车急停状态

        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/suspend"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/suspend, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def api_deviceInfo_vehicleStatus_suspend_post(
        self, body: object
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置单车急停状态

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/suspend"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/suspend, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    def api_deviceInfo_vehicleStatus_suspend_post_sync(
        self, body: object
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置单车急停状态

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/suspend"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/suspend, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, CreateSuccessSchema.model_validate_json(resp)

    async def api_deviceInfo_vehicleStatus_trailerStatus_get(
        self, vehicle_id: str
    ) -> Tuple[int, Dict]:
        """
        获取单车拖挂状态

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/trailerStatus"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/trailerStatus, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def api_deviceInfo_vehicleStatus_trailerStatus_get_sync(
        self, vehicle_id: str
    ) -> Tuple[int, Dict]:
        """
        获取单车拖挂状态

        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/trailerStatus"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/trailerStatus, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def api_deviceInfo_vehicleStatus_trailerStatus_post(
        self, body: SetTrailerStatusPost
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置单车拖挂状态

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/trailerStatus"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/trailerStatus, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    def api_deviceInfo_vehicleStatus_trailerStatus_post_sync(
        self, body: SetTrailerStatusPost
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置单车拖挂状态

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/trailerStatus"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/trailerStatus, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, CreateSuccessSchema.model_validate_json(resp)

    async def ghostVehicle(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取幽灵车状态

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/ghostVehicle"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/ghostVehicle, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def ghostVehicle_sync(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取幽灵车状态

        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/ghostVehicle"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/ghostVehicle, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def api_deviceInfo_vehicleStatus_ghostVehicle_post(
        self, body: SetGhostVehiclePost
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置幽灵车状态

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/ghostVehicle"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/ghostVehicle, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    def api_deviceInfo_vehicleStatus_ghostVehicle_post_sync(
        self, body: SetGhostVehiclePost
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置幽灵车状态

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/ghostVehicle"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/ghostVehicle, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, CreateSuccessSchema.model_validate_json(resp)

    async def api_deviceInfo_vehicleStatus_ghostVehicleCancel_post(
        self, body: SetGhostVehicleCancelPost
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置幽灵车取消状态

        """
        resp = await async_post(
            url=parse.urljoin(
                self.url, "/api/deviceInfo/vehicleStatus/ghostVehicleCancel"
            ),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/ghostVehicleCancel, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    def api_deviceInfo_vehicleStatus_ghostVehicleCancel_post_sync(
        self, body: SetGhostVehicleCancelPost
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置幽灵车取消状态

        """
        resp = requests.post(
            url=parse.urljoin(
                self.url, "/api/deviceInfo/vehicleStatus/ghostVehicleCancel"
            ),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/ghostVehicleCancel, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, CreateSuccessSchema.model_validate_json(resp)

    async def getVehicleChassis(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取车辆底盘信息

        """
        resp = await async_get(
            url=parse.urljoin(
                self.url, "/api/deviceInfo/vehicleStatus/getVehicleChassis"
            ),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/getVehicleChassis, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def getVehicleChassis_sync(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取车辆底盘信息

        """
        resp = requests.get(
            url=parse.urljoin(
                self.url, "/api/deviceInfo/vehicleStatus/getVehicleChassis"
            ),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/getVehicleChassis, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def getVehicleAscChassis(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取跨运车底盘信息

        """
        resp = await async_get(
            url=parse.urljoin(
                self.url, "/api/deviceInfo/vehicleStatus/getVehicleAscChassis"
            ),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/getVehicleAscChassis, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def getVehicleAscChassis_sync(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取跨运车底盘信息

        """
        resp = requests.get(
            url=parse.urljoin(
                self.url, "/api/deviceInfo/vehicleStatus/getVehicleAscChassis"
            ),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/getVehicleAscChassis, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def getVehiclesys(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取车辆系统信息

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/getVehiclesys"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/getVehiclesys, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def getVehiclesys_sync(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取车辆系统信息

        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/getVehiclesys"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/getVehiclesys, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def api_deviceInfo_vehicleStatus_SetOperation_post(
        self, body: object
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置Operation状态

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/SetOperation"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/SetOperation, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    def api_deviceInfo_vehicleStatus_SetOperation_post_sync(
        self, body: object
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置Operation状态

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/SetOperation"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/SetOperation, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, CreateSuccessSchema.model_validate_json(resp)

    async def Operation(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取Operation状态

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/Operation"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/Operation, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def Operation_sync(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取Operation状态

        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/Operation"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/Operation, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def SuspendReasonReport(self, body: ReportSuspend) -> Tuple[int, Dict]:
        """
        报告车辆停止原因

        """
        resp = await async_post(
            url=parse.urljoin(
                self.url, "/api/deviceInfo/vehicleStatus/SuspendReasonReport"
            ),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/SuspendReasonReport, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def SuspendReasonReport_sync(self, body: ReportSuspend) -> Tuple[int, Dict]:
        """
        报告车辆停止原因

        """
        resp = requests.post(
            url=parse.urljoin(
                self.url, "/api/deviceInfo/vehicleStatus/SuspendReasonReport"
            ),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/SuspendReasonReport, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def SuspendReason(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取车辆停止原因

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/SuspendReason"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/SuspendReason, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def SuspendReason_sync(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取车辆停止原因

        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/SuspendReason"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/SuspendReason, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def StopTime(self, body: ReportStopTime) -> Tuple[int, Dict]:
        """
        报告车辆停车时长

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/StopTime"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/StopTime, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def StopTime_sync(self, body: ReportStopTime) -> Tuple[int, Dict]:
        """
        报告车辆停车时长

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/StopTime"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/StopTime, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def CurrentStatus(self) -> Tuple[int, Dict]:
        """
        获取所有车辆的当前状态信息

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/CurrentStatus"),
            timeout=self.timeout,
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/CurrentStatus, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def CurrentStatus_sync(self) -> Tuple[int, Dict]:
        """
        获取所有车辆的当前状态信息

        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/CurrentStatus"),
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/CurrentStatus, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def BtnStatus(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取急停，左驻车，右驻车的按钮状态

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/BtnStatus"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/BtnStatus, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def BtnStatus_sync(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取急停，左驻车，右驻车的按钮状态

        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/BtnStatus"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/BtnStatus, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def api_deviceInfo_vehicleStatus_BtnStatus_post(
        self, body: BtnStatusSchemas, vehicle_id: str
    ) -> Tuple[int, Dict]:
        """
        设置急停，左驻车，右驻车的按钮状态

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/BtnStatus"),
            timeout=self.timeout,
            data=body.model_dump_json(),
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/BtnStatus, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def api_deviceInfo_vehicleStatus_BtnStatus_post_sync(
        self, body: BtnStatusSchemas, vehicle_id: str
    ) -> Tuple[int, Dict]:
        """
        设置急停，左驻车，右驻车的按钮状态

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/BtnStatus"),
            timeout=self.timeout,
            data=body.model_dump_json(),
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/BtnStatus, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def craneStatus(
        self, device_id: str, vehicle_id: str, lane: str, block: str, stack: str
    ) -> Tuple[int, Dict]:
        """
        获取 Crane 状态

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/deviceInfo/craneStatus/"),
            timeout=self.timeout,
            params=dict(
                device_id=device_id,
                vehicle_id=vehicle_id,
                lane=lane,
                block=block,
                stack=stack,
            ),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/craneStatus/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def craneStatus_sync(
        self, device_id: str, vehicle_id: str, lane: str, block: str, stack: str
    ) -> Tuple[int, Dict]:
        """
        获取 Crane 状态

        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/api/deviceInfo/craneStatus/"),
            timeout=self.timeout,
            params=dict(
                device_id=device_id,
                vehicle_id=vehicle_id,
                lane=lane,
                block=block,
                stack=stack,
            ),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/craneStatus/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def lane(self, lane: str) -> Tuple[int, Dict]:
        """
        获取车道Y

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/deviceInfo/craneStatus/lane"),
            timeout=self.timeout,
            params=dict(lane=lane),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/craneStatus/lane, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def lane_sync(self, lane: str) -> Tuple[int, Dict]:
        """
        获取车道Y

        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/api/deviceInfo/craneStatus/lane"),
            timeout=self.timeout,
            params=dict(lane=lane),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/craneStatus/lane, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def craneList(self, feild_get: str = "min") -> Tuple[int, Dict]:
        """
        获取 Crane 列表

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/deviceInfo/craneStatus/craneList"),
            timeout=self.timeout,
            params=dict(feild_get=feild_get),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/craneStatus/craneList, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def craneList_sync(self, feild_get: str = "min") -> Tuple[int, Dict]:
        """
        获取 Crane 列表

        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/api/deviceInfo/craneStatus/craneList"),
            timeout=self.timeout,
            params=dict(feild_get=feild_get),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/craneStatus/craneList, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def plcStatus(self, device_id: str = "all") -> Tuple[int, Dict]:
        """
        获取 Plc 状态

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/deviceInfo/plcStatus"),
            timeout=self.timeout,
            params=dict(device_id=device_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/plcStatus, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def plcStatus_sync(self, device_id: str = "all") -> Tuple[int, Dict]:
        """
        获取 Plc 状态

        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/api/deviceInfo/plcStatus"),
            timeout=self.timeout,
            params=dict(device_id=device_id),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/plcStatus, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def SetPileInfoReport(
        self, body: SetPileInfoSchemas
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置充电桩信息

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/deviceInfo/PileInfo/SetPileInfoReport"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/PileInfo/SetPileInfoReport, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    def SetPileInfoReport_sync(
        self, body: SetPileInfoSchemas
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置充电桩信息

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/deviceInfo/PileInfo/SetPileInfoReport"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/PileInfo/SetPileInfoReport, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, CreateSuccessSchema.model_validate_json(resp)

    async def getPileInfoReport(self, body: GetPileInfoSchemas) -> Tuple[int, Dict]:
        """
        获取充电桩

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/deviceInfo/PileInfo/getPileInfoReport"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/PileInfo/getPileInfoReport, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def getPileInfoReport_sync(self, body: GetPileInfoSchemas) -> Tuple[int, Dict]:
        """
        获取充电桩

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/deviceInfo/PileInfo/getPileInfoReport"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/PileInfo/getPileInfoReport, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def SetPileInfoAllCodeReport(
        self, body: SetPileInfoAllSchemas
    ) -> Tuple[int, Dict]:
        """
        设置所有充电桩开关

        """
        resp = await async_post(
            url=parse.urljoin(
                self.url, "/api/deviceInfo/PileInfo/SetPileInfoAllCodeReport"
            ),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/PileInfo/SetPileInfoAllCodeReport, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def SetPileInfoAllCodeReport_sync(
        self, body: SetPileInfoAllSchemas
    ) -> Tuple[int, Dict]:
        """
        设置所有充电桩开关

        """
        resp = requests.post(
            url=parse.urljoin(
                self.url, "/api/deviceInfo/PileInfo/SetPileInfoAllCodeReport"
            ),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/PileInfo/SetPileInfoAllCodeReport, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def GetPileInfoAllCodeReport(self) -> Tuple[int, Dict]:
        """
        获取所有充电桩开关

        """
        resp = await async_get(
            url=parse.urljoin(
                self.url, "/api/deviceInfo/PileInfo/GetPileInfoAllCodeReport"
            ),
            timeout=self.timeout,
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/PileInfo/GetPileInfoAllCodeReport, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def GetPileInfoAllCodeReport_sync(self) -> Tuple[int, Dict]:
        """
        获取所有充电桩开关

        """
        resp = requests.get(
            url=parse.urljoin(
                self.url, "/api/deviceInfo/PileInfo/GetPileInfoAllCodeReport"
            ),
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/PileInfo/GetPileInfoAllCodeReport, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def PileMessage(self, body: PileMessageSchemas) -> Tuple[int, Dict]:
        """
        充电故障原因

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/deviceInfo/PileInfo/PileMessage"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/PileInfo/PileMessage, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def PileMessage_sync(self, body: PileMessageSchemas) -> Tuple[int, Dict]:
        """
        充电故障原因

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/deviceInfo/PileInfo/PileMessage"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/PileInfo/PileMessage, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def PileMessageGet(self) -> Tuple[int, Dict]:
        """
        充电故障原因查询

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/deviceInfo/PileInfo/PileMessageGet"),
            timeout=self.timeout,
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/PileInfo/PileMessageGet, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def PileMessageGet_sync(self) -> Tuple[int, Dict]:
        """
        充电故障原因查询

        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/api/deviceInfo/PileInfo/PileMessageGet"),
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/PileInfo/PileMessageGet, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def arriveTg(self, body: object) -> Tuple[int, Dict]:
        """
        外集卡到达 Tg 区域

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/deviceInfo/externalTruck/arriveTg"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/externalTruck/arriveTg, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def arriveTg_sync(self, body: object) -> Tuple[int, Dict]:
        """
        外集卡到达 Tg 区域

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/deviceInfo/externalTruck/arriveTg"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/externalTruck/arriveTg, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def leaveTg(self, body: object) -> Tuple[int, Dict]:
        """
        外集卡离开 Tg 区域

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/deviceInfo/externalTruck/leaveTg"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/externalTruck/leaveTg, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def leaveTg_sync(self, body: object) -> Tuple[int, Dict]:
        """
        外集卡离开 Tg 区域

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/deviceInfo/externalTruck/leaveTg"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/externalTruck/leaveTg, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def SetmultiCarEmergencyStop(self, body: object) -> Tuple[int, Dict]:
        """
        设置物理急停状态

        """
        resp = await async_post(
            url=parse.urljoin(
                self.url, "/api/deviceInfo/emergency_status/SetmultiCarEmergencyStop"
            ),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/emergency_status/SetmultiCarEmergencyStop, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def SetmultiCarEmergencyStop_sync(self, body: object) -> Tuple[int, Dict]:
        """
        设置物理急停状态

        """
        resp = requests.post(
            url=parse.urljoin(
                self.url, "/api/deviceInfo/emergency_status/SetmultiCarEmergencyStop"
            ),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/emergency_status/SetmultiCarEmergencyStop, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def GetmultiCarEmergencyStop(self) -> Tuple[int, Dict]:
        """
        获取物理急停状态

        """
        resp = await async_get(
            url=parse.urljoin(
                self.url, "/api/deviceInfo/emergency_status/GetmultiCarEmergencyStop"
            ),
            timeout=self.timeout,
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/emergency_status/GetmultiCarEmergencyStop, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def GetmultiCarEmergencyStop_sync(self) -> Tuple[int, Dict]:
        """
        获取物理急停状态

        """
        resp = requests.get(
            url=parse.urljoin(
                self.url, "/api/deviceInfo/emergency_status/GetmultiCarEmergencyStop"
            ),
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/deviceInfo/emergency_status/GetmultiCarEmergencyStop, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()


DeviceInfoRequest = DeviceInfoRequestCls()
