# generated by datamodel-codegen:
#   filename:  device_info.json
#   timestamp: 2024-03-14T07:59:38+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field


class BtnStatusSchemas(BaseModel):
    emergency_stop: str = Field(..., title='Emergency Stop')
    left_status: str = Field(..., title='Left Status')
    right_status: str = Field(..., title='Right Status')


class CreateSuccessSchema(BaseModel):
    data: Optional[Any] = Field(None, title='Data')
    code: Optional[int] = Field(200, title='Code')
    msg: Optional[str] = Field('success', title='Msg')
    error: Optional[str] = Field('', title='Error')


class GetPileInfoSchemas(BaseModel):
    message_name: str = Field(..., title='Message Name')
    charging_station_id: Optional[str] = Field(None, title='Charging Station Id')


class GhostStatus(Enum):
    ghost = 'ghost'
    normal = 'normal'


class LoginStatus(Enum):
    login = 'login'
    logout = 'logout'


class PileMessageSchemas(BaseModel):
    charging_station_id: str = Field(..., title='Charging Station Id')
    atID: str = Field(..., title='Atid')
    message: str = Field(..., title='Message')
    MessageId: str = Field(..., title='Messageid')


class Point(BaseModel):
    x: float = Field(..., title='X')
    y: float = Field(..., title='Y')
    theta: float = Field(..., title='Theta')


class Position(BaseModel):
    x: float = Field(..., title='X')
    y: float = Field(..., title='Y')
    z: float = Field(..., title='Z')
    theta: float = Field(..., title='Theta')
    v: float = Field(..., title='V')


class ReportStopTime(BaseModel):
    vehicle_id: str = Field(..., title='Vehicle Id')
    stop_time: Union[float, int] = Field(..., title='Stop Time')


class ReportSuspend(BaseModel):
    vehicle_id: str = Field(..., title='Vehicle Id')
    suspend_reason: List[int] = Field(..., title='Suspend Reason')
    suspend_time_stamp: Union[float, int] = Field(..., title='Suspend Time Stamp')


class SetGhostVehicleCancelPost(BaseModel):
    vehicle_id: str = Field(..., title='Vehicle Id')
    manual_cancel: bool = Field(..., title='Manual Cancel')


class SetGhostVehiclePost(BaseModel):
    vehicle_id: str = Field(..., title='Vehicle Id')
    ghost_status: GhostStatus
    position: Position


class SetLongPath(BaseModel):
    vehicle_id: str = Field(..., title='Vehicle Id')
    vehicle_mission_id: str = Field(..., title='Vehicle Mission Id')
    destination_type: str = Field(..., title='Destination Type')
    path: List[Point] = Field(..., title='Path')


class SetModePost(BaseModel):
    vehicle_id: str = Field(..., title='Vehicle Id')
    mode: str = Field(..., title='Mode')


class SetPileInfoAllSchemas(BaseModel):
    pile_info_all_code: int = Field(..., title='Pile Info All Code')


class SetPileInfoSchemas(BaseModel):
    pile_info_data: Dict[str, Any] = Field(..., title='Pile Info Data')


class SetShortPath(BaseModel):
    vehicle_id: str = Field(..., title='Vehicle Id')
    vehicle_mission_id: str = Field(..., title='Vehicle Mission Id')
    destination_type: str = Field(..., title='Destination Type')
    path: List[Point] = Field(..., title='Path')


class SetSocPost(BaseModel):
    vehicle_id: str = Field(..., title='Vehicle Id')
    fuel_type: str = Field(..., title='Fuel Type')
    battery_state: Optional[str] = Field('normal', title='Battery State')
    remaining_fuel_percentage: float = Field(..., title='Remaining Fuel Percentage')
    remaining_fuel_capacity: float = Field(..., title='Remaining Fuel Capacity')
    charge_status: str = Field(..., title='Charge Status')


class SetTrailerStatusPost(BaseModel):
    vehicle_id: str = Field(..., title='Vehicle Id')
    has_trailer: str = Field(..., title='Has Trailer')


class ValidationError(BaseModel):
    loc: List[Union[str, int]] = Field(..., title='Location')
    msg: str = Field(..., title='Message')
    type: str = Field(..., title='Error Type')


class VehicleType(Enum):
    QTRUCK = 'QTRUCK'
    ASC = 'ASC'
    IGV = 'IGV'


class HTTPValidationError(BaseModel):
    detail: Optional[List[ValidationError]] = Field(None, title='Detail')


class SetLoginStatusPost(BaseModel):
    vehicle_id: str = Field(..., title='Vehicle Id')
    status: LoginStatus
    vehicle_type: Optional[VehicleType] = None
