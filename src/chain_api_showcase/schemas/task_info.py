# generated by datamodel-codegen:
#   filename:  task_info.json
#   timestamp: 2024-03-06T08:28:10+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field


class AlarmMessageSchema(BaseModel):
    start_time: Union[int, str] = Field(..., title='Start Time')
    end_time: Union[int, str] = Field(..., title='End Time')
    truck_list: Optional[List] = Field([], title='Truck List')
    level: Optional[int] = Field(0, title='Level')
    per_page: Optional[int] = Field(10, title='Per Page')
    page: Optional[int] = Field(1, title='Page')


class AutomaticTsSwitchSchema(BaseModel):
    ts_name: str = Field(..., title='Ts Name')
    vessel_id: str = Field(..., title='Vessel Id')
    vessel_name: str = Field(..., title='Vessel Name')
    ts_type: str = Field(..., title='Ts Type')
    qc_id: str = Field(..., title='Qc Id')
    bollard_id: str = Field(..., title='Bollard Id')
    ts_state: str = Field(..., title='Ts State')
    ts_lane: str = Field(..., title='Ts Lane')
    position: str = Field(..., title='Position')
    offset: float = Field(..., title='Offset')
    reason: str = Field(..., title='Reason')
    auther: str = Field(..., title='Auther')
    x: float = Field(..., title='X')
    y: float = Field(..., title='Y')
    heading: float = Field(..., title='Heading')


class ContainerStack(Enum):
    field_01 = '01'
    field_02 = '02'
    field_03 = '03'


class CreateFence(BaseModel):
    device_id: str = Field(..., title='Device Id')
    passing_location: str = Field(..., title='Passing Location')
    passing_event: str = Field(..., title='Passing Event')
    timestamp: Optional[str] = Field('', title='Timestamp')


class CreateSuccessSchema(BaseModel):
    data: Optional[Any] = Field(None, title='Data')
    code: Optional[int] = Field(200, title='Code')
    msg: Optional[str] = Field('success', title='Msg')
    error: Optional[str] = Field('', title='Error')


class CreateSuccessSchemaCount(BaseModel):
    data: Optional[Any] = Field(None, title='Data')
    code: Optional[int] = Field(200, title='Code')
    msg: Optional[str] = Field('success', title='Msg')
    error: Optional[str] = Field('', title='Error')
    count: int = Field(..., title='Count')


class DelVesselInfoSchemas(BaseModel):
    vesselVisitId: str = Field(..., title='Vesselvisitid')


class DeleteJobPost(BaseModel):
    job_ids: List[str] = Field(..., title='Job Ids')


class DeleteKvStore(BaseModel):
    namespace: str = Field(..., title='Namespace')
    key: Optional[str] = Field(None, title='Key')


class ErrorOrigin(Enum):
    system = 'system'
    chassis = 'chassis'


class FinishFenceEvent(BaseModel):
    device_id: str = Field(..., title='Device Id')
    passing_location: str = Field(..., title='Passing Location')
    passing_event: str = Field(..., title='Passing Event')
    job_finish: int = Field(..., title='Job Finish')


class FullStopStatus(BaseModel):
    status: str = Field(..., title='Status')


class GetBusProcessOut(BaseModel):
    process_def_key: Optional[str] = Field(None, title='Process Def Key')
    tenant_id: Optional[str] = Field(None, title='Tenant Id')
    job_type: Optional[str] = Field(None, title='Job Type')


class GetBusProcessOutSchema(BaseModel):
    data: Optional[GetBusProcessOut] = None
    code: Optional[int] = Field(200, title='Code')
    msg: Optional[str] = Field('', title='Msg')
    error: Optional[str] = Field('', title='Error')


class GetTsSchemas(BaseModel):
    ts_name: Optional[str] = Field(None, title='Ts Name')
    ts_vessel: Optional[str] = Field(None, title='Ts Vessel')
    job_type: Optional[str] = Field(None, title='Job Type')
    ts_status: Optional[str] = Field(None, title='Ts Status')
    ts_lane: Optional[str] = Field(None, title='Ts Lane')


class LockSwitchInSchema(BaseModel):
    ts_name: str = Field(..., title='Ts Name')
    ts_state: str = Field(..., title='Ts State')
    ts_type: str = Field(..., title='Ts Type')
    x: float = Field(..., title='X')
    y: float = Field(..., title='Y')
    heading: float = Field(..., title='Heading')


