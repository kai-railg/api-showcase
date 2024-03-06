# generated by datamodel-codegen:
#   filename:  inventory.json
#   timestamp: 2024-03-06T08:28:03+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Extra, Field


class ContainerCommonInfoSchema(BaseModel):
    message_name: Optional[str] = Field(None, title='Message Name')


class ContainerDBSchema(BaseModel):
    number: Optional[str] = Field('', title='Number')
    unique_id: Optional[str] = Field('', title='Unique Id')
    iso: Optional[str] = Field('', title='Iso')
    length: Optional[int] = Field(0, title='Length')
    width: Optional[int] = Field(0, title='Width')
    height: Optional[int] = Field(0, title='Height')
    weight: Optional[int] = Field(0, title='Weight')
    fms_x: Optional[Union[str, float]] = Field('0.0', title='Fms X')
    fms_y: Optional[Union[str, float]] = Field('0.0', title='Fms Y')
    fms_z: Optional[Union[str, float]] = Field('0.0', title='Fms Z')
    orientation: Optional[str] = Field('', title='Orientation')
    fms_orientation: Optional[Union[str, float]] = Field('0.0', title='Fms Orientation')
    reefer_status: Optional[str] = Field('', title='Reefer Status')
    CanBeHandle: Optional[bool] = Field(True, title='Canbehandle')
    vendor: Optional[str] = Field('', title='Vendor')
    color: Optional[str] = Field('', title='Color')
    associated_twin_container_1: Optional[str] = Field(
        '', title='Associated Twin Container 1'
    )
    associated_twin_container_2: Optional[str] = Field(
        '', title='Associated Twin Container 2'
    )
    ExamImgs: Optional[str] = Field('', title='Examimgs')
    iso_complement_status: Optional[bool] = Field(False, title='Iso Complement Status')


class ContainerImportSchema(BaseModel):
    number: Optional[str] = Field('', title='Number')
    unique_id: Optional[str] = Field('', title='Unique Id')
    iso: Optional[str] = Field('', title='Iso')
    length: Optional[int] = Field(0, title='Length')
    width: Optional[int] = Field(0, title='Width')
    height: Optional[int] = Field(0, title='Height')
    weight: Optional[int] = Field(0, title='Weight')
    fms_x: Optional[Union[str, float]] = Field('0.0', title='Fms X')
    fms_y: Optional[Union[str, float]] = Field('0.0', title='Fms Y')
    fms_z: Optional[Union[str, float]] = Field('0.0', title='Fms Z')
    orientation: Optional[str] = Field('', title='Orientation')
    fms_orientation: Optional[Union[str, float]] = Field('0.0', title='Fms Orientation')
    reefer_status: Optional[str] = Field('', title='Reefer Status')
    CanBeHandle: Optional[bool] = Field(True, title='Canbehandle')
    vendor: Optional[str] = Field('', title='Vendor')
    color: Optional[str] = Field('', title='Color')
    associated_twin_container_1: Optional[str] = Field(
        '', title='Associated Twin Container 1'
    )
    associated_twin_container_2: Optional[str] = Field(
        '', title='Associated Twin Container 2'
    )
    ExamImgs: Optional[str] = Field('', title='Examimgs')
    iso_complement_status: Optional[bool] = Field(False, title='Iso Complement Status')
    flush: Optional[bool] = Field(False, title='Flush')


class ContainerQuerySchema(BaseModel):
    message_name: Optional[str] = Field(None, title='Message Name')
    data: Optional[Any] = Field(None, title='Data')


class EditContainerSchema(BaseModel):
    area: Optional[str] = Field('', title='Area')
    block: Optional[str] = Field('', title='Block')
    query_unique_id: Optional[str] = Field('', title='Query Unique Id')
    container_number: Optional[str] = Field('', title='Container Number')
    orientation: Optional[str] = Field('', title='Orientation')
    stack: Optional[Union[int, str]] = Field(0, title='Stack')
    tier: Optional[Union[int, str]] = Field(0, title='Tier')


class GetAvailableTierSchema(BaseModel):
    area: str = Field(..., title='Area')
    block: str = Field(..., title='Block')
    lane: int = Field(..., title='Lane')
    stack: int = Field(..., title='Stack')


class GetContainerPointsSchema(BaseModel):
    unique_id: Optional[Union[str, List]] = Field(None, title='Unique Id')
    number: Optional[Union[str, List]] = Field(None, title='Number')
    area: Optional[Union[str, List]] = Field(None, title='Area')
    block: Optional[Union[str, List]] = Field(None, title='Block')
    lane: Optional[Union[int, List]] = Field(None, title='Lane')
    stack: Optional[Union[int, List]] = Field(None, title='Stack')
    tier: Optional[Union[int, List]] = Field(None, title='Tier')
    points: Optional[List[float]] = Field(None, title='Points')
    total_container: Optional[bool] = Field(False, title='Total Container')


class JobTypeEnum(Enum):
    pickup = 'pickup'
    ground = 'ground'


class LimitLowSchema(BaseModel):
    blocks: List[str] = Field(..., title='Blocks')


class MoveMentEnum(Enum):
    single = 'single'
    twin = 'twin'
    twinform = 'twinform'


