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

from ..schemas.vehicle_manager import *

FMS_IP_ADDRESS = f"http://{os.environ.get('FMS_IP_ADDRESS', '127.0.0.1')}"


class Vehicle_ManagerRequest(object):
    url = FMS_IP_ADDRESS + ":" + "8101"
    
    @classmethod
    async def fleetmgmt(cls, ) -> AsyncHttpResponse:
        """
        查询所有车辆的上下线状态
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/fleetmgmt/"
            ),
            
        )
         
    @classmethod
    async def stop(cls, body: StopRequestInSchema) -> AsyncHttpResponse:
        """
        单车警停
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/stop/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def stop_all(cls, body: StopAllRequestInSchema) -> AsyncHttpResponse:
        """
        全场警停
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/stop-all/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def position_remove(cls, body: RemoveVehiclePositionRequestInSchema,vin: str) -> AsyncHttpResponse:
        """
        删除幽灵车
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/position_remove/{vin}"
            ),
            json=body.dict(),
            params=dict(vin=vin)
        )
         
    @classmethod
    async def position_remove_all(cls, body: RemoveAllVehiclePositionRequestInSchema) -> AsyncHttpResponse:
        """
        一键清理占位车辆
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/position_remove_all/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def power(cls, body: VehiclePowerRequestInSchema) -> AsyncHttpResponse:
        """
        上/下电
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/power/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def bertinitial(cls, body: BerthRequestInSchema) -> AsyncHttpResponse:
        """
        更新船舶停靠朝向
        :param request: {'vesselVisitId': '9450387', 'operateType': 2, 'vesselDirection': 2, 'bowPbNum': [], 'sternPbNum': []}
operateType: 1 Initial (Default) 船舶靠岸; 2 Departure 船舶离岸
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/bertinitial/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def navigation(cls, body: NavigationRequestInSchema) -> AsyncHttpResponse:
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
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/navigation/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def api_vehicleManager_abort_post(cls, vehicle_id: str) -> AsyncHttpResponse:
        """
        Abort
        :param request: {"vehicle_id": "SC01", "updateMissionStatus": "ABORT", "transId":"a-b-c"}
:return:
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/abort/{vehicle_id}"
            ),
            
            params=dict(vehicle_id=vehicle_id)
        )
         
    @classmethod
    async def status(cls, twist_lock_station_id: str) -> AsyncHttpResponse:
        """
        查询单个锁站状态
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/twist_lock/status/{twist_lock_station_id}"
            ),
            params=dict(twist_lock_station_id=twist_lock_station_id)
        )
         
    @classmethod
    async def twist_locks(cls, status: str) -> AsyncHttpResponse:
        """
        根据状态查询符合要求的所有锁站
        status 共有如下枚举值CLOSE，IDLE，OCCUPIED，ASSIGNED，REMOVE,ALL
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/twist_locks/"
            ),
            params=dict(status=status)
        )
         
    @classmethod
    async def handshake(cls, body: HandshakeRequestInSchema) -> AsyncHttpResponse:
        """
        握手开关
        :param request: {'vehicleMissionId':'aaaaaa-bbbb','vin':'SC01','handshakeType':'on'}
:return:
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/handshake/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def qc_positions_change(cls, body: QCPositionRequestInSchema) -> AsyncHttpResponse:
        """
        修改Redis中岸桥的坐标值
        :param request: {'vehicleMissionId':'aaa-bbb','QCNumber':'QC01','x':'123','y':'123'}
:return:
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/qc_positions_change/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def unlock(cls, body: UnlockVehicleRequestInSchema) -> AsyncHttpResponse:
        """
        异常时解锁
        :param request: {'vehicleMissionId':'aaa-bbb','vin':'SC01','operationType':'unlock','offset':15}
:return:
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/unlock/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def alignment(cls, body: AlignmentRequestInSchema) -> AsyncHttpResponse:
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
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/alignment/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def safetyLeave(cls, body: SafeLeaveRequestInSchema) -> AsyncHttpResponse:
        """
        安全驶离
        :param request: {'vin':'SC01','operationType':'LEAVE'}
