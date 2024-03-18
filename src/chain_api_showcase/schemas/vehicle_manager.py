# generated by datamodel-codegen:
#   filename:  vehicle_manager.json
#   timestamp: 2024-03-18T08:32:17+00:00

from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field


class AbortResponseInSchema(BaseModel):
    data: Optional[Any] = Field(None, title='Data')
    code: Optional[int] = Field(200, title='Code')
    msg: Optional[str] = Field('success', title='Msg')
    error: Optional[str] = Field('', title='Error')
    status: Optional[int] = Field(200, title='Status')
    errorMsg: Optional[str] = Field('', title='Errormsg')


class AlarmResponseInSchema(BaseModel):
    data: Optional[Any] = Field(None, title='Data')
    code: Optional[int] = Field(200, title='Code')
    msg: Optional[str] = Field('success', title='Msg')
    error: Optional[str] = Field('', title='Error')
    status: Optional[str] = Field('', title='Status')
    errorMsg: Optional[str] = Field('', title='Errormsg')


class AlignmentRequestInSchema(BaseModel):
    vehicleMissionId: str = Field(..., title='Vehiclemissionid')
    timeStamp: str = Field(..., title='Timestamp')
    vin: str = Field(..., title='Vin')
    operationType: Optional[str] = Field('INPOSITION', title='Operationtype')
    craneID: str = Field(..., title='Craneid')
    offset: int = Field(..., title='Offset')
    ICPS: int = Field(..., title='Icps')
    containerId1: Optional[str] = Field('', title='Containerid1')
    containerId1Size: Optional[int] = Field(99, title='Containerid1Size')
    containerId1Pos: Optional[int] = Field(99, title='Containerid1Pos')
    containerId2: Optional[str] = Field('', title='Containerid2')
    containerId2Size: Optional[int] = Field(99, title='Containerid2Size')
    containerId2Pos: Optional[int] = Field(99, title='Containerid2Pos')


class AlignmentResponseInSchema(BaseModel):
    status: Optional[int] = Field(200, title='Status')
    errorMsg: Optional[str] = Field('', title='Errormsg')


class BerthRequestInSchema(BaseModel):
    vesselVisitId: str = Field(..., title='Vesselvisitid')
    operateType: int = Field(..., title='Operatetype')
    vesselDirection: int = Field(..., title='Vesseldirection')
    bowPbNum: List = Field(..., title='Bowpbnum')
    sternPbNum: List = Field(..., title='Sternpbnum')


class BerthResponseInSchema(BaseModel):
    data: Optional[Any] = Field(None, title='Data')
    code: Optional[int] = Field(200, title='Code')
    msg: Optional[str] = Field('success', title='Msg')
    error: Optional[str] = Field('', title='Error')
    status: Optional[str] = Field('', title='Status')
    errorMsg: Optional[str] = Field('', title='Errormsg')


class BodyObj(BaseModel):
    alarmLevel: int = Field(..., title='Alarmlevel')
    alarmType: int = Field(..., title='Alarmtype')
    alarmCode: int = Field(..., title='Alarmcode')
    description: Optional[str] = Field('', title='Description')
    subCode: Optional[int] = Field(0, title='Subcode')
    subDescription: Optional[str] = Field('', title='Subdescription')


class CreateDynamicQCAreaRequestInSchema(BaseModel):
    xl: float = Field(..., title='Xl')
    xr: float = Field(..., title='Xr')
    ship_id: str = Field(..., title='Ship Id')
    position: str = Field(..., title='Position')
    lane: int = Field(..., title='Lane')
    navi: Optional[bool] = Field(True, title='Navi')


class CreateDynamicQCAreaResponseInSchema(BaseModel):
    data: Optional[Any] = Field(None, title='Data')
    code: Optional[int] = Field(200, title='Code')
    msg: Optional[str] = Field('success', title='Msg')
    error: Optional[str] = Field('', title='Error')
    status: Optional[str] = Field('', title='Status')
    errorMsg: Optional[str] = Field('', title='Errormsg')


class CreateSuccessSchema(BaseModel):
    data: Optional[Any] = Field(None, title='Data')
    code: Optional[int] = Field(200, title='Code')
    msg: Optional[str] = Field('success', title='Msg')
    error: Optional[str] = Field('', title='Error')


class DeleteDynamicQCAreaRequestInSchema(BaseModel):
    ship_id: str = Field(..., title='Ship Id')