class PosDataDBSchema(BaseModel):
    area: Optional[str] = Field('', title='Area')
    block: Optional[str] = Field('', title='Block')
    lane: Optional[int] = Field(1, title='Lane')
    tier: Optional[int] = Field(1, title='Tier')
    stack: Optional[int] = Field(0, title='Stack')
    fms_x: Optional[str] = Field('', title='Fms X')
    fms_y: Optional[str] = Field('', title='Fms Y')
    fms_z: Optional[str] = Field('', title='Fms Z')


class PositionAndContainer(BaseModel):
    position: Optional[PosDataDBSchema]
    container: Optional[ContainerDBSchema]


class PositionImportSchema(BaseModel):
    area: Optional[str] = Field('', title='Area')
    block: Optional[str] = Field('', title='Block')
    lane: Optional[int] = Field(1, title='Lane')
    tier: Optional[int] = Field(1, title='Tier')
    stack: Optional[int] = Field(0, title='Stack')
    fms_x: Optional[str] = Field('', title='Fms X')
    fms_y: Optional[str] = Field('', title='Fms Y')
    fms_z: Optional[str] = Field('', title='Fms Z')
    pos_data_id: Optional[int] = Field(None, title='Pos Data Id')


class PositionWithoutTierSchema(BaseModel):
    area: Optional[str] = Field('', title='Area')
    block: Optional[str] = Field('', title='Block')
    lane: Optional[Union[str, int]] = Field('', title='Lane')
    stack: Optional[Union[str, int]] = Field('', title='Stack')


class QcLeaveNotifySchema(BaseModel):
    block: str = Field(..., title='Block')


class RemoveContainerSchema(BaseModel):
    unique_id: Optional[Union[str, List]] = Field(None, title='Unique Id')
    number: Optional[Union[str, List]] = Field(None, title='Number')
    area: Optional[Union[str, List]] = Field(None, title='Area')
    block: Optional[Union[str, List]] = Field(None, title='Block')
    lane: Optional[Union[int, List]] = Field(None, title='Lane')
    stack: Optional[Union[int, List]] = Field(None, title='Stack')
    tier: Optional[Union[int, List]] = Field(None, title='Tier')
    points: Optional[List[float]] = Field(None, title='Points')
    total_container: Optional[bool] = Field(False, title='Total Container')


class ResponseSuccess(BaseModel):
    class Config:
        extra = Extra.allow

    code: int = Field(..., title='Code')
    message: str = Field(..., title='Message')
    content: Union[List, Dict[str, Any]] = Field(..., title='Content')
    timeStamp: str = Field(..., title='Timestamp')


class SubPoints(BaseModel):
    x: float = Field(..., title='X')
    y: float = Field(..., title='Y')
    name: str = Field(..., title='Name')
    size: Optional[Union[str, int]] = Field(None, title='Size')
    area: Optional[str] = Field(None, title='Area')
    block: Optional[str] = Field(None, title='Block')
    lane: Optional[int] = Field(None, title='Lane')
    stack: Optional[int] = Field(None, title='Stack')


class SubTaskCheckSchema(BaseModel):
    position: Optional[PositionImportSchema]
    container: Optional[ContainerImportSchema]
    need_check: Optional[bool] = Field(True, title='Need Check')
    operation_type: Optional[str] = Field('', title='Operation Type')
    jobUniqueID: Optional[str] = Field('', title='Jobuniqueid')
    check_status: Optional[bool] = Field(False, title='Check Status')
    check_msg: Optional[str] = Field('', title='Check Msg')
    allow_send: Optional[bool] = Field(True, title='Allow Send')
    pos_data_obj: Optional[Any] = Field(None, title='Pos Data Obj')
    container_obj: Optional[Any] = Field(None, title='Container Obj')


class TGInitNotifySchema(BaseModel):
    truck_type: str = Field(..., title='Truck Type')
    lane: int = Field(..., title='Lane')


class TaskCheckSchema(BaseModel):
    tasks: Optional[List[SubTaskCheckSchema]] = Field([], title='Tasks')


class ValidationError(BaseModel):
    loc: List[Union[str, int]] = Field(..., title='Location')
    msg: str = Field(..., title='Message')
    type: str = Field(..., title='Error Type')


class AddPointSchema(BaseModel):
    version: Optional[str] = Field('20240306_081955', title='Version')
    points: List[SubPoints] = Field(..., title='Points')


class ContainerCheckSchema(BaseModel):
    containers: List[PositionAndContainer] = Field(..., title='Containers')
    movement: MoveMentEnum
    job_type: JobTypeEnum
    operator: Optional[str] = Field('FMS', title='Operator')
    vehicle_id: Optional[str] = Field('SC01', title='Vehicle Id')


class HTTPValidationError(BaseModel):
    detail: Optional[List[ValidationError]] = Field(None, title='Detail')


class InventoryUpdateSchema(BaseModel):
    containers: List[PositionAndContainer] = Field(..., title='Containers')
    operation_type: str = Field(..., title='Operation Type')
    message_name: Optional[str] = Field('InventoryUpdate', title='Message Name')
    vehicle_id: Optional[str] = Field('TOS', title='Vehicle Id')


class PositionAndContainerImport(BaseModel):
    position: Optional[PositionImportSchema]
    container: Optional[ContainerImportSchema]
    need_check: Optional[bool] = Field(True, title='Need Check')


class ImportContainersSchema(BaseModel):
    containers: List[PositionAndContainerImport] = Field(..., title='Containers')
