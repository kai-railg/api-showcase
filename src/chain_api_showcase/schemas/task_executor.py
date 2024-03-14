# generated by datamodel-codegen:
#   filename:  task_executor.json
#   timestamp: 2024-03-14T07:59:30+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field


class BoundaryEventEnum(Enum):
    update_event = 'update_event'
    update_ground_event = 'update_ground_event'
    shuffle_event = 'shuffle_event'
    temp_parking_event = 'temp_parking_event'
    temp_parking_cancel = 'temp_parking_cancel'
    temp_parking_resume = 'temp_parking_resume'
    redo_event = 'redo_event'
    redo_ground_event = 'redo_ground_event'
    manual_complete_event = 'manual_complete_event'
    teleop_event = 'teleop_event'
    abort_event = 'abort_event'
    abort_ground_event = 'abort_ground_event'
    abort_pickup_event = 'abort_pickup_event'


class BoundaryEventSchema(BaseModel):
    event_name: BoundaryEventEnum
    vehicle_id: str = Field(..., title='Vehicle Id')
    data: Optional[Any] = Field({}, title='Data')


class CancelCamundaSchema(BaseModel):
    vehicle_id: str = Field(..., title='Vehicle Id')
    instance_id: Optional[str] = Field('', title='Instance Id')
    cancel_reason: Optional[str] = Field('', title='Cancel Reason')


class CreateSuccessSchema(BaseModel):
    data: Optional[Any] = Field(None, title='Data')
    code: Optional[int] = Field(200, title='Code')
    msg: Optional[str] = Field('success', title='Msg')
    error: Optional[str] = Field('', title='Error')


class CycleEventNameEnum(Enum):
    InventoryKpiEvent = 'InventoryKpiEvent'
    VehicleRequestPathEvent = 'VehicleRequestPathEvent'
    ShuffleEvent = 'ShuffleEvent'


class EventDrivenNameEnum(Enum):
    container_update = 'container_update'
    vehicle_update = 'vehicle_update'
    path_update = 'path_update'


class EventDrivenTypeEnum(Enum):
    publish = 'publish'
    subscribe = 'subscribe'
    cancel = 'cancel'


class EventListenerInSchema(BaseModel):
    vin: str = Field(..., title='Vin')
    vehicleMissionId: Optional[str] = Field(None, title='Vehiclemissionid')
    jobId: Optional[str] = Field(None, title='Jobid')
    origin: Optional[str] = Field('', title='Origin')
    timeStamp: Optional[str] = Field('', title='Timestamp')
    data: Optional[Dict[str, Any]] = Field({}, title='Data')


class EventType(Enum):
    register = 'register'
    cancel = 'cancel'
    clear = 'clear'


class GetActivityNode(BaseModel):
    data: Optional[Any] = Field(None, title='Data')
    code: Optional[int] = Field(200, title='Code')
    msg: Optional[str] = Field('success', title='Msg')
    error: Optional[str] = Field('', title='Error')


class LogicalLocation(BaseModel):
    area: Optional[str] = Field(..., title='Area')
    block: Optional[str] = Field(..., title='Block')
    lane: Optional[Union[str, int]] = Field(..., title='Lane')
    stack: Optional[Union[str, int]] = Field(..., title='Stack')
    tier: Optional[Union[str, int]] = Field(..., title='Tier')
    orientation: Optional[str] = Field('', title='Orientation')


class PlannedContainerDestinationListSchema(BaseModel):
    area: Optional[str] = Field('', title='Area')
    block: Optional[str] = Field('', title='Block')
    lane: Optional[Union[str, int]] = Field(1, title='Lane')
    stack: Optional[Union[str, int]] = Field(1, title='Stack')
    tier: Optional[Union[str, int]] = Field(1, title='Tier')
    orientation: Optional[str] = Field('', title='Orientation')
    uniqueObjectID: Optional[str] = Field(None, title='Uniqueobjectid')
    destDoorDirection: Optional[str] = Field(None, title='Destdoordirection')
    containerNum: Optional[str] = Field(None, title='Containernum')
    containerISO: Optional[str] = Field(None, title='Containeriso')
    containerLengthFT: Optional[float] = Field(None, title='Containerlengthft')
    containerWeightKG: Optional[float] = Field(None, title='Containerweightkg')
    containerStack: Optional[str] = Field(None, title='Containerstack')
    containerHeight: Optional[float] = Field(None, title='Containerheight')
    containerWidth: Optional[float] = Field(None, title='Containerwidth')
    targetReady: Optional[bool] = Field(True, title='Targetready')
    portLocation: Optional[Dict[str, Any]] = Field(None, title='Portlocation')
    reeferStatus: Optional[str] = Field('', title='Reeferstatus')
    relativePos: Optional[str] = Field('', title='Relativepos')
    associatedTwinContainer_id: Optional[str] = Field(
        '', title='Associatedtwincontainer Id'
    )