class DeleteDynamicQCAreaResponseInSchema(BaseModel):
    data: Optional[Any] = Field(None, title='Data')
    code: Optional[int] = Field(200, title='Code')
    msg: Optional[str] = Field('success', title='Msg')
    error: Optional[str] = Field('', title='Error')
    status: Optional[str] = Field('', title='Status')
    errorMsg: Optional[str] = Field('', title='Errormsg')


class EventRegisterInSchema(BaseModel):
    vin: str = Field(..., title='Vin')
    vehicleMissionId: str = Field(..., title='Vehiclemissionid')
    timeStamp: str = Field(..., title='Timestamp')
    eventType: str = Field(..., title='Eventtype')
    data: Optional[Any] = Field(None, title='Data')


class FleetmgmtResponseInSchema(BaseModel):
    data: Optional[Any] = Field(None, title='Data')
    code: Optional[int] = Field(200, title='Code')
    msg: Optional[str] = Field('success', title='Msg')
    error: Optional[str] = Field('', title='Error')
    count: Optional[int] = Field(0, title='Count')
    vehicles: Optional[List] = Field([], title='Vehicles')


class HandleAreaByQCRequestInSchema(BaseModel):
    transId: str = Field(..., title='Transid')
    lockAreaId: str = Field(..., title='Lockareaid')
    operationType: str = Field(..., title='Operationtype')
    freeZone: Optional[str] = Field('', title='Freezone')
    allowedEquipments: Optional[List] = Field([], title='Allowedequipments')


class HandleAreaByQCResponseInSchema(BaseModel):
    data: Optional[Any] = Field(None, title='Data')
    code: Optional[int] = Field(200, title='Code')
    msg: Optional[str] = Field('success', title='Msg')
    error: Optional[str] = Field('', title='Error')
    status: Optional[str] = Field('', title='Status')
    errorMsg: Optional[str] = Field('', title='Errormsg')


class HandshakeRequestInSchema(BaseModel):
    vin: str = Field(..., title='Vin')
    vehicleMissionId: str = Field(..., title='Vehiclemissionid')
    handshakeType: str = Field(..., title='Handshaketype')


class HandshakeResponseInSchema(BaseModel):
    data: Optional[Any] = Field(None, title='Data')
    code: Optional[int] = Field(200, title='Code')
    msg: Optional[str] = Field('success', title='Msg')
    error: Optional[str] = Field('', title='Error')
    status: Optional[str] = Field('', title='Status')
    errorMsg: Optional[str] = Field('', title='Errormsg')


class HeaderObj(BaseModel):
    transId: str = Field(..., title='Transid')
    deviceId: str = Field(..., title='Deviceid')
    timestamp: str = Field(..., title='Timestamp')


class LockoutNotificationRequestInSchema(BaseModel):
    vin: str = Field(..., title='Vin')
    missionId: str = Field(..., title='Missionid')
    targetId: str = Field(..., title='Targetid')
    autoCalib: int = Field(..., title='Autocalib')


class LockoutNotificationResponseInSchema(BaseModel):
    data: Optional[Any] = Field(None, title='Data')
    code: Optional[int] = Field(200, title='Code')
    msg: Optional[str] = Field('success', title='Msg')
    error: Optional[str] = Field('', title='Error')
    status: Optional[str] = Field('', title='Status')
    errorMsg: Optional[str] = Field('', title='Errormsg')


class NavigationRequestInSchema(BaseModel):
    vehicleMissionId: str = Field(..., title='Vehiclemissionid')
    parkClosely: Optional[int] = Field(0, title='Parkclosely')
    operationType: Optional[str] = Field('', title='Operationtype')
    vin: str = Field(..., title='Vin')
    X: Optional[float] = Field(None, title='X')
    Y: Optional[float] = Field(None, title='Y')
    XY_heading: Optional[float] = Field(None, title='Xy Heading')
    destination: str = Field(..., title='Destination')
    missionType: str = Field(..., title='Missiontype')
    movementType: Optional[str] = Field(None, title='Movementtype')
    orientation: Optional[str] = Field(None, title='Orientation')
    locationType: Optional[str] = Field(None, title='Locationtype')
    moveTask: Optional[bool] = Field(False, title='Movetask')
    passingLocation: Optional[List] = Field([], title='Passinglocation')
    missionStage: Optional[int] = Field(None, title='Missionstage')
    bidirection: Optional[int] = Field(1, title='Bidirection')
    containerId1: Optional[str] = Field(None, title='Containerid1')
    containerId1Size: Optional[int] = Field(None, title='Containerid1Size')
    containerId1Pos: Optional[int] = Field(None, title='Containerid1Pos')
    containerId1Seq: Optional[int] = Field(None, title='Containerid1Seq')
    containerId1Orientation: Optional[str] = Field(
        None, title='Containerid1Orientation'
    )
    containerId1ISO: Optional[str] = Field(None, title='Containerid1Iso')
    containerId1X: Optional[float] = Field(None, title='Containerid1X')
    containerId1Y: Optional[float] = Field(None, title='Containerid1Y')
    containerId1Weight: Optional[int] = Field(None, title='Containerid1Weight')
    containerId2: Optional[str] = Field(None, title='Containerid2')
    containerId2Size: Optional[int] = Field(None, title='Containerid2Size')
    containerId2Pos: Optional[int] = Field(None, title='Containerid2Pos')
    containerId2Seq: Optional[int] = Field(None, title='Containerid2Seq')
    containerId2ISO: Optional[str] = Field(None, title='Containerid2Iso')
    containerId2X: Optional[float] = Field(None, title='Containerid2X')
    containerId2Y: Optional[float] = Field(None, title='Containerid2Y')
    containerId2Orientation: Optional[str] = Field(
        None, title='Containerid2Orientation'
    )


