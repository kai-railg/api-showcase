# generated by datamodel-codegen:
#   filename:  tos_interface.json
#   timestamp: 2024-03-06T08:20:34+00:00

from __future__ import annotations

from typing import List, Optional, Union

from pydantic import BaseModel, Field


class AreaAvailabilityUpdated(BaseModel):
    messageID: str = Field(..., title='Messageid')
    messageName: str = Field(..., title='Messagename')
    AreaStatusEvent_type: str = Field(..., title='Areastatusevent Type')
    Area_type: str = Field(..., title='Area Type')
    status: str = Field(..., title='Status')
    Position_list: List = Field(..., title='Position List')


class AreaInventoryQuery(BaseModel):
    messageID: str = Field(..., title='Messageid')
    messageName: str = Field(..., title='Messagename')
    timeStamp: str = Field(..., title='Timestamp')
    InventoryStatusQueryEvent_type: str = Field(
        ..., title='Inventorystatusqueryevent Type'
    )
    Area_type: str = Field(..., title='Area Type')
    Position_type: str = Field(..., title='Position Type')
    block: str = Field(..., title='Block')


class BodyGuiImportInventoryUploadGuiInventoryPost(BaseModel):
    uploadfile: bytes = Field(..., title='Uploadfile')


class BodyImportInstructionUploadWorkInstructionPost(BaseModel):
    uploadfile: bytes = Field(..., title='Uploadfile')


class BodyImportInventoryUploadWorkInventoryPost(BaseModel):
    uploadfile: bytes = Field(..., title='Uploadfile')


class BodyImportQueueUploadWorkQueuePost(BaseModel):
    uploadfile: bytes = Field(..., title='Uploadfile')


class ButtonSend(BaseModel):
    task_name: str = Field(..., title='Task Name')


class ContainerUpdate(BaseModel):
    messageID: str = Field(..., title='Messageid')
    messageName: str = Field(..., title='Messagename')
    InventoryStatusEvent_type: str = Field(..., title='Inventorystatusevent Type')
    uid: str = Field(..., title='Uid')
    number: str = Field(..., title='Number')
    ISO: str = Field(..., title='Iso')
    isoLenFt: str = Field(..., title='Isolenft')
    length: str = Field(..., title='Length')
    width: str = Field(..., title='Width')
    height: str = Field(..., title='Height')
    weight: str = Field(..., title='Weight')
    Position_type: str = Field(..., title='Position Type')
    area: str = Field(..., title='Area')
    lane: str = Field(..., title='Lane')
    offsetMm: str = Field(..., title='Offsetmm')
    orientation: str = Field(..., title='Orientation')


class InventoryImportDegree(BaseModel):
    msg: str = Field(..., title='Msg')
    code: Optional[int] = Field(200, title='Code')


class Login(BaseModel):
    user_name: str = Field(..., title='User Name')
    password: str = Field(..., title='Password')


class ScStatus(BaseModel):
    vehicle_id: str = Field(..., title='Vehicle Id')
    mode: str = Field(..., title='Mode')


class ValidationError(BaseModel):
    loc: List[Union[str, int]] = Field(..., title='Location')
    msg: str = Field(..., title='Message')
    type: str = Field(..., title='Error Type')


class WaCancelledResponse(BaseModel):
    messageID: str = Field(..., title='Messageid')
    messageName: str = Field(..., title='Messagename')
    status: str = Field(..., title='Status')
    name: str = Field(..., title='Name')
    equipType: str = Field(..., title='Equiptype')
    AckMessage_code: str = Field(..., title='Ackmessage Code')


class WaCreatedResponse(BaseModel):
    messageID: str = Field(..., title='Messageid')
    timeStamp: str = Field(..., title='Timestamp')
    pong: str = Field(..., title='Pong')
    messageUniqueID: str = Field(..., title='Messageuniqueid')
    messageName: str = Field(..., title='Messagename')
    AckEvent_type: str = Field(..., title='Ackevent Type')
    status: str = Field(..., title='Status')


class HTTPValidationError(BaseModel):
    detail: Optional[List[ValidationError]] = Field(None, title='Detail')
