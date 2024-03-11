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
from ..schemas.vehicle_manager import *

__all__ = ["VehicleManagerRequest"]


class VehicleManagerRequestCls(ApiRequestBaseCls):
    def __init__(self):
        super(VehicleManagerRequestCls, self).__init__()
        self.SERVICE_PORT = 8101
        self.SERVICE_NAME = "vehicle_manager"
        self.module_mapping[self.SERVICE_NAME] = self

    async def fleetmgmt(self) -> Tuple[int, FleetmgmtResponseInSchema]:
        """
        查询所有车辆的上下线状态

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/vehicleManager/fleetmgmt/"),
            timeout=self.timeout,
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/fleetmgmt/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, FleetmgmtResponseInSchema.model_validate_json(resp)

    def fleetmgmt_sync(self) -> Tuple[int, FleetmgmtResponseInSchema]:
        """
        查询所有车辆的上下线状态

        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/api/vehicleManager/fleetmgmt/"),
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/fleetmgmt/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, FleetmgmtResponseInSchema.model_validate_json(resp)

    async def stop(self, body: StopRequestInSchema) -> Tuple[int, StopResponseInSchema]:
        """
        单车警停

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/vehicleManager/stop/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/stop/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, StopResponseInSchema.model_validate_json(resp)

    def stop_sync(self, body: StopRequestInSchema) -> Tuple[int, StopResponseInSchema]:
        """
        单车警停

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/vehicleManager/stop/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/stop/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, StopResponseInSchema.model_validate_json(resp)

    async def stop_all(
        self, body: StopAllRequestInSchema
    ) -> Tuple[int, StopAllResponseInSchema]:
        """
        全场警停

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/vehicleManager/stop-all/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/stop-all/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, StopAllResponseInSchema.model_validate_json(resp)

    def stop_all_sync(
        self, body: StopAllRequestInSchema
    ) -> Tuple[int, StopAllResponseInSchema]:
        """
        全场警停

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/vehicleManager/stop-all/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/stop-all/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, StopAllResponseInSchema.model_validate_json(resp)

    async def position_remove(
        self, body: RemoveVehiclePositionRequestInSchema, vin: str
    ) -> Tuple[int, RemoveVehiclePositionResponseInSchema]:
        """
        删除幽灵车

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/vehicleManager/position_remove/{vin}"),
            timeout=self.timeout,
            data=body.model_dump_json(),
            params=dict(vin=vin),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/position_remove/{vin}, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, RemoveVehiclePositionResponseInSchema.model_validate_json(
            resp
        )

    def position_remove_sync(
        self, body: RemoveVehiclePositionRequestInSchema, vin: str
    ) -> Tuple[int, RemoveVehiclePositionResponseInSchema]:
        """
        删除幽灵车

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/vehicleManager/position_remove/{vin}"),
            timeout=self.timeout,
            data=body.model_dump_json(),
            params=dict(vin=vin),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/position_remove/{vin}, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return (
            resp.status_code,
            RemoveVehiclePositionResponseInSchema.model_validate_json(resp),
        )

    async def position_remove_all(
        self, body: RemoveAllVehiclePositionRequestInSchema
    ) -> Tuple[int, RemoveAllVehiclePositionResponseInSchema]:
        """
        一键清理占位车辆

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/vehicleManager/position_remove_all/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/position_remove_all/, response: {resp.text}"
            )
            return resp.status, resp.text
        return (
            resp.status,
            RemoveAllVehiclePositionResponseInSchema.model_validate_json(resp),
        )

    def position_remove_all_sync(
        self, body: RemoveAllVehiclePositionRequestInSchema
    ) -> Tuple[int, RemoveAllVehiclePositionResponseInSchema]:
        """
        一键清理占位车辆

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/vehicleManager/position_remove_all/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/position_remove_all/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return (
            resp.status_code,
            RemoveAllVehiclePositionResponseInSchema.model_validate_json(resp),
        )

    async def power(
        self, body: VehiclePowerRequestInSchema
    ) -> Tuple[int, VehiclePowerResponseInSchema]:
        """
        上/下电

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/vehicleManager/power/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/power/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, VehiclePowerResponseInSchema.model_validate_json(resp)

    def power_sync(
        self, body: VehiclePowerRequestInSchema
    ) -> Tuple[int, VehiclePowerResponseInSchema]:
        """
        上/下电

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/vehicleManager/power/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/power/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, VehiclePowerResponseInSchema.model_validate_json(resp)

    async def bertinitial(
        self, body: BerthRequestInSchema
    ) -> Tuple[int, BerthResponseInSchema]:
        """
                更新船舶停靠朝向
                :param request: {'vesselVisitId': '9450387', 'operateType': 2, 'vesselDirection': 2, 'bowPbNum': [], 'sternPbNum': []}
        operateType: 1 Initial (Default) 船舶靠岸; 2 Departure 船舶离岸
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/vehicleManager/bertinitial/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/bertinitial/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, BerthResponseInSchema.model_validate_json(resp)

    def bertinitial_sync(
        self, body: BerthRequestInSchema
    ) -> Tuple[int, BerthResponseInSchema]:
        """
                更新船舶停靠朝向
                :param request: {'vesselVisitId': '9450387', 'operateType': 2, 'vesselDirection': 2, 'bowPbNum': [], 'sternPbNum': []}
        operateType: 1 Initial (Default) 船舶靠岸; 2 Departure 船舶离岸
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/vehicleManager/bertinitial/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/bertinitial/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, BerthResponseInSchema.model_validate_json(resp)

    async def navigation(
        self, body: NavigationRequestInSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
                下发路径
                起始点:
            CLTP-X2-13-01, CLTP-X3-13-01, CLTP-X4-13-01, CLTP-X2-18-01, CLTP-X3-18-01, CLTP-X4-18-01

        request params:
        {
            "vehicleMissionId": "Test_20230414_123_f2fsf232t3232r3",
            "parkClosely": 0,
            "operationType": "",
            "vin": "I001",
            "destination": "CLTP-T2-04-01",
            "missionType": "MOVE",
            "passingLocation": [],
            "containerId1": "string",
            "containerId1Size": 0,
            "containerId1Pos": 0,
            "containerId1Seq": 0,
            "containerId2": "string",
            "containerId2Size": 0,
            "containerId2Pos": 0
        }
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/vehicleManager/navigation/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/navigation/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    def navigation_sync(
        self, body: NavigationRequestInSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
                下发路径
                起始点:
            CLTP-X2-13-01, CLTP-X3-13-01, CLTP-X4-13-01, CLTP-X2-18-01, CLTP-X3-18-01, CLTP-X4-18-01

        request params:
        {
            "vehicleMissionId": "Test_20230414_123_f2fsf232t3232r3",
            "parkClosely": 0,
            "operationType": "",
            "vin": "I001",
            "destination": "CLTP-T2-04-01",
            "missionType": "MOVE",
            "passingLocation": [],
            "containerId1": "string",
            "containerId1Size": 0,
            "containerId1Pos": 0,
            "containerId1Seq": 0,
            "containerId2": "string",
            "containerId2Size": 0,
            "containerId2Pos": 0
        }
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/vehicleManager/navigation/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/navigation/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, CreateSuccessSchema.model_validate_json(resp)

    async def api_vehicleManager_abort_post(
        self, vehicle_id: str
    ) -> Tuple[int, AbortResponseInSchema]:
        """
                Abort
                :param request: {"vehicle_id": "SC01", "updateMissionStatus": "ABORT", "transId":"a-b-c"}
        :return:
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/vehicleManager/abort/{vehicle_id}"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/abort/{vehicle_id}, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, AbortResponseInSchema.model_validate_json(resp)

    def api_vehicleManager_abort_post_sync(
        self, vehicle_id: str
    ) -> Tuple[int, AbortResponseInSchema]:
        """
                Abort
                :param request: {"vehicle_id": "SC01", "updateMissionStatus": "ABORT", "transId":"a-b-c"}
        :return:
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/vehicleManager/abort/{vehicle_id}"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/abort/{vehicle_id}, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, AbortResponseInSchema.model_validate_json(resp)

    async def status(
        self, twist_lock_station_id: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        查询单个锁站状态

        """
        resp = await async_get(
            url=parse.urljoin(
                self.url,
                "/api/vehicleManager/twist_lock/status/{twist_lock_station_id}",
            ),
            timeout=self.timeout,
            params=dict(twist_lock_station_id=twist_lock_station_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/twist_lock/status/{twist_lock_station_id}, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    def status_sync(
        self, twist_lock_station_id: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        查询单个锁站状态

        """
        resp = requests.get(
            url=parse.urljoin(
                self.url,
                "/api/vehicleManager/twist_lock/status/{twist_lock_station_id}",
            ),
            timeout=self.timeout,
            params=dict(twist_lock_station_id=twist_lock_station_id),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/twist_lock/status/{twist_lock_station_id}, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, CreateSuccessSchema.model_validate_json(resp)

    async def twist_locks(self, status: str) -> Tuple[int, CreateSuccessSchema]:
        """
        根据状态查询符合要求的所有锁站
        status 共有如下枚举值CLOSE，IDLE，OCCUPIED，ASSIGNED，REMOVE,ALL
        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/vehicleManager/twist_locks/"),
            timeout=self.timeout,
            params=dict(status=status),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/twist_locks/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    def twist_locks_sync(self, status: str) -> Tuple[int, CreateSuccessSchema]:
        """
        根据状态查询符合要求的所有锁站
        status 共有如下枚举值CLOSE，IDLE，OCCUPIED，ASSIGNED，REMOVE,ALL
        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/api/vehicleManager/twist_locks/"),
            timeout=self.timeout,
            params=dict(status=status),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/twist_locks/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, CreateSuccessSchema.model_validate_json(resp)

    async def handshake(
        self, body: HandshakeRequestInSchema
    ) -> Tuple[int, HandshakeResponseInSchema]:
        """
                握手开关
                :param request: {'vehicleMissionId':'aaaaaa-bbbb','vin':'SC01','handshakeType':'on'}
        :return:
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/vehicleManager/handshake/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/handshake/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, HandshakeResponseInSchema.model_validate_json(resp)

    def handshake_sync(
        self, body: HandshakeRequestInSchema
    ) -> Tuple[int, HandshakeResponseInSchema]:
        """
                握手开关
                :param request: {'vehicleMissionId':'aaaaaa-bbbb','vin':'SC01','handshakeType':'on'}
        :return:
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/vehicleManager/handshake/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/handshake/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, HandshakeResponseInSchema.model_validate_json(resp)

    async def qc_positions_change(
        self, body: QCPositionRequestInSchema
    ) -> Tuple[int, QCPositionResponseInSchema]:
        """
                修改Redis中岸桥的坐标值
                :param request: {'vehicleMissionId':'aaa-bbb','QCNumber':'QC01','x':'123','y':'123'}
        :return:
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/vehicleManager/qc_positions_change/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/qc_positions_change/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, QCPositionResponseInSchema.model_validate_json(resp)

    def qc_positions_change_sync(
        self, body: QCPositionRequestInSchema
    ) -> Tuple[int, QCPositionResponseInSchema]:
        """
                修改Redis中岸桥的坐标值
                :param request: {'vehicleMissionId':'aaa-bbb','QCNumber':'QC01','x':'123','y':'123'}
        :return:
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/vehicleManager/qc_positions_change/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/qc_positions_change/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, QCPositionResponseInSchema.model_validate_json(resp)

    async def unlock(
        self, body: UnlockVehicleRequestInSchema
    ) -> Tuple[int, UnlockVehicleResponseInSchema]:
        """
                异常时解锁
                :param request: {'vehicleMissionId':'aaa-bbb','vin':'SC01','operationType':'unlock','offset':15}
        :return:
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/vehicleManager/unlock/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/unlock/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, UnlockVehicleResponseInSchema.model_validate_json(resp)

    def unlock_sync(
        self, body: UnlockVehicleRequestInSchema
    ) -> Tuple[int, UnlockVehicleResponseInSchema]:
        """
                异常时解锁
                :param request: {'vehicleMissionId':'aaa-bbb','vin':'SC01','operationType':'unlock','offset':15}
        :return:
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/vehicleManager/unlock/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/unlock/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, UnlockVehicleResponseInSchema.model_validate_json(resp)

    async def alignment(
        self, body: AlignmentRequestInSchema
    ) -> Tuple[int, AlignmentResponseInSchema]:
        """
                下发对位任务
                :param request:
        {
            "vehicleMissionId": "SC01",
            "timeStamp": "SC01",
            "vin": "SC01",
            "operationType": "INPOSITION",
            "craneID": "QC01",
            "offset": 15,  # 单位：mm
            "ICPS": 1,
            "containerId1": "TEST123"
            "containerId1Size": 40,
            "containerId1Pos": 1,
        }
        :return:
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/vehicleManager/alignment/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/alignment/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, AlignmentResponseInSchema.model_validate_json(resp)

    def alignment_sync(
        self, body: AlignmentRequestInSchema
    ) -> Tuple[int, AlignmentResponseInSchema]:
        """
                下发对位任务
                :param request:
        {
            "vehicleMissionId": "SC01",
            "timeStamp": "SC01",
            "vin": "SC01",
            "operationType": "INPOSITION",
            "craneID": "QC01",
            "offset": 15,  # 单位：mm
            "ICPS": 1,
            "containerId1": "TEST123"
            "containerId1Size": 40,
            "containerId1Pos": 1,
        }
        :return:
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/vehicleManager/alignment/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/alignment/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, AlignmentResponseInSchema.model_validate_json(resp)

    async def safetyLeave(
        self, body: SafeLeaveRequestInSchema
    ) -> Tuple[int, SafeLeaveResponseInSchema]:
        """
                安全驶离
                :param request: {'vin':'SC01','operationType':'LEAVE'}
        :return:
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/vehicleManager/safetyLeave/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/safetyLeave/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, SafeLeaveResponseInSchema.model_validate_json(resp)

    def safetyLeave_sync(
        self, body: SafeLeaveRequestInSchema
    ) -> Tuple[int, SafeLeaveResponseInSchema]:
        """
                安全驶离
                :param request: {'vin':'SC01','operationType':'LEAVE'}
        :return:
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/vehicleManager/safetyLeave/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/safetyLeave/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, SafeLeaveResponseInSchema.model_validate_json(resp)

    async def lockout_notification(
        self, body: LockoutNotificationRequestInSchema
    ) -> Tuple[int, LockoutNotificationResponseInSchema]:
        """
                闭锁通知
                :param request: {'vin':'SC01','missionId':'11'，'targetId':'RTG01','autoCalib':1}
        :return:
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/vehicleManager/lockout_notification/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/lockout_notification/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, LockoutNotificationResponseInSchema.model_validate_json(
            resp
        )

    def lockout_notification_sync(
        self, body: LockoutNotificationRequestInSchema
    ) -> Tuple[int, LockoutNotificationResponseInSchema]:
        """
                闭锁通知
                :param request: {'vin':'SC01','missionId':'11'，'targetId':'RTG01','autoCalib':1}
        :return:
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/vehicleManager/lockout_notification/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/lockout_notification/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return (
            resp.status_code,
            LockoutNotificationResponseInSchema.model_validate_json(resp),
        )

    async def short_route_mission(
        self, body: ShortBackPathRequestInSchema
    ) -> Tuple[int, ShortBackPathResponseInSchema]:
        """
                短途倒车
                {
            "vehicleMissionId": "35a0e1d4-e24d-11ec-adf5-4e77e2b881e4",
            "vin": "SC01",
            "destination": "YARD.A02.1.07.LS",
        }
        :适用项目：厦门海润码头，与2.5.1接口参数一致
        :param request:
        :return:
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/vehicleManager/short_route_mission/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/short_route_mission/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, ShortBackPathResponseInSchema.model_validate_json(resp)

    def short_route_mission_sync(
        self, body: ShortBackPathRequestInSchema
    ) -> Tuple[int, ShortBackPathResponseInSchema]:
        """
                短途倒车
                {
            "vehicleMissionId": "35a0e1d4-e24d-11ec-adf5-4e77e2b881e4",
            "vin": "SC01",
            "destination": "YARD.A02.1.07.LS",
        }
        :适用项目：厦门海润码头，与2.5.1接口参数一致
        :param request:
        :return:
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/vehicleManager/short_route_mission/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/short_route_mission/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, ShortBackPathResponseInSchema.model_validate_json(resp)

    async def query_position_available(
        self, body: QueryAvailablePosRequestInSchema
    ) -> Tuple[int, QueryAvailablePosResponseInSchema]:
        """
                查询点位是否可用
                {
            "vehicleMissionId":"4584be76-e082-11ec-9104-3cecef8668a8",
            "destination": "YARD.CK.Z.02",
            "vin": "V001",
            "timestamp": 1654495088
        }
        :适用项目：内蒙策克口岸
        :param request:
        :return:
        """
        resp = await async_post(
            url=parse.urljoin(
                self.url, "/api/vehicleManager/query_position_available/"
            ),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/query_position_available/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, QueryAvailablePosResponseInSchema.model_validate_json(resp)

    def query_position_available_sync(
        self, body: QueryAvailablePosRequestInSchema
    ) -> Tuple[int, QueryAvailablePosResponseInSchema]:
        """
                查询点位是否可用
                {
            "vehicleMissionId":"4584be76-e082-11ec-9104-3cecef8668a8",
            "destination": "YARD.CK.Z.02",
            "vin": "V001",
            "timestamp": 1654495088
        }
        :适用项目：内蒙策克口岸
        :param request:
        :return:
        """
        resp = requests.post(
            url=parse.urljoin(
                self.url, "/api/vehicleManager/query_position_available/"
            ),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/query_position_available/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, QueryAvailablePosResponseInSchema.model_validate_json(
            resp
        )

    async def report_led_information(
        self, body: ReportLedInfoRequestInSchema
    ) -> Tuple[int, ReportLedInfoResponseInSchema]:
        """
                向单车上报Led信息
                {
            "vehicleMissionId":"4584be76-e082-11ec-9104-3cecef8668a8",
            "vin": "A001",
            "LedValues": 1,  # 图片对应的编号(可选字段)
            "ID":40  # 默认40，专门用于在空箱堆场显示IGV车号(可选字段)
        }
        :适用项目：厦门海润码头
        :param request:
        :return:
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/vehicleManager/report_led_information/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/report_led_information/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, ReportLedInfoResponseInSchema.model_validate_json(resp)

    def report_led_information_sync(
        self, body: ReportLedInfoRequestInSchema
    ) -> Tuple[int, ReportLedInfoResponseInSchema]:
        """
                向单车上报Led信息
                {
            "vehicleMissionId":"4584be76-e082-11ec-9104-3cecef8668a8",
            "vin": "A001",
            "LedValues": 1,  # 图片对应的编号(可选字段)
            "ID":40  # 默认40，专门用于在空箱堆场显示IGV车号(可选字段)
        }
        :适用项目：厦门海润码头
        :param request:
        :return:
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/vehicleManager/report_led_information/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/report_led_information/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, ReportLedInfoResponseInSchema.model_validate_json(resp)

    async def weather(
        self, body: ReportWeatherRequestInSchema
    ) -> Tuple[int, ReportWeatherResponseInSchema]:
        """
                天气信息通知
                :param request: {'vehicleMissionId':'aaaa-bbbb','vin':'SC01','operationType':'rain'}
        :return:
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/vehicleManager/weather/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/weather/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, ReportWeatherResponseInSchema.model_validate_json(resp)

    def weather_sync(
        self, body: ReportWeatherRequestInSchema
    ) -> Tuple[int, ReportWeatherResponseInSchema]:
        """
                天气信息通知
                :param request: {'vehicleMissionId':'aaaa-bbbb','vin':'SC01','operationType':'rain'}
        :return:
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/vehicleManager/weather/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/weather/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, ReportWeatherResponseInSchema.model_validate_json(resp)

    async def ts_positions_change(
        self, body: TSPositionRequestInSchema
    ) -> Tuple[int, TSPositionResponseInSchema]:
        """
                修改Redis中锁站的坐标值
                :param request:{
            "transId": "1-2-3-4",
            "ts_name": "A.L.TS.01",  # "船舶航次A.装卸属性D/L.TS.车道号;装船L,卸船D",
            "ts_x": 123.44,
            "ts_lane": "02",
            "ts_type":"L"  # 锁站类型:装船L;卸船D
        }
        :return:{
            "ts_name": "A.L.TS.01",  # "船舶航次A.装卸属性D/L.TS.车道号;装船L,卸船D",
            "ts_x": 2.2,
            "ts_y": 2.3,
            "status":200
        }
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/vehicleManager/ts_positions_change/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/ts_positions_change/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, TSPositionResponseInSchema.model_validate_json(resp)

    def ts_positions_change_sync(
        self, body: TSPositionRequestInSchema
    ) -> Tuple[int, TSPositionResponseInSchema]:
        """
                修改Redis中锁站的坐标值
                :param request:{
            "transId": "1-2-3-4",
            "ts_name": "A.L.TS.01",  # "船舶航次A.装卸属性D/L.TS.车道号;装船L,卸船D",
            "ts_x": 123.44,
            "ts_lane": "02",
            "ts_type":"L"  # 锁站类型:装船L;卸船D
        }
        :return:{
            "ts_name": "A.L.TS.01",  # "船舶航次A.装卸属性D/L.TS.车道号;装船L,卸船D",
            "ts_x": 2.2,
            "ts_y": 2.3,
            "status":200
        }
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/vehicleManager/ts_positions_change/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/ts_positions_change/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, TSPositionResponseInSchema.model_validate_json(resp)

    async def create_qctp_area(
        self, body: CreateDynamicQCAreaRequestInSchema
    ) -> Tuple[int, CreateDynamicQCAreaResponseInSchema]:
        """
        创建Qctp倒车随动区域

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/vehicleManager/create_qctp_area/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/create_qctp_area/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateDynamicQCAreaResponseInSchema.model_validate_json(
            resp
        )

    def create_qctp_area_sync(
        self, body: CreateDynamicQCAreaRequestInSchema
    ) -> Tuple[int, CreateDynamicQCAreaResponseInSchema]:
        """
        创建Qctp倒车随动区域

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/vehicleManager/create_qctp_area/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/create_qctp_area/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return (
            resp.status_code,
            CreateDynamicQCAreaResponseInSchema.model_validate_json(resp),
        )

    async def delete_qctp_area(
        self, body: DeleteDynamicQCAreaRequestInSchema
    ) -> Tuple[int, DeleteDynamicQCAreaResponseInSchema]:
        """
        删除Qctp倒车随动区域

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/vehicleManager/delete_qctp_area/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/delete_qctp_area/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, DeleteDynamicQCAreaResponseInSchema.model_validate_json(
            resp
        )

    def delete_qctp_area_sync(
        self, body: DeleteDynamicQCAreaRequestInSchema
    ) -> Tuple[int, DeleteDynamicQCAreaResponseInSchema]:
        """
        删除Qctp倒车随动区域

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/vehicleManager/delete_qctp_area/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/delete_qctp_area/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return (
            resp.status_code,
            DeleteDynamicQCAreaResponseInSchema.model_validate_json(resp),
        )

    async def handle_area_by_qc_number(
        self, body: HandleAreaByQCRequestInSchema
    ) -> Tuple[int, HandleAreaByQCResponseInSchema]:
        """
                卸舱盖板期间创建Evade类型锁闭区
                :param request: {'transId': 'de2cb4b3-c324-45f9-84ff-097b3d2c728a','lockAreaId':'QCTP.QC38.04','operationType':'CREATE'}
        :param request: {'transId': 'de2cb4b3-c324-45f9-84ff-097b3d2c728a','lockAreaId':'QCTP.QC38.04','operationType':'DELETE'}
        :return:
        """
        resp = await async_post(
            url=parse.urljoin(
                self.url, "/api/vehicleManager/handle_area_by_qc_number/"
            ),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/handle_area_by_qc_number/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, HandleAreaByQCResponseInSchema.model_validate_json(resp)

    def handle_area_by_qc_number_sync(
        self, body: HandleAreaByQCRequestInSchema
    ) -> Tuple[int, HandleAreaByQCResponseInSchema]:
        """
                卸舱盖板期间创建Evade类型锁闭区
                :param request: {'transId': 'de2cb4b3-c324-45f9-84ff-097b3d2c728a','lockAreaId':'QCTP.QC38.04','operationType':'CREATE'}
        :param request: {'transId': 'de2cb4b3-c324-45f9-84ff-097b3d2c728a','lockAreaId':'QCTP.QC38.04','operationType':'DELETE'}
        :return:
        """
        resp = requests.post(
            url=parse.urljoin(
                self.url, "/api/vehicleManager/handle_area_by_qc_number/"
            ),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/handle_area_by_qc_number/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, HandleAreaByQCResponseInSchema.model_validate_json(
            resp
        )

    async def query_position_available_by_destination_type(
        self, body: QueryAvailablePosByTypeRequestInSchema
    ) -> Tuple[int, QueryAvailablePosByTypeResponseInSchema]:
        """
                按照点位类别查询点位是否可用
                :适用项目：所有项目-产品线

        :param request:
            {
            "vehicleMissionId":"4584be76-e082-11ec-9104-3cecef8668a8",
            "timestamp": "20201105T121212Z",  # 时间戳，消息上报时间，UTC时间
            "destinationType": ["PARK", "CHARGING"]
            }

            {
                "missionId": "a-b-c",
                "timestampSelf": "20161219T114920178Z",
                "timestamp": 1671545703,
                "data":{
                    "PARK": [{"x": 1.1, "y": 2.2, "theta": 3.14, "destination": "PARK.PB01"}],
                    "CHARGING": [{"x": 1.1, "y": 2.2, "theta": 3.14, "destination": "CHARGING.01"}]
                }
            }

        :return:
                {
                "vehicleMissionId": "a-b-c",
                "timestamp": "20161219T114920178Z",
                "msg":"",
                "data":{
                    "PARK": ["PARK.PB01"],
                    "CHARGING": ["CHARGING.01"]
                    }
                }
        """
        resp = await async_post(
            url=parse.urljoin(
                self.url,
                "/api/vehicleManager/query_position_available_by_destination_type/",
            ),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/query_position_available_by_destination_type/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, QueryAvailablePosByTypeResponseInSchema.model_validate_json(
            resp
        )

    def query_position_available_by_destination_type_sync(
        self, body: QueryAvailablePosByTypeRequestInSchema
    ) -> Tuple[int, QueryAvailablePosByTypeResponseInSchema]:
        """
                按照点位类别查询点位是否可用
                :适用项目：所有项目-产品线

        :param request:
            {
            "vehicleMissionId":"4584be76-e082-11ec-9104-3cecef8668a8",
            "timestamp": "20201105T121212Z",  # 时间戳，消息上报时间，UTC时间
            "destinationType": ["PARK", "CHARGING"]
            }

            {
                "missionId": "a-b-c",
                "timestampSelf": "20161219T114920178Z",
                "timestamp": 1671545703,
                "data":{
                    "PARK": [{"x": 1.1, "y": 2.2, "theta": 3.14, "destination": "PARK.PB01"}],
                    "CHARGING": [{"x": 1.1, "y": 2.2, "theta": 3.14, "destination": "CHARGING.01"}]
                }
            }

        :return:
                {
                "vehicleMissionId": "a-b-c",
                "timestamp": "20161219T114920178Z",
                "msg":"",
                "data":{
                    "PARK": ["PARK.PB01"],
                    "CHARGING": ["CHARGING.01"]
                    }
                }
        """
        resp = requests.post(
            url=parse.urljoin(
                self.url,
                "/api/vehicleManager/query_position_available_by_destination_type/",
            ),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/query_position_available_by_destination_type/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return (
            resp.status_code,
            QueryAvailablePosByTypeResponseInSchema.model_validate_json(resp),
        )

    async def handel_nopass_area(self) -> Tuple[int, CreateSuccessSchema]:
        """
        创建/更新/删除锁闭区

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/vehicleManager/handel_nopass_area/"),
            timeout=self.timeout,
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/handel_nopass_area/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    def handel_nopass_area_sync(self) -> Tuple[int, CreateSuccessSchema]:
        """
        创建/更新/删除锁闭区

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/vehicleManager/handel_nopass_area/"),
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/handel_nopass_area/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, CreateSuccessSchema.model_validate_json(resp)

    async def query_nopass_area(self) -> Tuple[int, CreateSuccessSchema]:
        """
        查询锁闭区

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/vehicleManager/query_nopass_area/"),
            timeout=self.timeout,
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/query_nopass_area/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    def query_nopass_area_sync(self) -> Tuple[int, CreateSuccessSchema]:
        """
        查询锁闭区

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/vehicleManager/query_nopass_area/"),
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/query_nopass_area/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, CreateSuccessSchema.model_validate_json(resp)

    async def report_speed_ratio(
        self, body: ReportSpeedRatioRequestInSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
                调整单车仿真器倍率
                :param request: {'vehicleMissionId':'aaaa-bbbb','vin':'ALL','speedRatio':1}
        :return:
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/vehicleManager/report_speed_ratio/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/report_speed_ratio/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    def report_speed_ratio_sync(
        self, body: ReportSpeedRatioRequestInSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
                调整单车仿真器倍率
                :param request: {'vehicleMissionId':'aaaa-bbbb','vin':'ALL','speedRatio':1}
        :return:
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/vehicleManager/report_speed_ratio/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/report_speed_ratio/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, CreateSuccessSchema.model_validate_json(resp)

    async def save_lock_area_check_time(self) -> Tuple[int, CreateSuccessSchema]:
        """
                设置车辆在卡口的等待时间
                :param request:{
            "transId":"a-b-c",
            "lockAreaId": "1-2-3-4",
            "checkTime": 5  # 单位：秒
        }
        :return:{
            "status":200
        }
        """
        resp = await async_post(
            url=parse.urljoin(
                self.url, "/api/vehicleManager/save_lock_area_check_time/"
            ),
            timeout=self.timeout,
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/save_lock_area_check_time/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    def save_lock_area_check_time_sync(self) -> Tuple[int, CreateSuccessSchema]:
        """
                设置车辆在卡口的等待时间
                :param request:{
            "transId":"a-b-c",
            "lockAreaId": "1-2-3-4",
            "checkTime": 5  # 单位：秒
        }
        :return:{
            "status":200
        }
        """
        resp = requests.post(
            url=parse.urljoin(
                self.url, "/api/vehicleManager/save_lock_area_check_time/"
            ),
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/save_lock_area_check_time/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, CreateSuccessSchema.model_validate_json(resp)

    async def forced_alarm_cancel(self) -> Tuple[int, CreateSuccessSchema]:
        """
        强制恢复故障车辆

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/vehicleManager/forced_alarm_cancel/"),
            timeout=self.timeout,
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/forced_alarm_cancel/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    def forced_alarm_cancel_sync(self) -> Tuple[int, CreateSuccessSchema]:
        """
        强制恢复故障车辆

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/vehicleManager/forced_alarm_cancel/"),
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/forced_alarm_cancel/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, CreateSuccessSchema.model_validate_json(resp)

    async def report_qtruck_command(
        self, body: ReportQtruckCommandRequestInSchema
    ) -> Tuple[int, ReportQtruckCommandResponseInSchema]:
        """
            倒车及上下挂
            :param request: {'transId':'aaaa-bbbb','vin':'SC01','missionCommand':15}
        command给值范围
            15-车辆自行倒车进停车位
            16-开始自动上挂
            17-开始自动下挂
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/vehicleManager/report_qtruck_command/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/report_qtruck_command/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, ReportQtruckCommandResponseInSchema.model_validate_json(
            resp
        )

    def report_qtruck_command_sync(
        self, body: ReportQtruckCommandRequestInSchema
    ) -> Tuple[int, ReportQtruckCommandResponseInSchema]:
        """
            倒车及上下挂
            :param request: {'transId':'aaaa-bbbb','vin':'SC01','missionCommand':15}
        command给值范围
            15-车辆自行倒车进停车位
            16-开始自动上挂
            17-开始自动下挂
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/vehicleManager/report_qtruck_command/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/report_qtruck_command/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return (
            resp.status_code,
            ReportQtruckCommandResponseInSchema.model_validate_json(resp),
        )

    async def alarm_request(
        self, body: AlarmRequestInSchema
    ) -> Tuple[int, AlarmResponseInSchema]:
        """
            告警信息上报
            :param request:
        11- path planning interface故障[自定义]
        12- path planning故障[自定义]
        13- path planning hub故障[自定义]
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/vehicleManager/alarm_request/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/alarm_request/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, AlarmResponseInSchema.model_validate_json(resp)

    def alarm_request_sync(
        self, body: AlarmRequestInSchema
    ) -> Tuple[int, AlarmResponseInSchema]:
        """
            告警信息上报
            :param request:
        11- path planning interface故障[自定义]
        12- path planning故障[自定义]
        13- path planning hub故障[自定义]
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/vehicleManager/alarm_request/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/alarm_request/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, AlarmResponseInSchema.model_validate_json(resp)

    async def receive_vehicle_message(
        self, body: VinMqttRequestInSchema
    ) -> Tuple[int, VinMqttResponseInSchema]:
        """
        接收车辆的Mqtt消息

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/vehicleManager/receive_vehicle_message/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/receive_vehicle_message/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, VinMqttResponseInSchema.model_validate_json(resp)

    def receive_vehicle_message_sync(
        self, body: VinMqttRequestInSchema
    ) -> Tuple[int, VinMqttResponseInSchema]:
        """
        接收车辆的Mqtt消息

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/vehicleManager/receive_vehicle_message/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/receive_vehicle_message/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, VinMqttResponseInSchema.model_validate_json(resp)

    async def sensorInfo(self, vehicle_id: str) -> Tuple[int, SensorResponseInSchema]:
        """
        上报车辆激光数据

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/vehicleManager/sensorInfo/"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/sensorInfo/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, SensorResponseInSchema.model_validate_json(resp)

    def sensorInfo_sync(self, vehicle_id: str) -> Tuple[int, SensorResponseInSchema]:
        """
        上报车辆激光数据

        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/api/vehicleManager/sensorInfo/"),
            timeout=self.timeout,
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/sensorInfo/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, SensorResponseInSchema.model_validate_json(resp)

    async def unlock_init(self) -> Tuple[int, CreateSuccessSchema]:
        """
        下发解锁任务
        todo 需要实现下发解锁任务逻辑，需要实现request_body对应的schema
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/vehicleManager/unlock_init/"),
            timeout=self.timeout,
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/unlock_init/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    def unlock_init_sync(self) -> Tuple[int, CreateSuccessSchema]:
        """
        下发解锁任务
        todo 需要实现下发解锁任务逻辑，需要实现request_body对应的schema
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/vehicleManager/unlock_init/"),
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/unlock_init/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, CreateSuccessSchema.model_validate_json(resp)

    async def eventRegister(
        self, body: EventRegisterInSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        事件注册
        todo 需要实现事件注册的逻辑， request_body的schema也需要实现
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/vehicleManager/eventRegister/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/eventRegister/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    def eventRegister_sync(
        self, body: EventRegisterInSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        事件注册
        todo 需要实现事件注册的逻辑， request_body的schema也需要实现
        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/vehicleManager/eventRegister/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/eventRegister/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, CreateSuccessSchema.model_validate_json(resp)

    async def api_test(self) -> Tuple[int, Dict]:
        """
        Receive Vehicle Message

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/vehicleManager/api_test/"),
            timeout=self.timeout,
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/api_test/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def api_test_sync(self) -> Tuple[int, Dict]:
        """
        Receive Vehicle Message

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/api/vehicleManager/api_test/"),
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/api_test/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def start_tracemalloc(self) -> Tuple[int, Dict]:
        """
        Service Status

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/vehicleManager/trace/start_tracemalloc"),
            timeout=self.timeout,
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/trace/start_tracemalloc, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def start_tracemalloc_sync(self) -> Tuple[int, Dict]:
        """
        Service Status

        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/api/vehicleManager/trace/start_tracemalloc"),
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/trace/start_tracemalloc, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def stop_tracemalloc(self) -> Tuple[int, Dict]:
        """
        Service Status

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/vehicleManager/trace/stop_tracemalloc"),
            timeout=self.timeout,
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/trace/stop_tracemalloc, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def stop_tracemalloc_sync(self) -> Tuple[int, Dict]:
        """
        Service Status

        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/api/vehicleManager/trace/stop_tracemalloc"),
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/trace/stop_tracemalloc, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def get_tracemalloc(self) -> Tuple[int, Dict]:
        """
        Service Status

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/vehicleManager/trace/get_tracemalloc"),
            timeout=self.timeout,
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/trace/get_tracemalloc, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def get_tracemalloc_sync(self) -> Tuple[int, Dict]:
        """
        Service Status

        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/api/vehicleManager/trace/get_tracemalloc"),
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /api/vehicleManager/trace/get_tracemalloc, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def GetRRTaskInfo(
        self, body: TaskInfoRequestInSchema
    ) -> Tuple[int, TaskInfoResponseInSchema]:
        """
        请求任务信息

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/WellGNS/GetRRTaskInfo/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /WellGNS/GetRRTaskInfo/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, TaskInfoResponseInSchema.model_validate_json(resp)

    def GetRRTaskInfo_sync(
        self, body: TaskInfoRequestInSchema
    ) -> Tuple[int, TaskInfoResponseInSchema]:
        """
        请求任务信息

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/WellGNS/GetRRTaskInfo/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /WellGNS/GetRRTaskInfo/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, TaskInfoResponseInSchema.model_validate_json(resp)

    async def SetRRTaskStatus(
        self, body: TaskStatusRequestInSchema
    ) -> Tuple[int, Dict]:
        """
        请求获取

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/WellGNS/SetRRTaskStatus/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /WellGNS/SetRRTaskStatus/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def SetRRTaskStatus_sync(self, body: TaskStatusRequestInSchema) -> Tuple[int, Dict]:
        """
        请求获取

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/WellGNS/SetRRTaskStatus/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /WellGNS/SetRRTaskStatus/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def TruckPathReport(
        self, body: PathRequestInSchema
    ) -> Tuple[int, PathResponseInSchema]:
        """
        上报路径信息

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/WellGNS/TruckPathReport/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /WellGNS/TruckPathReport/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, PathResponseInSchema.model_validate_json(resp)

    def TruckPathReport_sync(
        self, body: PathRequestInSchema
    ) -> Tuple[int, PathResponseInSchema]:
        """
        上报路径信息

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/WellGNS/TruckPathReport/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /WellGNS/TruckPathReport/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, PathResponseInSchema.model_validate_json(resp)

    async def GetRoute(
        self, body: PathRequestInSchema
    ) -> Tuple[int, PathResponseInSchema]:
        """
        请求导航路径

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/WellGNS/GetRoute/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /WellGNS/GetRoute/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, PathResponseInSchema.model_validate_json(resp)

    def GetRoute_sync(
        self, body: PathRequestInSchema
    ) -> Tuple[int, PathResponseInSchema]:
        """
        请求导航路径

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/WellGNS/GetRoute/"),
            timeout=self.timeout,
            data=body.model_dump_json(),
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /WellGNS/GetRoute/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, PathResponseInSchema.model_validate_json(resp)

    async def getEmergencyStopInfo(self) -> Tuple[int, Dict]:
        """
        马来西亚单车获取急停信息

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/WellGNS/getEmergencyStopInfo/"),
            timeout=self.timeout,
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /WellGNS/getEmergencyStopInfo/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def getEmergencyStopInfo_sync(self) -> Tuple[int, Dict]:
        """
        马来西亚单车获取急停信息

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/WellGNS/getEmergencyStopInfo/"),
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /WellGNS/getEmergencyStopInfo/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def SetTruckLocationInfo(self) -> Tuple[int, Dict]:
        """
        马来西亚单车上报位置信息

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/WellGNS/SetTruckLocationInfo/"),
            timeout=self.timeout,
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /WellGNS/SetTruckLocationInfo/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def SetTruckLocationInfo_sync(self) -> Tuple[int, Dict]:
        """
        马来西亚单车上报位置信息

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/WellGNS/SetTruckLocationInfo/"),
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /WellGNS/SetTruckLocationInfo/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def SetTruckChassis(self) -> Tuple[int, Dict]:
        """
        马来西亚单车上报底盘信息

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/WellGNS/SetTruckChassis/"),
            timeout=self.timeout,
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /WellGNS/SetTruckChassis/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def SetTruckChassis_sync(self) -> Tuple[int, Dict]:
        """
        马来西亚单车上报底盘信息

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/WellGNS/SetTruckChassis/"),
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /WellGNS/SetTruckChassis/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def SetTruckSystemStatus(self) -> Tuple[int, Dict]:
        """
        马来西亚单车上报系统信息

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/WellGNS/SetTruckSystemStatus/"),
            timeout=self.timeout,
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /WellGNS/SetTruckSystemStatus/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def SetTruckSystemStatus_sync(self) -> Tuple[int, Dict]:
        """
        马来西亚单车上报系统信息

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/WellGNS/SetTruckSystemStatus/"),
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /WellGNS/SetTruckSystemStatus/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def SetSuspendReasonReport(self) -> Tuple[int, Dict]:
        """
        马来西亚单车上报停车原因

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/WellGNS/SetSuspendReasonReport/"),
            timeout=self.timeout,
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /WellGNS/SetSuspendReasonReport/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def SetSuspendReasonReport_sync(self) -> Tuple[int, Dict]:
        """
        马来西亚单车上报停车原因

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/WellGNS/SetSuspendReasonReport/"),
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /WellGNS/SetSuspendReasonReport/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def CauseMatchFailure(self) -> Tuple[int, Dict]:
        """
        马来西亚单车上报对位超时原因

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/WellGNS/CauseMatchFailure/"),
            timeout=self.timeout,
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /WellGNS/CauseMatchFailure/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def CauseMatchFailure_sync(self) -> Tuple[int, Dict]:
        """
        马来西亚单车上报对位超时原因

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/WellGNS/CauseMatchFailure/"),
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /WellGNS/CauseMatchFailure/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def GetServiceStatus(self) -> Tuple[int, Dict]:
        """
        马来西亚单车获取服务状态

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/WellGNS/GetServiceStatus/"),
            timeout=self.timeout,
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /WellGNS/GetServiceStatus/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def GetServiceStatus_sync(self) -> Tuple[int, Dict]:
        """
        马来西亚单车获取服务状态

        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/WellGNS/GetServiceStatus/"),
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /WellGNS/GetServiceStatus/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def GetRainFallInfo(self) -> Tuple[int, Dict]:
        """
        马来西亚单车获取雨量模式以及雨量信息

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/WellGNS/GetRainFallInfo/"),
            timeout=self.timeout,
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /WellGNS/GetRainFallInfo/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def GetRainFallInfo_sync(self) -> Tuple[int, Dict]:
        """
        马来西亚单车获取雨量模式以及雨量信息

        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/WellGNS/GetRainFallInfo/"),
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /WellGNS/GetRainFallInfo/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def GetAllvehicleinfo(self) -> Tuple[int, Dict]:
        """
        获取车辆位置信息

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/WellGNS/GetAllvehicleinfo/"),
            timeout=self.timeout,
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /WellGNS/GetAllvehicleinfo/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def GetAllvehicleinfo_sync(self) -> Tuple[int, Dict]:
        """
        获取车辆位置信息

        """
        resp = requests.get(
            url=parse.urljoin(self.url, "/WellGNS/GetAllvehicleinfo/"),
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /WellGNS/GetAllvehicleinfo/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()

    async def GetTrunkInformation(self) -> Tuple[int, Dict]:
        """
        马来西亚单车上报是否有箱信息

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/WellGNS/GetTrunkInformation/"),
            timeout=self.timeout,
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /WellGNS/GetTrunkInformation/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    def GetTrunkInformation_sync(self) -> Tuple[int, Dict]:
        """
        马来西亚单车上报是否有箱信息

        """
        resp = requests.post(
            url=parse.urljoin(self.url, "/WellGNS/GetTrunkInformation/"),
            timeout=self.timeout,
        )
        if resp.status_code != 200:
            print(
                f"Request failed: {resp.status_code}, url: {self.url}, api: /WellGNS/GetTrunkInformation/, response: {resp.text}"
            )
            return resp.status_code, resp.text
        return resp.status_code, resp.json()


VehicleManagerRequest = VehicleManagerRequestCls()