class PathRequestInSchema(BaseModel):
    i_at_id: str = Field(..., title='I At Id')
    waypoints: Optional[List] = Field([], title='Waypoints')


class PathResponseInSchema(BaseModel):
    code: Optional[int] = Field(200, title='Code')
    msg: Optional[str] = Field('success', title='Msg')
    truck_id: Optional[str] = Field('AT01', title='Truck Id')


class QCPositionRequestInSchema(BaseModel):
    QCNumber: str = Field(..., title='Qcnumber')
    vehicleMissionId: str = Field(..., title='Vehiclemissionid')
    x: int = Field(..., title='X')
    y: int = Field(..., title='Y')


class QCPositionResponseInSchema(BaseModel):
    data: Optional[Any] = Field(None, title='Data')
    code: Optional[int] = Field(200, title='Code')
    msg: Optional[str] = Field('success', title='Msg')
    error: Optional[str] = Field('', title='Error')
    status: Optional[str] = Field('', title='Status')
    errorMsg: Optional[str] = Field('', title='Errormsg')


class QueryAvailablePosByTypeRequestInSchema(BaseModel):
    vehicleMissionId: str = Field(..., title='Vehiclemissionid')
    timestamp: str = Field(..., title='Timestamp')
    destinationType: List[str] = Field(..., title='Destinationtype')


class QueryAvailablePosByTypeResponseInSchema(BaseModel):
    data: Optional[str] = Field('', title='Data')
    code: Optional[int] = Field(200, title='Code')
    msg: Optional[str] = Field('', title='Msg')
    error: Optional[str] = Field('', title='Error')
    status: Optional[str] = Field('', title='Status')
    vehicleMissionId: str = Field(..., title='Vehiclemissionid')
    timestamp: Optional[str] = Field('', title='Timestamp')


class QueryAvailablePosRequestInSchema(BaseModel):
    vin: str = Field(..., title='Vin')
    vehicleMissionId: str = Field(..., title='Vehiclemissionid')
    destination: str = Field(..., title='Destination')
    timestamp: int = Field(..., title='Timestamp')


class QueryAvailablePosResponseInSchema(BaseModel):
    data: Optional[Any] = Field(None, title='Data')
    code: Optional[int] = Field(200, title='Code')
    msg: Optional[str] = Field('success', title='Msg')
    error: Optional[str] = Field('', title='Error')
    status: Optional[str] = Field('', title='Status')
    errorMsg: Optional[str] = Field('', title='Errormsg')


class RemoveAllVehiclePositionRequestInSchema(BaseModel):
    requestId: str = Field(..., title='Requestid')
    operationType: str = Field(..., title='Operationtype')


class RemoveAllVehiclePositionResponseInSchema(BaseModel):
    data: Optional[Any] = Field(None, title='Data')
    code: Optional[int] = Field(200, title='Code')
    msg: Optional[str] = Field('success', title='Msg')
    error: Optional[str] = Field('', title='Error')
    vin: Optional[str] = Field('', title='Vin')
    statusCode: Optional[str] = Field('', title='Statuscode')
    errorMsg: Optional[str] = Field('', title='Errormsg')


class RemoveVehiclePositionRequestInSchema(BaseModel):
    transId: str = Field(..., title='Transid')
    operationType: Optional[str] = Field('cancel', title='Operationtype')


