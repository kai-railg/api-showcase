# generated by datamodel-codegen:
#   filename:  crane_info.json
#   timestamp: 2024-03-04T06:22:18+00:00

from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field


class ApplicationLaneRequestModel(BaseModel):
    messageName: Optional[str] = Field('', title='Messagename')
    messageUniqueID: Optional[str] = Field(
        None, description='消息ID', title='Messageuniqueid'
    )
    messageTimestamp: Optional[str] = Field(
        None, description='消息发送时间', title='Messagetimestamp'
    )
    deviceId: int = Field(..., title='Deviceid')
    vehicleId: str = Field(..., title='Vehicleid')
    lane: int = Field(..., title='Lane')
    status: bool = Field(..., title='Status')


class CPSInfoRequestModel(BaseModel):
    messageName: Optional[str] = Field('CPSInfoReport', title='Messagename')
    messageUniqueID: Optional[str] = Field(
        None, description='消息ID', title='Messageuniqueid'
    )
    messageTimestamp: Optional[str] = Field(
        None, description='消息发送时间', title='Messagetimestamp'
    )
    vehicleID: str = Field(..., title='Vehicleid')
    deviceID: str = Field(..., title='Deviceid')
    offset: float = Field(..., title='Offset')
    status: int = Field(..., title='Status')


class CPSInfoResponseModel(BaseModel):
    code: int = Field(..., title='Code')
    msg: str = Field(..., title='Msg')
    error: str = Field(..., title='Error')


class CommonResponseModel(BaseModel):
    code: int = Field(..., title='Code')
    msg: str = Field(..., title='Msg')
    error: str = Field(..., title='Error')
    data: Dict[str, Any] = Field(..., title='Data')


class ContainerPointRequestModel(BaseModel):
    messageUniqueID: Optional[str] = Field(
        None, description='消息ID', title='Messageuniqueid'
    )
    messageTimestamp: Optional[str] = Field(
        None, description='消息发送时间', title='Messagetimestamp'
    )
    QcId: str = Field(..., title='Qcid')
    lane: str = Field(..., title='Lane')
    offset: float = Field(..., title='Offset')


class EngineRequestModel(BaseModel):
    messageUniqueID: Optional[str] = Field(
        None, description='消息ID', title='Messageuniqueid'
    )
    messageTimestamp: Optional[str] = Field(
        None, description='消息发送时间', title='Messagetimestamp'
    )
    node: str = Field(..., title='Node')
    vehicleId: str = Field(..., title='Vehicleid')
    value: bool = Field(..., title='Value')


class MixedAreaRequestModel(BaseModel):
    messageUniqueID: Optional[str] = Field(
        None, description='消息ID', title='Messageuniqueid'
    )
    messageTimestamp: Optional[str] = Field(
        None, description='消息发送时间', title='Messagetimestamp'
    )
    messageNumber: int = Field(..., title='Messagenumber')
    value: bool = Field(..., title='Value')


class PlcDataRequestModel(BaseModel):
    messageName: Optional[str] = Field('', title='Messagename')
    messageUniqueID: Optional[str] = Field(
        None, description='消息ID', title='Messageuniqueid'
    )
    messageTimestamp: Optional[str] = Field(
        None, description='消息发送时间', title='Messagetimestamp'
    )
    deviceId: int = Field(..., title='Deviceid')
    content: Dict[str, Any] = Field(..., title='Content')


class QCHoldingRequestModel(BaseModel):
    messageName: Optional[str] = Field('', title='Messagename')
    messageUniqueID: Optional[str] = Field(
        None, description='消息ID', title='Messageuniqueid'
    )
    messageTimestamp: Optional[str] = Field(
        None, description='消息发送时间', title='Messagetimestamp'
    )
    deviceId: int = Field(..., title='Deviceid')
    lane: int = Field(..., title='Lane')
    lock: Optional[bool] = Field(None, title='Lock')


class QCPointRequestModel(BaseModel):
    messageName: Optional[str] = Field('', title='Messagename')
    messageUniqueID: Optional[str] = Field(
        None, description='消息ID', title='Messageuniqueid'
    )
    messageTimestamp: Optional[str] = Field(
        None, description='消息发送时间', title='Messagetimestamp'
    )
    deviceId: int = Field(..., title='Deviceid')
    lane: int = Field(..., title='Lane')


class QCSignalRequestModel(BaseModel):
    messageName: Optional[str] = Field('', title='Messagename')
    messageUniqueID: Optional[str] = Field(
        None, description='消息ID', title='Messageuniqueid'
    )
    messageTimestamp: Optional[str] = Field(
        None, description='消息发送时间', title='Messagetimestamp'
    )
    QcId: str = Field(..., title='Qcid')
    ActivityAction: str = Field(..., title='Activityaction')


class UpdatePlcDataModel(BaseModel):
    messageUniqueID: Optional[str] = Field(
        None, description='消息ID', title='Messageuniqueid'
    )
    messageTimestamp: Optional[str] = Field(
        None, description='消息发送时间', title='Messagetimestamp'
    )
    plcKey: str = Field(..., title='Plckey')
    plcValue: Any = Field(..., title='Plcvalue')


class UpdateQCPositionModel(BaseModel):
    messageUniqueID: Optional[str] = Field(
        None, description='消息ID', title='Messageuniqueid'
    )
    messageTimestamp: Optional[str] = Field(
        None, description='消息发送时间', title='Messagetimestamp'
    )
    x: int = Field(..., title='X')
    QcId: str = Field(..., title='Qcid')


class ValidationError(BaseModel):
    loc: List[Union[str, int]] = Field(..., title='Location')
    msg: str = Field(..., title='Message')
    type: str = Field(..., title='Error Type')


class HTTPValidationError(BaseModel):
    detail: Optional[List[ValidationError]] = Field(None, title='Detail')