class RchSchema(BaseModel):
    offset: int = Field(..., title='Offset')
    vin: str = Field(..., title='Vin')
    craneID: Optional[str] = Field('', title='Craneid')
    timeStamp: str = Field(..., title='Timestamp')


class ReceiveTaskType(Enum):
    NAVI_FINISHED = 'NAVI_FINISHED'
    CRANE_ARRIVE = 'CRANE_ARRIVE'
    ALIMENT_FINISHED = 'ALIMENT_FINISHED'
    CNTR_FINISHED = 'CNTR_FINISHED'
    MISSION_FINISHED = 'MISSION_FINISHED'
    UNLOCK_FINISHED = 'UNLOCK_FINISHED'
    AUTO_BACKUP_FINISHED = 'AUTO_BACKUP_FINISHED'
    UP_HANG_FINISHED = 'UP_HANG_FINISHED'
    DOWN_HANG_FINISHED = 'DOWN_HANG_FINISHED'
    LOCK_FINISHED = 'LOCK_FINISHED'
    NEED_RCH = 'NEED_RCH'
    RCH_FINISHED = 'RCH_FINISHED'
    BUFFER_TRUE = 'BUFFER_TRUE'
    WAIT_CONTAINER_APPEAR = 'WAIT_CONTAINER_APPEAR'
    TG_DOOR_OPEN = 'TG_DOOR_OPEN'
    REEFER_DOOR_OPEN = 'REEFER_DOOR_OPEN'
    HOIST_READY = 'HOIST_READY'
    IS_LOADABLE_LANE = 'IS_LOADABLE_LANE'
    IS_LOADABLE_HOLDING = 'IS_LOADABLE_HOLDING'
    SPREADER_FINISHED = 'SPREADER_FINISHED'
    IS_HAVE_LANE = 'IS_HAVE_LANE'
    Reefer_OFF = 'Reefer_OFF'
    TASK_ERROR = 'TASK_ERROR'
    CEG_OPEN_DOOR = 'CEG_OPEN_DOOR'
    UPDATE_PREEMPTION_TASK = 'UPDATE_PREEMPTION_TASK'
    UPDATE_BOX_AND_DESTINATION = 'UPDATE_BOX_AND_DESTINATION'
    SPREADER_BUTTON_STOP = 'SPREADER_BUTTON_STOP'
    SPREADER_BUTTON_RESUME = 'SPREADER_BUTTON_RESUME'
    MIXED_AREA_ATTR_AVAILABLE = 'MIXED_AREA_ATTR_AVAILABLE'
    CHCK_VEHICLE_CHASSIS_6 = 'CHCK_VEHICLE_CHASSIS_6'
    UPDATE_TEMP_PARKING_DEST = 'UPDATE_TEMP_PARKING_DEST'
    TEMP_PARKING_FINISHED = 'TEMP_PARKING_FINISHED'
    TEMP_PARKING_CANCEL = 'TEMP_PARKING_CANCEL'
    TEMP_PARKING_RESUME = 'TEMP_PARKING_RESUME'
    SPREADER_TASK_START = 'SPREADER_TASK_START'
    SPREADER_CONTAINER_FINISHED = 'SPREADER_CONTAINER_FINISHED'
    WAIT_TELEOP_FINISHED = 'WAIT_TELEOP_FINISHED'
    ASC_SWITCH_MODE = 'ASC_SWITCH_MODE'
    CHECK_SPREADER_FINISHED = 'CHECK_SPREADER_FINISHED'


