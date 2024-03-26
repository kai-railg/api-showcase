# generated by datamodel-codegen:
#   filename:  task_scheduler.json
#   timestamp: 2024-03-26T08:59:12+00:00

from __future__ import annotations

from enum import Enum
from typing import Dict, List, Optional, Union

from pydantic import BaseModel, Field


class DependencyDefinition(BaseModel):
    movementUniqueID: str = Field(..., title='Movementuniqueid')
    processDependency: str = Field(..., title='Processdependency')
    dependencyType: Optional[str] = Field(None, title='Dependencytype')


class DependencyItem(BaseModel):
    pickupDependency: List[List[str]] = Field(..., title='Pickupdependency')
    groundDependency: List[List[str]] = Field(..., title='Grounddependency')


class Destination(BaseModel):
    area: str = Field(..., title='Area')
    block: str = Field(..., title='Block')
    lane: int = Field(..., title='Lane')
    stack: str = Field(..., title='Stack')
    tier: int = Field(..., title='Tier')
    orientation: str = Field(..., title='Orientation')


class ExecutorLogicalLocation(BaseModel):
    area: str = Field(..., title='Area')
    block: str = Field(..., title='Block')
    lane: Optional[int] = Field(None, title='Lane')
    stack: str = Field(..., title='Stack')
    tier: Optional[int] = Field(None, title='Tier')
    orientation: str = Field(..., title='Orientation')


class ExecutorPortLocation(BaseModel):
    portX: float = Field(..., title='Portx')
    portY: float = Field(..., title='Porty')


class JobContent(BaseModel):
    tosUniqueID: str = Field(..., title='Tosuniqueid')
    twinMoveID: Optional[str] = Field(None, title='Twinmoveid')


class JobType(Enum):
    RECEIVE = 'RECEIVE'
    DELIVER = 'DELIVER'
    NAVIGATION = 'NAVIGATION'


class LocationCheck(BaseModel):
    area: str = Field(..., title='Area')
    block: str = Field(..., title='Block')
    lane: int = Field(..., title='Lane')
    stack: int = Field(..., title='Stack')
    tier: int = Field(..., title='Tier')
    orientation: str = Field(..., title='Orientation')


class MoveType(Enum):
    single = 'single'
    twin = 'twin'
    twinform = 'twinform'


class MovementCancel(BaseModel):
    messageName: Optional[str] = Field('movementCancel', title='Messagename')
    messageUniqueID: str = Field(..., title='Messageuniqueid')
    timestamp: str = Field(..., title='Timestamp')
    equipmentName: str = Field(..., title='Equipmentname')
    equipType: str = Field(..., title='Equiptype')


class MovementCancelResponse(BaseModel):
    messageName: Optional[str] = Field('movementCancelResponse', title='Messagename')
    messageUniqueID: str = Field(..., title='Messageuniqueid')
    timestamp: str = Field(..., title='Timestamp')
    cancelResult: bool = Field(..., title='Cancelresult')


class MovementType(Enum):
    Yardmove = 'Yardmove'
    Load = 'Load'
    Discharge = 'Discharge'


class MovementUpdateResponse(BaseModel):
    messageName: str = Field(..., title='Messagename')
    messageUniqueID: str = Field(..., title='Messageuniqueid')
    timeStamp: str = Field(..., title='Timestamp')
    updateResult: Optional[bool] = Field(None, title='Updateresult')


class Origin(BaseModel):
    area: str = Field(..., title='Area')
    block: str = Field(..., title='Block')
    lane: int = Field(..., title='Lane')
    stack: str = Field(..., title='Stack')
    tier: int = Field(..., title='Tier')
    orientation: str = Field(..., title='Orientation')