:return:
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/safetyLeave/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def lockout_notification(cls, body: LockoutNotificationRequestInSchema) -> AsyncHttpResponse:
        """
        闭锁通知
        :param request: {'vin':'SC01','missionId':'11'，'targetId':'RTG01','autoCalib':1}
:return:
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/lockout_notification/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def short_route_mission(cls, body: ShortBackPathRequestInSchema) -> AsyncHttpResponse:
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
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/short_route_mission/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def query_position_available(cls, body: QueryAvailablePosRequestInSchema) -> AsyncHttpResponse:
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
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/query_position_available/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def report_led_information(cls, body: ReportLedInfoRequestInSchema) -> AsyncHttpResponse:
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
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/report_led_information/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def weather(cls, body: ReportWeatherRequestInSchema) -> AsyncHttpResponse:
        """
        天气信息通知
        :param request: {'vehicleMissionId':'aaaa-bbbb','vin':'SC01','operationType':'rain'}
:return:
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/weather/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def ts_positions_change(cls, body: TSPositionRequestInSchema) -> AsyncHttpResponse:
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
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/ts_positions_change/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def create_qctp_area(cls, body: CreateDynamicQCAreaRequestInSchema) -> AsyncHttpResponse:
        """
        创建Qctp倒车随动区域
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/create_qctp_area/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def delete_qctp_area(cls, body: DeleteDynamicQCAreaRequestInSchema) -> AsyncHttpResponse:
        """
        删除Qctp倒车随动区域
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/delete_qctp_area/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def handle_area_by_qc_number(cls, body: HandleAreaByQCRequestInSchema) -> AsyncHttpResponse:
        """
        卸舱盖板期间创建Evade类型锁闭区
        :param request: {'transId': 'de2cb4b3-c324-45f9-84ff-097b3d2c728a','lockAreaId':'QCTP.QC38.04','operationType':'CREATE'}
:param request: {'transId': 'de2cb4b3-c324-45f9-84ff-097b3d2c728a','lockAreaId':'QCTP.QC38.04','operationType':'DELETE'}
:return:
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/handle_area_by_qc_number/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def query_position_available_by_destination_type(cls, body: QueryAvailablePosByTypeRequestInSchema) -> AsyncHttpResponse:
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
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/query_position_available_by_destination_type/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def handel_nopass_area(cls, ) -> AsyncHttpResponse:
        """
        创建/更新/删除锁闭区
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/handel_nopass_area/"
            ),
            
            
        )
         
    @classmethod
    async def query_nopass_area(cls, ) -> AsyncHttpResponse:
        """
        查询锁闭区
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/query_nopass_area/"
            ),
            
            
        )
         
    @classmethod
    async def report_speed_ratio(cls, body: ReportSpeedRatioRequestInSchema) -> AsyncHttpResponse:
        """
        调整单车仿真器倍率
        :param request: {'vehicleMissionId':'aaaa-bbbb','vin':'ALL','speedRatio':1}