class ServiceTaskInSchema(BaseModel):
    activityId: str = Field(..., title='Activityid')
    processDefinitionKey: str = Field(..., title='Processdefinitionkey')
    businessKey: str = Field(..., title='Businesskey')
    tenantId: str = Field(..., title='Tenantid')
    topicName: str = Field(..., title='Topicname')
    variables: Dict[str, Any] = Field(..., title='Variables')
    serviceEnv: Dict[str, Any] = Field(..., title='Serviceenv')


class ServiceTaskOutSchema(BaseModel):
    data: Optional[Dict[str, Any]] = Field({}, title='Data')
    code: Optional[int] = Field(200, title='Code')
    msg: Optional[str] = Field('', title='Msg')
    error: Optional[str] = Field('', title='Error')


class UpdateQcTaskSchema(BaseModel):
    qcId: Optional[str] = Field(None, title='Qcid')
    spreadSize: Optional[str] = Field(None, title='Spreadsize')


class ValidationError(BaseModel):
    loc: List[Union[str, int]] = Field(..., title='Location')
    msg: str = Field(..., title='Message')
    type: str = Field(..., title='Error Type')


class CycleEventSchema(BaseModel):
    event_name: CycleEventNameEnum = Field(
        ..., description='事件名称，比如 InventoryKpiEvent, 事件唯一标识'
    )
    event_type: Optional[EventType] = Field(
        'register', description='事件类型，分为注册和取消'
    )
    callback_module_name: Optional[str] = Field(
        '', description='事件回调模块名', title='Callback Module Name'
    )
    callback_params: Optional[Dict[str, Any]] = Field(
        {}, description='事件回调参数', title='Callback Params'
    )
    callback_path: Optional[str] = Field(
        '', description='事件回调url path', title='Callback Path'
    )
    callback_method: Optional[str] = Field(
        'get', description='事件回调方法', title='Callback Method'
    )
    time_cycle_pt: Optional[int] = Field(
        10, description='循环事件间隔，单位为秒', title='Time Cycle Pt'
    )


class DestinationSchema(BaseModel):
    logicalLocation: LogicalLocation


class EventDrivenSchema(BaseModel):
    event_name: EventDrivenNameEnum = Field(
        ..., description='事件唯一标识，比如 container_update '
    )
    event_type: EventDrivenTypeEnum = Field(..., description='事件类型，分为注册和取消')
    callback_module_name: Optional[str] = Field(
        '', description='事件回调模块名', title='Callback Module Name'
    )
    callback_path: Optional[str] = Field(
        '', description='事件回调url path', title='Callback Path'
    )
    callback_method: Optional[str] = Field(
        'post', description='事件回调方法', title='Callback Method'
    )


class HTTPValidationError(BaseModel):
    errors: Optional[List[ValidationError]] = Field(None, title='Errors')


class VehicleOrderSchema(BaseModel):
    messageName: str = Field(..., title='Messagename')
    messageUniqueId: Optional[str] = Field(
        None, description='消息id', title='Messageuniqueid'
    )
    messageTimestamp: Optional[str] = Field(None, title='Messagetimestamp')
    executeTogether: Optional[bool] = Field(False, title='Executetogether')
    uniqueOrderID: str = Field(..., title='Uniqueorderid')
    origin: Optional[str] = Field('', title='Origin')
    X: Optional[float] = Field(0, title='X')
    Y: Optional[float] = Field(0, title='Y')
    XY_heading: Optional[float] = Field(0, title='Xy Heading')
    craneID: Optional[str] = Field('', title='Craneid')
    moveType: Optional[str] = Field('', title='Movetype')
    jobType: str = Field(..., title='Jobtype')
    vehicleID: str = Field(..., title='Vehicleid')
    bidirection: Optional[int] = Field(1, title='Bidirection')
    job_content: Optional[Dict[str, Any]] = Field({}, title='Job Content')
    passingLocation: Optional[str] = Field('', title='Passinglocation')
    movementType: Optional[str] = Field('', title='Movementtype')
    destination: Optional[DestinationSchema] = {}
    plannedContainerDestinationList: Optional[
        List[PlannedContainerDestinationListSchema]
    ] = Field([], title='Plannedcontainerdestinationlist')
    vesselVisitID: Optional[str] = Field('', title='Vesselvisitid')
    mode: Optional[str] = Field('', title='Mode')