class PlannedContainerDestinationDict(BaseModel):
    area: str = Field(..., title='Area')
    block: Optional[str] = Field(None, title='Block')
    lane: Optional[int] = Field(None, title='Lane')
    stack: Optional[str] = Field(None, title='Stack')
    tier: Optional[int] = Field(None, title='Tier')
    uniqueObjectID: str = Field(..., title='Uniqueobjectid')
    targetReady: bool = Field(..., title='Targetready')
    reeferStatus: Optional[str] = Field(None, title='Reeferstatus')
    relativePos: str = Field(..., title='Relativepos')
    destDoorDirection: str = Field(..., title='Destdoordirection')
    containerNum: Optional[str] = Field(None, title='Containernum')
    containerISO: str = Field(..., title='Containeriso')
    containerLengthFT: float = Field(..., title='Containerlengthft')
    containerHeight: float = Field(..., title='Containerheight')
    containerWeightKG: float = Field(..., title='Containerweightkg')
    containerWidth: Optional[float] = Field(None, title='Containerwidth')
    associatedTwinContainer_id: Optional[str] = Field(
        None, title='Associatedtwincontainer Id'
    )


class PortLocation(BaseModel):
    portX: Optional[float] = Field(None, title='Portx')
    portY: Optional[float] = Field(None, title='Porty')


class StageData(BaseModel):
    job_status: str = Field(..., title='Job Status')
    job_lane: str = Field(..., title='Job Lane')


class Status(Enum):
    OK = 'OK'
    FAIL = 'FAIL'


class TOSOrderUpdate(BaseModel):
    messageName: Optional[str] = Field('TOSOrderUpdate', title='Messagename')
    messageUniqueID: str = Field(..., title='Messageuniqueid')
    timestamp: str = Field(..., title='Timestamp')
    updateOrderOperationType: str = Field(..., title='Updateorderoperationtype')
    updateOrderUniqueID: str = Field(..., title='Updateorderuniqueid')
    updateOrderStatus: bool = Field(..., title='Updateorderstatus')


class TeleoperatorAssistance(Enum):
    PICKUP = 'PICKUP'
    GROUND = 'GROUND'
    PICKUP_AND_GROUND = 'PICKUP_AND_GROUND'


class ValidationError(BaseModel):
    loc: List[Union[str, int]] = Field(..., title='Location')
    msg: str = Field(..., title='Message')
    type: str = Field(..., title='Error Type')


class ActionCodeResponse(BaseModel):
    messageName: Optional[str] = Field('ActionCodeResponse', title='Messagename')
    messageUniqueId: str = Field(..., title='Messageuniqueid')
    messageTimestamp: str = Field(..., title='Messagetimestamp')
    buffer: bool = Field(..., title='Buffer')
    deliveryStatus: str = Field(..., title='Deliverystatus')
    locationCheck: LocationCheck


class ContainerDefinition(BaseModel):
    uniqueObjectID: str = Field(..., title='Uniqueobjectid')
    number: Optional[str] = Field(None, title='Number')
    logicalLocation: Origin
    portLocation: PortLocation
    ISO: Optional[str] = Field(None, title='Iso')
    length: Optional[float] = Field(None, title='Length')
    width: Optional[float] = Field(None, title='Width')
    height: Optional[float] = Field(None, title='Height')
    weight: float = Field(..., title='Weight')
    relativePos: str = Field(..., title='Relativepos')
    targetReady: bool = Field(..., title='Targetready')
    reeferStatus: Optional[str] = Field(None, title='Reeferstatus')
    associatedTwinContainer_1: Optional[str] = Field(
        None, title='Associatedtwincontainer 1'
    )
    associatedTwinContainer_2: Optional[str] = Field(
        None, title='Associatedtwincontainer 2'
    )


class DependencyCheckResponse(BaseModel):
    messageName: str = Field(..., title='Messagename')
    messageUniqueID: str = Field(..., title='Messageuniqueid')
    timeStamp: str = Field(..., title='Timestamp')
    dependencyList: Dict[str, DependencyItem] = Field(..., title='Dependencylist')


class DependencyInfo(BaseModel):
    movementUniqueID: str = Field(..., title='Movementuniqueid')
    origin: Origin
    destination: Destination
    containerNumber: str = Field(..., title='Containernumber')