:return:
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/report_speed_ratio/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def save_lock_area_check_time(cls, ) -> AsyncHttpResponse:
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
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/save_lock_area_check_time/"
            ),
            
            
        )
         
    @classmethod
    async def forced_alarm_cancel(cls, ) -> AsyncHttpResponse:
        """
        强制恢复故障车辆
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/forced_alarm_cancel/"
            ),
            
            
        )
         
    @classmethod
    async def report_qtruck_command(cls, body: ReportQtruckCommandRequestInSchema) -> AsyncHttpResponse:
        """
        倒车及上下挂
        :param request: {'transId':'aaaa-bbbb','vin':'SC01','missionCommand':15}
    command给值范围
        15-车辆自行倒车进停车位
        16-开始自动上挂
        17-开始自动下挂
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/report_qtruck_command/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def alarm_request(cls, body: AlarmRequestInSchema) -> AsyncHttpResponse:
        """
        告警信息上报
        :param request:
    11- path planning interface故障[自定义]
    12- path planning故障[自定义]
    13- path planning hub故障[自定义]
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/alarm_request/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def receive_vehicle_message(cls, body: VinMqttRequestInSchema) -> AsyncHttpResponse:
        """
        接收车辆的Mqtt消息
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/receive_vehicle_message/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def sensorInfo(cls, vehicle_id: str) -> AsyncHttpResponse:
        """
        上报车辆激光数据
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/sensorInfo/"
            ),
            params=dict(vehicle_id=vehicle_id)
        )
         
    @classmethod
    async def unlock_init(cls, ) -> AsyncHttpResponse:
        """
        下发解锁任务
        todo 需要实现下发解锁任务逻辑，需要实现request_body对应的schema
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/unlock_init/"
            ),
            
            
        )
         
    @classmethod
    async def eventRegister(cls, body: EventRegisterInSchema) -> AsyncHttpResponse:
        """
        事件注册
        todo 需要实现事件注册的逻辑， request_body的schema也需要实现
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/eventRegister/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def api_test(cls, ) -> AsyncHttpResponse:
        """
        Receive Vehicle Message
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/api_test/"
            ),
            
            
        )
         
    @classmethod
    async def start_tracemalloc(cls, ) -> AsyncHttpResponse:
        """
        Service Status
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/trace/start_tracemalloc"
            ),
            
        )
         
    @classmethod
    async def stop_tracemalloc(cls, ) -> AsyncHttpResponse:
        """
        Service Status
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/trace/stop_tracemalloc"
            ),
            
        )
         
    @classmethod
    async def get_tracemalloc(cls, ) -> AsyncHttpResponse:
        """
        Service Status
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/trace/get_tracemalloc"
            ),
            
        )
         
    @classmethod
    async def GetRRTaskInfo(cls, body: TaskInfoRequestInSchema) -> AsyncHttpResponse:
        """
        请求任务信息
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/WellGNS/GetRRTaskInfo/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def SetRRTaskStatus(cls, body: TaskStatusRequestInSchema) -> AsyncHttpResponse:
        """
        请求获取
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/WellGNS/SetRRTaskStatus/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def TruckPathReport(cls, body: PathRequestInSchema) -> AsyncHttpResponse:
        """
        上报路径信息
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/WellGNS/TruckPathReport/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def GetRoute(cls, body: PathRequestInSchema) -> AsyncHttpResponse:
        """
        请求导航路径
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/WellGNS/GetRoute/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def getEmergencyStopInfo(cls, ) -> AsyncHttpResponse:
        """
        马来西亚单车获取急停信息
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/WellGNS/getEmergencyStopInfo/"
            ),
            
            
        )
         
    @classmethod
    async def SetTruckLocationInfo(cls, ) -> AsyncHttpResponse:
        """
        马来西亚单车上报位置信息
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/WellGNS/SetTruckLocationInfo/"
            ),
            
            
        )
         
    @classmethod
    async def SetTruckChassis(cls, ) -> AsyncHttpResponse:
        """
        马来西亚单车上报底盘信息
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/WellGNS/SetTruckChassis/"
            ),
            
            
        )
         
    @classmethod
    async def SetTruckSystemStatus(cls, ) -> AsyncHttpResponse:
        """
        马来西亚单车上报系统信息
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/WellGNS/SetTruckSystemStatus/"
            ),
            
            
        )
         
    @classmethod
    async def SetSuspendReasonReport(cls, ) -> AsyncHttpResponse:
        """
        马来西亚单车上报停车原因
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/WellGNS/SetSuspendReasonReport/"
            ),
            
            
        )
         
    @classmethod
    async def CauseMatchFailure(cls, ) -> AsyncHttpResponse:
        """
        马来西亚单车上报对位超时原因
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/WellGNS/CauseMatchFailure/"
            ),
            
            
        )
         
    @classmethod
    async def GetServiceStatus(cls, ) -> AsyncHttpResponse:
        """
        马来西亚单车获取服务状态
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/WellGNS/GetServiceStatus/"
            ),
            
        )
         
    @classmethod
    async def GetRainFallInfo(cls, ) -> AsyncHttpResponse:
        """
        马来西亚单车获取雨量模式以及雨量信息
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/WellGNS/GetRainFallInfo/"
            ),
            
        )
         
    @classmethod
    async def GetAllvehicleinfo(cls, ) -> AsyncHttpResponse:
        """
        获取车辆位置信息
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/WellGNS/GetAllvehicleinfo/"
            ),
            
        )
         
    @classmethod
    async def GetTrunkInformation(cls, ) -> AsyncHttpResponse:
        """
        马来西亚单车上报是否有箱信息
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/WellGNS/GetTrunkInformation/"
            ),
            
            
        )
         