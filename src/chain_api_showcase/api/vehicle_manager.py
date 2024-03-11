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
        return await self.request(
            request=async_get,
            api="/api/vehicleManager/fleetmgmt/",
            body={},
            resp_model=FleetmgmtResponseInSchema,
        )

    def fleetmgmt_sync(self) -> Tuple[int, FleetmgmtResponseInSchema]:
        """
        查询所有车辆的上下线状态

        """
        return self.request_sync(
            request=requests.get,
            api="/api/vehicleManager/fleetmgmt/",
            body={},
            resp_model=FleetmgmtResponseInSchema,
        )

    async def stop(self, body: StopRequestInSchema) -> Tuple[int, StopResponseInSchema]:
        """
        单车警停

        """
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/stop/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=StopResponseInSchema,
        )

    def stop_sync(self, body: StopRequestInSchema) -> Tuple[int, StopResponseInSchema]:
        """
        单车警停

        """
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/stop/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=StopResponseInSchema,
        )

    async def stop_all(
        self, body: StopAllRequestInSchema
    ) -> Tuple[int, StopAllResponseInSchema]:
        """
        全场警停

        """
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/stop-all/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=StopAllResponseInSchema,
        )

    def stop_all_sync(
        self, body: StopAllRequestInSchema
    ) -> Tuple[int, StopAllResponseInSchema]:
        """
        全场警停

        """
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/stop-all/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=StopAllResponseInSchema,
        )

    async def position_remove(
        self, body: RemoveVehiclePositionRequestInSchema, vin: str
    ) -> Tuple[int, RemoveVehiclePositionResponseInSchema]:
        """
        删除幽灵车

        """
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/position_remove/{vin}",
            body={"data": body.model_dump_json(), "params": dict(vin=vin)},
            resp_model=RemoveVehiclePositionResponseInSchema,
        )

    def position_remove_sync(
        self, body: RemoveVehiclePositionRequestInSchema, vin: str
    ) -> Tuple[int, RemoveVehiclePositionResponseInSchema]:
        """
        删除幽灵车

        """
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/position_remove/{vin}",
            body={"data": body.model_dump_json(), "params": dict(vin=vin)},
            resp_model=RemoveVehiclePositionResponseInSchema,
        )

    async def position_remove_all(
        self, body: RemoveAllVehiclePositionRequestInSchema
    ) -> Tuple[int, RemoveAllVehiclePositionResponseInSchema]:
        """
        一键清理占位车辆

        """
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/position_remove_all/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=RemoveAllVehiclePositionResponseInSchema,
        )

    def position_remove_all_sync(
        self, body: RemoveAllVehiclePositionRequestInSchema
    ) -> Tuple[int, RemoveAllVehiclePositionResponseInSchema]:
        """
        一键清理占位车辆

        """
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/position_remove_all/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=RemoveAllVehiclePositionResponseInSchema,
        )

    async def power(
        self, body: VehiclePowerRequestInSchema
    ) -> Tuple[int, VehiclePowerResponseInSchema]:
        """
        上/下电

        """
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/power/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=VehiclePowerResponseInSchema,
        )

    def power_sync(
        self, body: VehiclePowerRequestInSchema
    ) -> Tuple[int, VehiclePowerResponseInSchema]:
        """
        上/下电

        """
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/power/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=VehiclePowerResponseInSchema,
        )

    async def bertinitial(
        self, body: BerthRequestInSchema
    ) -> Tuple[int, BerthResponseInSchema]:
        """
                更新船舶停靠朝向
                :param request: {'vesselVisitId': '9450387', 'operateType': 2, 'vesselDirection': 2, 'bowPbNum': [], 'sternPbNum': []}
        operateType: 1 Initial (Default) 船舶靠岸; 2 Departure 船舶离岸
        """
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/bertinitial/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=BerthResponseInSchema,
        )

    def bertinitial_sync(
        self, body: BerthRequestInSchema
    ) -> Tuple[int, BerthResponseInSchema]:
        """
                更新船舶停靠朝向
                :param request: {'vesselVisitId': '9450387', 'operateType': 2, 'vesselDirection': 2, 'bowPbNum': [], 'sternPbNum': []}
        operateType: 1 Initial (Default) 船舶靠岸; 2 Departure 船舶离岸
        """
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/bertinitial/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=BerthResponseInSchema,
        )

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
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/navigation/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

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
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/navigation/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def api_vehicleManager_abort_post(
        self, vehicle_id: str
    ) -> Tuple[int, AbortResponseInSchema]:
        """
                Abort
                :param request: {"vehicle_id": "SC01", "updateMissionStatus": "ABORT", "transId":"a-b-c"}
        :return:
        """
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/abort/{vehicle_id}",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=AbortResponseInSchema,
        )

    def api_vehicleManager_abort_post_sync(
        self, vehicle_id: str
    ) -> Tuple[int, AbortResponseInSchema]:
        """
                Abort
                :param request: {"vehicle_id": "SC01", "updateMissionStatus": "ABORT", "transId":"a-b-c"}
        :return:
        """
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/abort/{vehicle_id}",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=AbortResponseInSchema,
        )

    async def status(
        self, twist_lock_station_id: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        查询单个锁站状态

        """
        return await self.request(
            request=async_get,
            api="/api/vehicleManager/twist_lock/status/{twist_lock_station_id}",
            body={"params": dict(twist_lock_station_id=twist_lock_station_id)},
            resp_model=CreateSuccessSchema,
        )

    def status_sync(
        self, twist_lock_station_id: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        查询单个锁站状态

        """
        return self.request_sync(
            request=requests.get,
            api="/api/vehicleManager/twist_lock/status/{twist_lock_station_id}",
            body={"params": dict(twist_lock_station_id=twist_lock_station_id)},
            resp_model=CreateSuccessSchema,
        )

    async def twist_locks(self, status: str) -> Tuple[int, CreateSuccessSchema]:
        """
        根据状态查询符合要求的所有锁站
        status 共有如下枚举值CLOSE，IDLE，OCCUPIED，ASSIGNED，REMOVE,ALL
        """
        return await self.request(
            request=async_get,
            api="/api/vehicleManager/twist_locks/",
            body={"params": dict(status=status)},
            resp_model=CreateSuccessSchema,
        )

    def twist_locks_sync(self, status: str) -> Tuple[int, CreateSuccessSchema]:
        """
        根据状态查询符合要求的所有锁站
        status 共有如下枚举值CLOSE，IDLE，OCCUPIED，ASSIGNED，REMOVE,ALL
        """
        return self.request_sync(
            request=requests.get,
            api="/api/vehicleManager/twist_locks/",
            body={"params": dict(status=status)},
            resp_model=CreateSuccessSchema,
        )

    async def handshake(
        self, body: HandshakeRequestInSchema
    ) -> Tuple[int, HandshakeResponseInSchema]:
        """
                握手开关
                :param request: {'vehicleMissionId':'aaaaaa-bbbb','vin':'SC01','handshakeType':'on'}
        :return:
        """
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/handshake/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=HandshakeResponseInSchema,
        )

    def handshake_sync(
        self, body: HandshakeRequestInSchema
    ) -> Tuple[int, HandshakeResponseInSchema]:
        """
                握手开关
                :param request: {'vehicleMissionId':'aaaaaa-bbbb','vin':'SC01','handshakeType':'on'}
        :return:
        """
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/handshake/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=HandshakeResponseInSchema,
        )

    async def qc_positions_change(
        self, body: QCPositionRequestInSchema
    ) -> Tuple[int, QCPositionResponseInSchema]:
        """
                修改Redis中岸桥的坐标值
                :param request: {'vehicleMissionId':'aaa-bbb','QCNumber':'QC01','x':'123','y':'123'}
        :return:
        """
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/qc_positions_change/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=QCPositionResponseInSchema,
        )

    def qc_positions_change_sync(
        self, body: QCPositionRequestInSchema
    ) -> Tuple[int, QCPositionResponseInSchema]:
        """
                修改Redis中岸桥的坐标值
                :param request: {'vehicleMissionId':'aaa-bbb','QCNumber':'QC01','x':'123','y':'123'}
        :return:
        """
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/qc_positions_change/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=QCPositionResponseInSchema,
        )

    async def unlock(
        self, body: UnlockVehicleRequestInSchema
    ) -> Tuple[int, UnlockVehicleResponseInSchema]:
        """
                异常时解锁
                :param request: {'vehicleMissionId':'aaa-bbb','vin':'SC01','operationType':'unlock','offset':15}
        :return:
        """
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/unlock/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=UnlockVehicleResponseInSchema,
        )

    def unlock_sync(
        self, body: UnlockVehicleRequestInSchema
    ) -> Tuple[int, UnlockVehicleResponseInSchema]:
        """
                异常时解锁
                :param request: {'vehicleMissionId':'aaa-bbb','vin':'SC01','operationType':'unlock','offset':15}
        :return:
        """
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/unlock/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=UnlockVehicleResponseInSchema,
        )

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
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/alignment/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=AlignmentResponseInSchema,
        )

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
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/alignment/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=AlignmentResponseInSchema,
        )

    async def safetyLeave(
        self, body: SafeLeaveRequestInSchema
    ) -> Tuple[int, SafeLeaveResponseInSchema]:
        """
                安全驶离
                :param request: {'vin':'SC01','operationType':'LEAVE'}
        :return:
        """
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/safetyLeave/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=SafeLeaveResponseInSchema,
        )

    def safetyLeave_sync(
        self, body: SafeLeaveRequestInSchema
    ) -> Tuple[int, SafeLeaveResponseInSchema]:
        """
                安全驶离
                :param request: {'vin':'SC01','operationType':'LEAVE'}
        :return:
        """
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/safetyLeave/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=SafeLeaveResponseInSchema,
        )

    async def lockout_notification(
        self, body: LockoutNotificationRequestInSchema
    ) -> Tuple[int, LockoutNotificationResponseInSchema]:
        """
                闭锁通知
                :param request: {'vin':'SC01','missionId':'11'，'targetId':'RTG01','autoCalib':1}
        :return:
        """
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/lockout_notification/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=LockoutNotificationResponseInSchema,
        )

    def lockout_notification_sync(
        self, body: LockoutNotificationRequestInSchema
    ) -> Tuple[int, LockoutNotificationResponseInSchema]:
        """
                闭锁通知
                :param request: {'vin':'SC01','missionId':'11'，'targetId':'RTG01','autoCalib':1}
        :return:
        """
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/lockout_notification/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=LockoutNotificationResponseInSchema,
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
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/short_route_mission/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=ShortBackPathResponseInSchema,
        )

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
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/short_route_mission/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=ShortBackPathResponseInSchema,
        )

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
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/query_position_available/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=QueryAvailablePosResponseInSchema,
        )

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
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/query_position_available/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=QueryAvailablePosResponseInSchema,
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
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/report_led_information/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=ReportLedInfoResponseInSchema,
        )

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
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/report_led_information/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=ReportLedInfoResponseInSchema,
        )

    async def weather(
        self, body: ReportWeatherRequestInSchema
    ) -> Tuple[int, ReportWeatherResponseInSchema]:
        """
                天气信息通知
                :param request: {'vehicleMissionId':'aaaa-bbbb','vin':'SC01','operationType':'rain'}
        :return:
        """
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/weather/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=ReportWeatherResponseInSchema,
        )

    def weather_sync(
        self, body: ReportWeatherRequestInSchema
    ) -> Tuple[int, ReportWeatherResponseInSchema]:
        """
                天气信息通知
                :param request: {'vehicleMissionId':'aaaa-bbbb','vin':'SC01','operationType':'rain'}
        :return:
        """
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/weather/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=ReportWeatherResponseInSchema,
        )

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
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/ts_positions_change/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=TSPositionResponseInSchema,
        )

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
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/ts_positions_change/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=TSPositionResponseInSchema,
        )

    async def create_qctp_area(
        self, body: CreateDynamicQCAreaRequestInSchema
    ) -> Tuple[int, CreateDynamicQCAreaResponseInSchema]:
        """
        创建Qctp倒车随动区域

        """
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/create_qctp_area/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateDynamicQCAreaResponseInSchema,
        )

    def create_qctp_area_sync(
        self, body: CreateDynamicQCAreaRequestInSchema
    ) -> Tuple[int, CreateDynamicQCAreaResponseInSchema]:
        """
        创建Qctp倒车随动区域

        """
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/create_qctp_area/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateDynamicQCAreaResponseInSchema,
        )

    async def delete_qctp_area(
        self, body: DeleteDynamicQCAreaRequestInSchema
    ) -> Tuple[int, DeleteDynamicQCAreaResponseInSchema]:
        """
        删除Qctp倒车随动区域

        """
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/delete_qctp_area/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=DeleteDynamicQCAreaResponseInSchema,
        )

    def delete_qctp_area_sync(
        self, body: DeleteDynamicQCAreaRequestInSchema
    ) -> Tuple[int, DeleteDynamicQCAreaResponseInSchema]:
        """
        删除Qctp倒车随动区域

        """
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/delete_qctp_area/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=DeleteDynamicQCAreaResponseInSchema,
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
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/handle_area_by_qc_number/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=HandleAreaByQCResponseInSchema,
        )

    def handle_area_by_qc_number_sync(
        self, body: HandleAreaByQCRequestInSchema
    ) -> Tuple[int, HandleAreaByQCResponseInSchema]:
        """
                卸舱盖板期间创建Evade类型锁闭区
                :param request: {'transId': 'de2cb4b3-c324-45f9-84ff-097b3d2c728a','lockAreaId':'QCTP.QC38.04','operationType':'CREATE'}
        :param request: {'transId': 'de2cb4b3-c324-45f9-84ff-097b3d2c728a','lockAreaId':'QCTP.QC38.04','operationType':'DELETE'}
        :return:
        """
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/handle_area_by_qc_number/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=HandleAreaByQCResponseInSchema,
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
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/query_position_available_by_destination_type/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=QueryAvailablePosByTypeResponseInSchema,
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
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/query_position_available_by_destination_type/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=QueryAvailablePosByTypeResponseInSchema,
        )

    async def handel_nopass_area(self) -> Tuple[int, CreateSuccessSchema]:
        """
        创建/更新/删除锁闭区

        """
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/handel_nopass_area/",
            body={},
            resp_model=CreateSuccessSchema,
        )

    def handel_nopass_area_sync(self) -> Tuple[int, CreateSuccessSchema]:
        """
        创建/更新/删除锁闭区

        """
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/handel_nopass_area/",
            body={},
            resp_model=CreateSuccessSchema,
        )

    async def query_nopass_area(self) -> Tuple[int, CreateSuccessSchema]:
        """
        查询锁闭区

        """
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/query_nopass_area/",
            body={},
            resp_model=CreateSuccessSchema,
        )

    def query_nopass_area_sync(self) -> Tuple[int, CreateSuccessSchema]:
        """
        查询锁闭区

        """
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/query_nopass_area/",
            body={},
            resp_model=CreateSuccessSchema,
        )

    async def report_speed_ratio(
        self, body: ReportSpeedRatioRequestInSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
                调整单车仿真器倍率
                :param request: {'vehicleMissionId':'aaaa-bbbb','vin':'ALL','speedRatio':1}
        :return:
        """
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/report_speed_ratio/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def report_speed_ratio_sync(
        self, body: ReportSpeedRatioRequestInSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
                调整单车仿真器倍率
                :param request: {'vehicleMissionId':'aaaa-bbbb','vin':'ALL','speedRatio':1}
        :return:
        """
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/report_speed_ratio/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

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
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/save_lock_area_check_time/",
            body={},
            resp_model=CreateSuccessSchema,
        )

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
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/save_lock_area_check_time/",
            body={},
            resp_model=CreateSuccessSchema,
        )

    async def forced_alarm_cancel(self) -> Tuple[int, CreateSuccessSchema]:
        """
        强制恢复故障车辆

        """
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/forced_alarm_cancel/",
            body={},
            resp_model=CreateSuccessSchema,
        )

    def forced_alarm_cancel_sync(self) -> Tuple[int, CreateSuccessSchema]:
        """
        强制恢复故障车辆

        """
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/forced_alarm_cancel/",
            body={},
            resp_model=CreateSuccessSchema,
        )

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
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/report_qtruck_command/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=ReportQtruckCommandResponseInSchema,
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
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/report_qtruck_command/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=ReportQtruckCommandResponseInSchema,
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
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/alarm_request/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=AlarmResponseInSchema,
        )

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
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/alarm_request/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=AlarmResponseInSchema,
        )

    async def receive_vehicle_message(
        self, body: VinMqttRequestInSchema
    ) -> Tuple[int, VinMqttResponseInSchema]:
        """
        接收车辆的Mqtt消息

        """
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/receive_vehicle_message/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=VinMqttResponseInSchema,
        )

    def receive_vehicle_message_sync(
        self, body: VinMqttRequestInSchema
    ) -> Tuple[int, VinMqttResponseInSchema]:
        """
        接收车辆的Mqtt消息

        """
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/receive_vehicle_message/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=VinMqttResponseInSchema,
        )

    async def sensorInfo(self, vehicle_id: str) -> Tuple[int, SensorResponseInSchema]:
        """
        上报车辆激光数据

        """
        return await self.request(
            request=async_get,
            api="/api/vehicleManager/sensorInfo/",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=SensorResponseInSchema,
        )

    def sensorInfo_sync(self, vehicle_id: str) -> Tuple[int, SensorResponseInSchema]:
        """
        上报车辆激光数据

        """
        return self.request_sync(
            request=requests.get,
            api="/api/vehicleManager/sensorInfo/",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=SensorResponseInSchema,
        )

    async def unlock_init(self) -> Tuple[int, CreateSuccessSchema]:
        """
        下发解锁任务
        todo 需要实现下发解锁任务逻辑，需要实现request_body对应的schema
        """
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/unlock_init/",
            body={},
            resp_model=CreateSuccessSchema,
        )

    def unlock_init_sync(self) -> Tuple[int, CreateSuccessSchema]:
        """
        下发解锁任务
        todo 需要实现下发解锁任务逻辑，需要实现request_body对应的schema
        """
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/unlock_init/",
            body={},
            resp_model=CreateSuccessSchema,
        )

    async def eventRegister(
        self, body: EventRegisterInSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        事件注册
        todo 需要实现事件注册的逻辑， request_body的schema也需要实现
        """
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/eventRegister/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def eventRegister_sync(
        self, body: EventRegisterInSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        事件注册
        todo 需要实现事件注册的逻辑， request_body的schema也需要实现
        """
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/eventRegister/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def api_test(self) -> Tuple[int, Dict]:
        """
        Receive Vehicle Message

        """
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/api_test/",
            body={},
            resp_model=None,
        )

    def api_test_sync(self) -> Tuple[int, Dict]:
        """
        Receive Vehicle Message

        """
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/api_test/",
            body={},
            resp_model=None,
        )

    async def start_tracemalloc(self) -> Tuple[int, Dict]:
        """
        Service Status

        """
        return await self.request(
            request=async_get,
            api="/api/vehicleManager/trace/start_tracemalloc",
            body={},
            resp_model=None,
        )

    def start_tracemalloc_sync(self) -> Tuple[int, Dict]:
        """
        Service Status

        """
        return self.request_sync(
            request=requests.get,
            api="/api/vehicleManager/trace/start_tracemalloc",
            body={},
            resp_model=None,
        )

    async def stop_tracemalloc(self) -> Tuple[int, Dict]:
        """
        Service Status

        """
        return await self.request(
            request=async_get,
            api="/api/vehicleManager/trace/stop_tracemalloc",
            body={},
            resp_model=None,
        )

    def stop_tracemalloc_sync(self) -> Tuple[int, Dict]:
        """
        Service Status

        """
        return self.request_sync(
            request=requests.get,
            api="/api/vehicleManager/trace/stop_tracemalloc",
            body={},
            resp_model=None,
        )

    async def get_tracemalloc(self) -> Tuple[int, Dict]:
        """
        Service Status

        """
        return await self.request(
            request=async_get,
            api="/api/vehicleManager/trace/get_tracemalloc",
            body={},
            resp_model=None,
        )

    def get_tracemalloc_sync(self) -> Tuple[int, Dict]:
        """
        Service Status

        """
        return self.request_sync(
            request=requests.get,
            api="/api/vehicleManager/trace/get_tracemalloc",
            body={},
            resp_model=None,
        )

    async def GetRRTaskInfo(
        self, body: TaskInfoRequestInSchema
    ) -> Tuple[int, TaskInfoResponseInSchema]:
        """
        请求任务信息

        """
        return await self.request(
            request=async_post,
            api="/WellGNS/GetRRTaskInfo/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=TaskInfoResponseInSchema,
        )

    def GetRRTaskInfo_sync(
        self, body: TaskInfoRequestInSchema
    ) -> Tuple[int, TaskInfoResponseInSchema]:
        """
        请求任务信息

        """
        return self.request_sync(
            request=requests.post,
            api="/WellGNS/GetRRTaskInfo/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=TaskInfoResponseInSchema,
        )

    async def SetRRTaskStatus(
        self, body: TaskStatusRequestInSchema
    ) -> Tuple[int, Dict]:
        """
        请求获取

        """
        return await self.request(
            request=async_post,
            api="/WellGNS/SetRRTaskStatus/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def SetRRTaskStatus_sync(self, body: TaskStatusRequestInSchema) -> Tuple[int, Dict]:
        """
        请求获取

        """
        return self.request_sync(
            request=requests.post,
            api="/WellGNS/SetRRTaskStatus/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    async def TruckPathReport(
        self, body: PathRequestInSchema
    ) -> Tuple[int, PathResponseInSchema]:
        """
        上报路径信息

        """
        return await self.request(
            request=async_post,
            api="/WellGNS/TruckPathReport/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=PathResponseInSchema,
        )

    def TruckPathReport_sync(
        self, body: PathRequestInSchema
    ) -> Tuple[int, PathResponseInSchema]:
        """
        上报路径信息

        """
        return self.request_sync(
            request=requests.post,
            api="/WellGNS/TruckPathReport/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=PathResponseInSchema,
        )

    async def GetRoute(
        self, body: PathRequestInSchema
    ) -> Tuple[int, PathResponseInSchema]:
        """
        请求导航路径

        """
        return await self.request(
            request=async_post,
            api="/WellGNS/GetRoute/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=PathResponseInSchema,
        )

    def GetRoute_sync(
        self, body: PathRequestInSchema
    ) -> Tuple[int, PathResponseInSchema]:
        """
        请求导航路径

        """
        return self.request_sync(
            request=requests.post,
            api="/WellGNS/GetRoute/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=PathResponseInSchema,
        )

    async def getEmergencyStopInfo(self) -> Tuple[int, Dict]:
        """
        马来西亚单车获取急停信息

        """
        return await self.request(
            request=async_post,
            api="/WellGNS/getEmergencyStopInfo/",
            body={},
            resp_model=None,
        )

    def getEmergencyStopInfo_sync(self) -> Tuple[int, Dict]:
        """
        马来西亚单车获取急停信息

        """
        return self.request_sync(
            request=requests.post,
            api="/WellGNS/getEmergencyStopInfo/",
            body={},
            resp_model=None,
        )

    async def SetTruckLocationInfo(self) -> Tuple[int, Dict]:
        """
        马来西亚单车上报位置信息

        """
        return await self.request(
            request=async_post,
            api="/WellGNS/SetTruckLocationInfo/",
            body={},
            resp_model=None,
        )

    def SetTruckLocationInfo_sync(self) -> Tuple[int, Dict]:
        """
        马来西亚单车上报位置信息

        """
        return self.request_sync(
            request=requests.post,
            api="/WellGNS/SetTruckLocationInfo/",
            body={},
            resp_model=None,
        )

    async def SetTruckChassis(self) -> Tuple[int, Dict]:
        """
        马来西亚单车上报底盘信息

        """
        return await self.request(
            request=async_post,
            api="/WellGNS/SetTruckChassis/",
            body={},
            resp_model=None,
        )

    def SetTruckChassis_sync(self) -> Tuple[int, Dict]:
        """
        马来西亚单车上报底盘信息

        """
        return self.request_sync(
            request=requests.post,
            api="/WellGNS/SetTruckChassis/",
            body={},
            resp_model=None,
        )

    async def SetTruckSystemStatus(self) -> Tuple[int, Dict]:
        """
        马来西亚单车上报系统信息

        """
        return await self.request(
            request=async_post,
            api="/WellGNS/SetTruckSystemStatus/",
            body={},
            resp_model=None,
        )

    def SetTruckSystemStatus_sync(self) -> Tuple[int, Dict]:
        """
        马来西亚单车上报系统信息

        """
        return self.request_sync(
            request=requests.post,
            api="/WellGNS/SetTruckSystemStatus/",
            body={},
            resp_model=None,
        )

    async def SetSuspendReasonReport(self) -> Tuple[int, Dict]:
        """
        马来西亚单车上报停车原因

        """
        return await self.request(
            request=async_post,
            api="/WellGNS/SetSuspendReasonReport/",
            body={},
            resp_model=None,
        )

    def SetSuspendReasonReport_sync(self) -> Tuple[int, Dict]:
        """
        马来西亚单车上报停车原因

        """
        return self.request_sync(
            request=requests.post,
            api="/WellGNS/SetSuspendReasonReport/",
            body={},
            resp_model=None,
        )

    async def CauseMatchFailure(self) -> Tuple[int, Dict]:
        """
        马来西亚单车上报对位超时原因

        """
        return await self.request(
            request=async_post,
            api="/WellGNS/CauseMatchFailure/",
            body={},
            resp_model=None,
        )

    def CauseMatchFailure_sync(self) -> Tuple[int, Dict]:
        """
        马来西亚单车上报对位超时原因

        """
        return self.request_sync(
            request=requests.post,
            api="/WellGNS/CauseMatchFailure/",
            body={},
            resp_model=None,
        )

    async def GetServiceStatus(self) -> Tuple[int, Dict]:
        """
        马来西亚单车获取服务状态

        """
        return await self.request(
            request=async_get,
            api="/WellGNS/GetServiceStatus/",
            body={},
            resp_model=None,
        )

    def GetServiceStatus_sync(self) -> Tuple[int, Dict]:
        """
        马来西亚单车获取服务状态

        """
        return self.request_sync(
            request=requests.get,
            api="/WellGNS/GetServiceStatus/",
            body={},
            resp_model=None,
        )

    async def GetRainFallInfo(self) -> Tuple[int, Dict]:
        """
        马来西亚单车获取雨量模式以及雨量信息

        """
        return await self.request(
            request=async_get, api="/WellGNS/GetRainFallInfo/", body={}, resp_model=None
        )

    def GetRainFallInfo_sync(self) -> Tuple[int, Dict]:
        """
        马来西亚单车获取雨量模式以及雨量信息

        """
        return self.request_sync(
            request=requests.get,
            api="/WellGNS/GetRainFallInfo/",
            body={},
            resp_model=None,
        )

    async def GetAllvehicleinfo(self) -> Tuple[int, Dict]:
        """
        获取车辆位置信息

        """
        return await self.request(
            request=async_get,
            api="/WellGNS/GetAllvehicleinfo/",
            body={},
            resp_model=None,
        )

    def GetAllvehicleinfo_sync(self) -> Tuple[int, Dict]:
        """
        获取车辆位置信息

        """
        return self.request_sync(
            request=requests.get,
            api="/WellGNS/GetAllvehicleinfo/",
            body={},
            resp_model=None,
        )

    async def GetTrunkInformation(self) -> Tuple[int, Dict]:
        """
        马来西亚单车上报是否有箱信息

        """
        return await self.request(
            request=async_post,
            api="/WellGNS/GetTrunkInformation/",
            body={},
            resp_model=None,
        )

    def GetTrunkInformation_sync(self) -> Tuple[int, Dict]:
        """
        马来西亚单车上报是否有箱信息

        """
        return self.request_sync(
            request=requests.post,
            api="/WellGNS/GetTrunkInformation/",
            body={},
            resp_model=None,
        )


VehicleManagerRequest = VehicleManagerRequestCls()