class RemoveVehiclePositionResponseInSchema(BaseModel):
    data: Optional[Any] = Field(None, title='Data')
    code: Optional[int] = Field(200, title='Code')
    msg: Optional[str] = Field('success', title='Msg')
    error: Optional[str] = Field('', title='Error')
    vin: Optional[str] = Field('', title='Vin')
    statusCode: Optional[str] = Field('', title='Statuscode')
    errorMsg: Optional[str] = Field('', title='Errormsg')


class ReportLedInfoRequestInSchema(BaseModel):
    vin: str = Field(..., title='Vin')
    vehicleMissionId: str = Field(..., title='Vehiclemissionid')
    LedValues: int = Field(..., title='Ledvalues')
    ID: int = Field(..., title='Id')


class ReportLedInfoResponseInSchema(BaseModel):
    data: Optional[Any] = Field(None, title='Data')
    code: Optional[int] = Field(200, title='Code')
    msg: Optional[str] = Field('success', title='Msg')
    error: Optional[str] = Field('', title='Error')
    status: Optional[str] = Field('', title='Status')
    errorMsg: Optional[str] = Field('', title='Errormsg')


class ReportQtruckCommandRequestInSchema(BaseModel):
    transId: str = Field(..., title='Transid')
    vin: str = Field(..., title='Vin')
    missionCommand: int = Field(..., title='Missioncommand')


class ReportQtruckCommandResponseInSchema(BaseModel):
    data: Optional[Any] = Field(None, title='Data')
    code: Optional[int] = Field(200, title='Code')
    msg: Optional[str] = Field('success', title='Msg')
    error: Optional[str] = Field('', title='Error')
    status: Optional[str] = Field('', title='Status')
    errorMsg: Optional[str] = Field('', title='Errormsg')


class ReportSpeedRatioRequestInSchema(BaseModel):
    vin: Optional[str] = Field('ALL', title='Vin')
    speedRatio: Optional[int] = Field(1, title='Speedratio')


class ReportWeatherRequestInSchema(BaseModel):
    vin: str = Field(..., title='Vin')
    vehicleMissionId: str = Field(..., title='Vehiclemissionid')
    operationType: str = Field(..., title='Operationtype')


class ReportWeatherResponseInSchema(BaseModel):
    data: Optional[Any] = Field(None, title='Data')
    code: Optional[int] = Field(200, title='Code')
    msg: Optional[str] = Field('success', title='Msg')
    error: Optional[str] = Field('', title='Error')
    status: Optional[str] = Field('', title='Status')
    errorMsg: Optional[str] = Field('', title='Errormsg')


class SafeLeaveRequestInSchema(BaseModel):
    vin: str = Field(..., title='Vin')
    operationType: Optional[str] = Field('LEAVE', title='Operationtype')
    vehicleMissionId: str = Field(..., title='Vehiclemissionid')
    timeStamp: str = Field(..., title='Timestamp')


class SafeLeaveResponseInSchema(BaseModel):
    code: Optional[int] = Field(200, title='Code')
    vin: Optional[str] = Field('', title='Vin')
    errorMsg: Optional[str] = Field('', title='Errormsg')


class SensorResponseInSchema(BaseModel):
    FrontObsExists: Optional[int] = Field(-9999, title='Frontobsexists')
    RearObsExists: Optional[int] = Field(-9999, title='Rearobsexists')
    ObsHeight: Optional[int] = Field(-9999, title='Obsheight')


class ShortBackPathRequestInSchema(BaseModel):
    vin: str = Field(..., title='Vin')
    vehicleMissionId: str = Field(..., title='Vehiclemissionid')
    destination: str = Field(..., title='Destination')


class ShortBackPathResponseInSchema(BaseModel):
    data: Optional[Any] = Field(None, title='Data')
    code: Optional[int] = Field(200, title='Code')
    msg: Optional[str] = Field('success', title='Msg')
    error: Optional[str] = Field('', title='Error')
    status: Optional[str] = Field('', title='Status')
    errorMsg: Optional[str] = Field('', title='Errormsg')


class StopAllRequestInSchema(BaseModel):
    requestId: str = Field(..., title='Requestid')
    command: Optional[int] = Field(0, title='Command')


class StopAllResponseInSchema(BaseModel):
    data: Optional[Any] = Field(None, title='Data')
    code: Optional[int] = Field(200, title='Code')
    msg: Optional[str] = Field('success', title='Msg')
    error: Optional[str] = Field('', title='Error')
    vin: Optional[str] = Field('', title='Vin')