class ExecutorDestination(BaseModel):
    logicalLocation: ExecutorLogicalLocation
    portLocation: Optional[ExecutorPortLocation] = None


class HTTPValidationError(BaseModel):
    detail: Optional[List[ValidationError]] = Field(None, title='Detail')


class MovementInstruction(BaseModel):
    movementUniqueID: str = Field(..., title='Movementuniqueid')
    movementStatus: str = Field(..., title='Movementstatus')
    messageSequence: int = Field(..., title='Messagesequence')
    workQueueName: str = Field(..., title='Workqueuename')
    movementType: str = Field(..., title='Movementtype')
    twinPickupGap: Optional[int] = Field(None, title='Twinpickupgap')
    twinGroundingGap: Optional[int] = Field(None, title='Twingroundinggap')
    equipmentName: Optional[str] = Field(None, title='Equipmentname')
    teleoperatorAssistance: Optional[TeleoperatorAssistance] = None
    origin: Origin
    destination: Destination
    originStartTime: str = Field(..., title='Originstarttime')
    containerDetails: Optional[ContainerDefinition] = None
    associatedTwinMove: Optional[str] = Field(None, title='Associatedtwinmove')
    movementDependencies: Optional[List[DependencyDefinition]] = Field(
        None, title='Movementdependencies'
    )


class MovementInstructionStatus(BaseModel):
    movementUniqueID: str = Field(..., title='Movementuniqueid')
    status: Status
    equipmentName: Optional[str] = Field(None, title='Equipmentname')
    rejectCode: Optional[List[str]] = Field(None, title='Rejectcode')
    rejectReason: Optional[List[str]] = Field(None, title='Rejectreason')


class MovementInstructions(BaseModel):
    messageUniqueID: str = Field(..., title='Messageuniqueid')
    messageName: str = Field(..., title='Messagename')
    timeStamp: str = Field(..., title='Timestamp')
    messageSource: str = Field(..., title='Messagesource')
    movementInstructions: List[MovementInstruction] = Field(
        ..., title='Movementinstructions'
    )


class VehicleOrder(BaseModel):
    messageName: Optional[str] = Field('VehicleOrder', title='Messagename')
    messageUniqueId: Optional[str] = Field(None, title='Messageuniqueid')
    messageTimestamp: Optional[str] = Field(None, title='Messagetimestamp')
    moveType: Optional[MoveType] = None
    uniqueOrderID: str = Field(..., title='Uniqueorderid')
    origin: str = Field(..., title='Origin')
    jobType: JobType
    vehicleID: str = Field(..., title='Vehicleid')
    bidirection: Optional[int] = Field(None, title='Bidirection')
    job_content: Optional[JobContent] = None
    movementType: Optional[MovementType] = None
    destination: Optional[ExecutorDestination] = None
    plannedContainerDestinationList: Optional[List[PlannedContainerDestinationDict]] = (
        Field(None, title='Plannedcontainerdestinationlist')
    )
    actionCode: Optional[str] = Field(None, title='Actioncode')
    stageData: Optional[StageData] = None


class WorkQueueInfo(BaseModel):
    work_queue: str = Field(..., title='Work Queue')
    tos_to_scheduler_dependency_list: List[DependencyInfo] = Field(
        ..., title='Tos To Scheduler Dependency List'
    )


class DependencyCheck(BaseModel):
    messageName: Optional[str] = Field('dependencyCheck', title='Messagename')
    messageUniqueID: str = Field(..., title='Messageuniqueid')
    movementInstructions: List[WorkQueueInfo] = Field(..., title='Movementinstructions')


class MovementCreatedResponse(BaseModel):
    messageName: Optional[str] = Field('MovementCreatedResponse', title='Messagename')
    messageUniqueID: str = Field(..., title='Messageuniqueid')
    timeStamp: str = Field(..., title='Timestamp')
    stopStatus: Optional[bool] = Field(None, title='Stopstatus')
    movementInstructionStatus: List[MovementInstructionStatus] = Field(
        ..., title='Movementinstructionstatus'
    )