class PortLocation(BaseModel):
    portX: Optional[float] = Field(0, title='Portx')
    portY: Optional[float] = Field(0, title='Porty')
    portZ: Optional[float] = Field(0, title='Portz')
    portOrientation: Optional[Union[float, str]] = Field(0, title='Portorientation')


class PreArriveInSchema(BaseModel):
    vehicle_id: str = Field(..., title='Vehicle Id')


class QueryJobAllPost(BaseModel):
    start_time: Optional[str] = Field('', title='Start Time')
    end_time: Optional[str] = Field('', title='End Time')
    status: Optional[List[int]] = Field(None, title='Status')
    vehicles: Optional[List[str]] = Field(None, title='Vehicles')
    area: Optional[str] = Field(None, title='Area')
    page: Optional[int] = Field(1, title='Page')
    page_size: Optional[int] = Field(20, title='Page Size')


class QueryJobPost(BaseModel):
    status: Optional[List[int]] = Field(None, title='Status')
    vehicles: Optional[List[str]] = Field(None, title='Vehicles')
    area: Optional[str] = Field(None, title='Area')
    page: Optional[int] = Field(1, title='Page')
    page_size: Optional[int] = Field(20, title='Page Size')


class ResendOneJob(BaseModel):
    job_id: str = Field(..., title='Job Id')
    assign_to: Optional[str] = Field(None, title='Assign To')


class SetAlarmMessageBak(BaseModel):
    deviceId: str = Field(..., title='Deviceid')
    timestamp: str = Field(..., title='Timestamp')
    alarmLevel: Optional[int] = Field(0, title='Alarmlevel')
    alarmCode: int = Field(..., title='Alarmcode')
    alarmType: Optional[int] = Field(0, title='Alarmtype')
    description: str = Field(..., title='Description')
    subCode: Optional[int] = Field(0, title='Subcode')
    subDescription: Optional[str] = Field('null', title='Subdescription')
    messageType: str = Field(..., title='Messagetype')


class SetBusProcessInSchema(BaseModel):
    process_def_key: str = Field(..., title='Process Def Key')
    tenant_id: str = Field(..., title='Tenant Id')
    job_type: str = Field(..., title='Job Type')


class SetFMSMessage(BaseModel):
    messageUniqueID: str = Field(..., title='Messageuniqueid')
    vehicleID: Optional[str] = Field('', title='Vehicleid')
    description: str = Field(..., title='Description')
    source: str = Field(..., title='Source')
    type: str = Field(..., title='Type')
    level: Optional[int] = Field(3, title='Level')


class SetKvStoreInSchema(BaseModel):
    namespace: str = Field(..., title='Namespace')
    key: str = Field(..., title='Key')
    value: Optional[Any] = Field(None, title='Value')


class SetKvStoreListInSchema(BaseModel):
    namespace: str = Field(..., title='Namespace')
    key: str = Field(..., title='Key')
    value: Optional[Any] = Field(None, title='Value')
    operation: str = Field(..., title='Operation')
    allow_duplicate: Optional[bool] = Field(True, title='Allow Duplicate')


class SetLaneInSchema(BaseModel):
    device_id: str = Field(..., title='Device Id')
    lane_id: str = Field(..., title='Lane Id')
    lane_type: Optional[str] = Field('people', title='Lane Type')


class SetVesselInfoSchemas(BaseModel):
    vesselVisitId: str = Field(..., title='Vesselvisitid')
    vesselName: str = Field(..., title='Vesselname')
    inVyg: str = Field(..., title='Invyg')
    outVyg: str = Field(..., title='Outvyg')
    phase: str = Field(..., title='Phase')
    bollardFore: int = Field(..., title='Bollardfore')
    bollardAfter: int = Field(..., title='Bollardafter')
    vessl_type: str = Field(..., title='Vessl Type')
    initializedAt: str = Field(..., title='Initializedat')
    vesselDirection: str = Field(..., title='Vesseldirection')
    at_list: List = Field(..., title='At List')
    QCAG: List = Field(..., title='Qcag')
    bowPB: List = Field(..., title='Bowpb')
    stnPB: List = Field(..., title='Stnpb')
    ETA: str = Field(..., title='Eta')
    ETB: Optional[str] = Field('', title='Etb')
    ETD: str = Field(..., title='Etd')
    rta_time: str = Field(..., title='Rta Time')
    coordinate: List = Field(..., title='Coordinate')
    messes_type: str = Field(..., title='Messes Type')
    update_status: str = Field(..., title='Update Status')


