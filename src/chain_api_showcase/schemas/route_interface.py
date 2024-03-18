# generated by datamodel-codegen:
#   filename:  route_interface.json
#   timestamp: 2024-03-18T08:32:10+00:00

from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field


class EndPose(BaseModel):
    x: float = Field(..., title='X')
    y: float = Field(..., title='Y')
    heading: float = Field(..., title='Heading')
    bidirection: Optional[int] = Field(0, title='Bidirection')


class StartPose(BaseModel):
    x: float = Field(..., title='X')
    y: float = Field(..., title='Y')
    heading: float = Field(..., title='Heading')
    trailer_x: Optional[float] = Field(0, title='Trailer X')
    trailer_y: Optional[float] = Field(0, title='Trailer Y')
    trailer_heading: Optional[float] = Field(0, title='Trailer Heading')


class UpdateRequest(BaseModel):
    device_id: str = Field(..., title='Device Id')
    trans_id: str = Field(..., title='Trans Id')
    task_id: str = Field(..., title='Task Id')
    timestamp: int = Field(..., title='Timestamp')
    start_pose: StartPose
    end_pose: EndPose
    device_type: Optional[int] = Field(1, title='Device Type')
    traj_type: Optional[str] = Field('points', title='Traj Type')
    task_type: Optional[str] = Field('', title='Task Type')
    vessel_info: Optional[Dict[str, Any]] = Field({}, title='Vessel Info')
    passing_location: Optional[List] = Field([], title='Passing Location')
    arrive: Optional[bool] = Field(False, title='Arrive')


class ValidationError(BaseModel):
    loc: List[Union[str, int]] = Field(..., title='Location')
    msg: str = Field(..., title='Message')
    type: str = Field(..., title='Error Type')


class HTTPValidationError(BaseModel):
    detail: Optional[List[ValidationError]] = Field(None, title='Detail')