class StopRequestInSchema(BaseModel):
    vehicle_id: str = Field(..., title='Vehicle Id')
    command: int = Field(..., title='Command')
    operation_type: str = Field(..., title='Operation Type')


class StopResponseInSchema(BaseModel):
    data: Optional[Any] = Field(None, title='Data')
    code: Optional[int] = Field(200, title='Code')
    msg: Optional[str] = Field('success', title='Msg')
    error: Optional[str] = Field('', title='Error')
    vin: Optional[str] = Field('', title='Vin')


class TSPositionRequestInSchema(BaseModel):
    transId: str = Field(..., title='Transid')
    ts_name: str = Field(..., title='Ts Name')
    ts_x: str = Field(..., title='Ts X')
    ts_lane: str = Field(..., title='Ts Lane')
    ts_type: str = Field(..., title='Ts Type')


class TSPositionResponseInSchema(BaseModel):
    data: Optional[Any] = Field(None, title='Data')
    code: Optional[int] = Field(200, title='Code')
    msg: Optional[str] = Field('success', title='Msg')
    error: Optional[str] = Field('', title='Error')
    status: Optional[str] = Field('', title='Status')
    ts_name: Optional[str] = Field('', title='Ts Name')
    ts_x: Optional[float] = Field(0, title='Ts X')
    ts_y: Optional[float] = Field(0, title='Ts Y')


class TaskInfoRequestInSchema(BaseModel):
    truck_id: str = Field(..., title='Truck Id')


class TaskInfoResponseInSchema(BaseModel):
    container_info: Dict[str, Any] = Field(..., title='Container Info')
    task_type: Optional[int] = Field(1, title='Task Type')
    task_op: int = Field(..., title='Task Op')
    task_id: int = Field(..., title='Task Id')
    nGen_task_id: int = Field(..., title='Ngen Task Id')
    header: Dict[str, Any] = Field(..., title='Header')
    overtake: bool = Field(..., title='Overtake')
    tp_info: Dict[str, Any] = Field(..., title='Tp Info')
    vessel_info: Dict[str, Any] = Field(..., title='Vessel Info')
    force_overtake: int = Field(..., title='Force Overtake')
    is_redo: bool = Field(..., title='Is Redo')
    origin_tasktype: str = Field(..., title='Origin Tasktype')
    task_source: int = Field(..., title='Task Source')


class TaskStatusRequestInSchema(BaseModel):
    success: bool = Field(..., title='Success')
    task_info: Dict[str, Any] = Field(..., title='Task Info')
    time_stamp: float = Field(..., title='Time Stamp')
    truck_id: str = Field(..., title='Truck Id')


class UnlockVehicleRequestInSchema(BaseModel):
    vin: str = Field(..., title='Vin')
    vehicleMissionId: str = Field(..., title='Vehiclemissionid')
    operationType: str = Field(..., title='Operationtype')
    offset: int = Field(..., title='Offset')


class UnlockVehicleResponseInSchema(BaseModel):
    data: Optional[Any] = Field(None, title='Data')
    code: Optional[int] = Field(200, title='Code')
    msg: Optional[str] = Field('success', title='Msg')
    error: Optional[str] = Field('', title='Error')
    status: Optional[str] = Field('', title='Status')
    errorMsg: Optional[str] = Field('', title='Errormsg')


class ValidationError(BaseModel):
    loc: List[Union[str, int]] = Field(..., title='Location')
    msg: str = Field(..., title='Message')
    type: str = Field(..., title='Error Type')


class VehiclePowerRequestInSchema(BaseModel):
    requestId: str = Field(..., title='Requestid')
    vin: str = Field(..., title='Vin')
    mgmtType: str = Field(..., title='Mgmttype')


class VehiclePowerResponseInSchema(BaseModel):
    data: Optional[Any] = Field(None, title='Data')
    code: Optional[int] = Field(200, title='Code')
    msg: Optional[str] = Field('success', title='Msg')
    error: Optional[str] = Field('', title='Error')
    vin: Optional[str] = Field('', title='Vin')


class VinMqttRequestInSchema(BaseModel):
    topic_name: str = Field(..., title='Topic Name')
    qos: int = Field(..., title='Qos')
    message_type: str = Field(..., title='Message Type')
    received_data: str = Field(..., title='Received Data')


class VinMqttResponseInSchema(BaseModel):
    success: Optional[bool] = Field(True, title='Success')


class AlarmRequestInSchema(BaseModel):
    header: HeaderObj
    body: BodyObj


class HTTPValidationError(BaseModel):
    errors: Optional[List[ValidationError]] = Field(None, title='Errors')
