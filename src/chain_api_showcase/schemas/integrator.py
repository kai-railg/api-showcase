# generated by datamodel-codegen:
#   filename:  integrator.json
#   timestamp: 2024-03-18T08:09:31+00:00

from __future__ import annotations

from typing import Any, List, Optional, Union

from pydantic import BaseModel, Field


class EventCallback(BaseModel):
    event_name: str = Field(..., description='事件类型名称', title='Event Name')


class StdRes(BaseModel):
    data: Optional[Any] = Field(None, title='Data')
    code: Optional[int] = Field(200, title='Code')
    msg: Optional[str] = Field('success', title='Msg')


class ValidationError(BaseModel):
    loc: List[Union[str, int]] = Field(..., title='Location')
    msg: str = Field(..., title='Message')
    type: str = Field(..., title='Error Type')


class HTTPValidationError(BaseModel):
    detail: Optional[List[ValidationError]] = Field(None, title='Detail')