class SetVesselInfoStatusSchemas(BaseModel):
    vesselVisitId: str = Field(..., title='Vesselvisitid')
    VesselStatus: str = Field(..., title='Vesselstatus')


class SetWorkflowNodes(BaseModel):
    business_key: str = Field(..., title='Business Key')
    node: str = Field(..., title='Node')
    origin: Optional[str] = Field('AUTO', title='Origin')
    state: Optional[str] = Field('open', title='State')


class StopAlarmMessage(BaseModel):
    deviceId: str = Field(..., title='Deviceid')
    timestamp: str = Field(..., title='Timestamp')
    alarmCode: int = Field(..., title='Alarmcode')


class UpdateAdditionalInfo(BaseModel):
    vehicle_id: str = Field(..., title='Vehicle Id')
    job_content: Optional[Dict[str, Any]] = Field(None, title='Job Content')
    job_extra: Optional[Dict[str, Any]] = Field(None, title='Job Extra')
    job_add: Optional[Dict[str, Any]] = Field(None, title='Job Add')


class UpdateJobTask(BaseModel):
    job_content: Optional[Dict[str, Any]] = Field({}, title='Job Content')
    business_key: str = Field(..., title='Business Key')
    destination: Optional[Dict[str, Any]] = Field({}, title='Destination')
    passingLocation: Optional[str] = Field('', title='Passinglocation')
    plannedContainerDestinationList: Optional[List[Dict[str, Any]]] = Field(
        [], title='Plannedcontainerdestinationlist'
    )


class UpdatePlanContainers(BaseModel):
    business_key: str = Field(..., title='Business Key')
    plannedContainerDestinationList: List[Dict[str, Any]] = Field(
        ..., title='Plannedcontainerdestinationlist'
    )


class ValidationError(BaseModel):
    loc: List[Union[str, int]] = Field(..., title='Location')
    msg: str = Field(..., title='Message')
    type: str = Field(..., title='Error Type')


class VirtualPointsPost(BaseModel):
    virtual_type: str = Field(..., title='Virtual Type')
    key_points: List[str] = Field(..., title='Key Points')


class LogicalLocation(BaseModel):
    area: Optional[str] = Field(None, title='Area')
    block: Optional[str] = Field(None, title='Block')
    lane: Optional[str] = Field(None, title='Lane')
    stack: Optional[str] = Field(None, title='Stack')
    tier: Optional[str] = Field(None, title='Tier')


class ContainerInfoSchema(BaseModel):
    containerStack: Optional[ContainerStack] = None
    containerNum: Optional[str] = Field(None, title='Containernum')
    containerIso: Optional[str] = Field(None, title='Containeriso')
    doorDirection: Optional[str] = Field(None, title='Doordirection')
    referenceId: Optional[str] = Field(None, title='Referenceid')
    weight: Optional[str] = Field(None, title='Weight')
    sealing: Optional[str] = Field(None, title='Sealing')
    type: Optional[str] = Field(None, title='Type')
    emptyFull: Optional[str] = Field(None, title='Emptyfull')


class HTTPValidationError(BaseModel):
    detail: Optional[List[ValidationError]] = Field(None, title='Detail')


class ResendJobPost(BaseModel):
    business_keys: Optional[List[str]] = Field(None, title='Business Keys')
    resend_jobs: Optional[List[ResendOneJob]] = Field(None, title='Resend Jobs')


class SetAlarmMessage(BaseModel):
    deviceId: str = Field(..., title='Deviceid')
    error_origin: ErrorOrigin
    error_info: Optional[List[SetAlarmMessageBak]] = Field([], title='Error Info')


class SetContainerInfoInSchema(BaseModel):
    vehicle_id: str = Field(..., title='Vehicle Id')
    is_reference_id_updated: Optional[bool] = Field(
        True, title='Is Reference Id Updated'
    )
    containerList: List[ContainerInfoSchema] = Field(..., title='Containerlist')


class UpdateJobDest(BaseModel):
    business_key: str = Field(..., title='Business Key')
    destination: LogicalLocation
    port_location: Optional[PortLocation] = None
