# generated by datamodel-codegen:
#   filename:  gui_server.json
#   timestamp: 2024-03-26T08:59:05+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field


class BodyDenmarkinfoImportContainersPost(BaseModel):
    files: List[bytes] = Field(..., title='Files')


class BodyFileTransportUploadPost(BaseModel):
    files: List[bytes] = Field(..., title='Files')


class CRUDTwistlockStation(BaseModel):
    ts_name: str = Field(..., title='Ts Name')
    time_stamp: str = Field(..., title='Time Stamp')
    ts_creator: Optional[str] = Field('NPC', title='Ts Creator')
    ts_vessel: Optional[str] = Field('', title='Ts Vessel')
    job_type: Optional[str] = Field('', title='Job Type')
    ts_lane: Optional[str] = Field('', title='Ts Lane')
    ts_qc: Optional[str] = Field('', title='Ts Qc')
    ts_bollard: Optional[str] = Field('', title='Ts Bollard')
    ts_offset_x: Optional[float] = Field(0, title='Ts Offset X')
    ts_reason: Optional[str] = Field('', title='Ts Reason')
    ts_status: Optional[str] = Field('on', title='Ts Status')


class ContainerSteupSchemas(BaseModel):
    time_stamp: str = Field(..., title='Time Stamp')
    operation_type: str = Field(..., title='Operation Type')
    vehicle_id: str = Field(..., title='Vehicle Id')
    unique_id: str = Field(..., title='Unique Id')
    number: str = Field(..., title='Number')
    containers: List = Field(..., title='Containers')


class CreateGroupInSchema(BaseModel):
    name: str = Field(..., description='用户组名称', title='Name')
    description: Optional[str] = Field(
        None, description='用户组描述', title='Description'
    )
    permission_list: Optional[List[int]] = Field(
        ..., description='拥有权限', title='Permission List'
    )


class CreateSuccessSchema(BaseModel):
    data: Any = Field(..., title='Data')
    code: int = Field(..., title='Code')
    msg: str = Field(..., title='Msg')
    error: str = Field(..., title='Error')


class CreateUserInSchema(BaseModel):
    username: str = Field(..., description='用户名', title='Username')
    password: str = Field(..., description='密码', title='Password')
    email: Optional[str] = Field(None, description='邮箱', title='Email')
    first_name: Optional[str] = Field(None, description='名', title='First Name')
    last_name: Optional[str] = Field(None, description='姓', title='Last Name')
    department: str = Field(..., description='部门', title='Department')
    group_id: int = Field(..., description='组id', title='Group Id')
    question1: Optional[str] = Field(None, description='问题1', title='Question1')
    question2: Optional[str] = Field(None, description='问题2', title='Question2')
    answer1: Optional[str] = Field(None, description='答案1', title='Answer1')
    answer2: Optional[str] = Field(None, description='答案2', title='Answer2')


class DelVesselSchemas(BaseModel):
    vesselVisitId: str = Field(..., title='Vesselvisitid')
    vesselName: str = Field(..., title='Vesselname')


class DeleteSuccessSchema(BaseModel):
    data: Any = Field(..., title='Data')
    code: int = Field(..., title='Code')
    msg: str = Field(..., title='Msg')
    error: str = Field(..., title='Error')


class EventReport(BaseModel):
    vehicleID: str = Field(..., title='Vehicleid')
    eventType: str = Field(..., title='Eventtype')
    origin: Optional[str] = Field('GUI', title='Origin')
    timeStamp: Optional[str] = Field('', title='Timestamp')
    data: Optional[Dict[str, Any]] = Field({}, title='Data')


class FailTaskSchemas(BaseModel):
    vehicle_id: str = Field(..., title='Vehicle Id')
    error_msg: str = Field(..., title='Error Msg')
    timestamp: Optional[str] = Field(
        None, description='消息发送时间', title='Timestamp'
    )
    from_server: str = Field(..., title='From Server')
    code: Optional[int] = Field(None, title='Code')


class ForceOvertakeSchemas(BaseModel):
    vehicle_id: str = Field(..., title='Vehicle Id')
    overtake: int = Field(..., title='Overtake')


class GetAllMessageCSVSchemas(BaseModel):
    start_time: str = Field(..., title='Start Time')
    end_time: str = Field(..., title='End Time')
    messageType: Optional[str] = Field('null', title='Messagetype')
    truck_list: Optional[List] = Field([], title='Truck List')
    per_page: Optional[int] = Field(0, title='Per Page')
    page: Optional[int] = Field(0, title='Page')


class GetAllMessageSchemas(BaseModel):
    start_time: str = Field(..., title='Start Time')
    end_time: str = Field(..., title='End Time')
    messageType: str = Field(..., title='Messagetype')
    truck_list: Optional[List] = Field([], title='Truck List')
    per_page: Optional[int] = Field(10, title='Per Page')
    level: Optional[int] = Field(0, title='Level')
    page: Optional[int] = Field(1, title='Page')


class GetUserListOutWithGroup(BaseModel):
    id: Optional[int] = Field(..., description='id', title='Id')
    name: Optional[str] = Field(..., description='名称', title='Name')
    description: Optional[str] = Field(..., description='描述', title='Description')


class LoadFirstInSchema(BaseModel):
    vehicleID: str = Field(..., title='Vehicleid')
    overtakeLane: str = Field(..., title='Overtakelane')
    origin: str = Field(..., title='Origin')


class LoginInSchema(BaseModel):
    username: str = Field(..., description='用户名', title='Username')
    password: str = Field(..., description='密码', title='Password')


class PermissionBelongType(Enum):
    ART = 'ART'
    Berth = 'Berth'
    TS = 'TS'
    Charging = 'Charging'
    WFM = 'WFM'
    KPI = 'KPI'
    Warning = 'Warning'
    User = 'User'
    X_RAY = 'X-RAY'
    QC_RCH = 'QC_RCH'
    YARD_RCH = 'YARD_RCH'
    SPECIAl_RCH = 'SPECIAl_RCH'


class ReceiveDataType(Enum):
    json = 'json'
    list = 'list'


class ReceiveOperationType(Enum):
    create = 'create'
    update = 'update'
    delete = 'delete'


class RedoTaskInSchema(BaseModel):
    vehicleID: str = Field(..., title='Vehicleid')
    origin: str = Field(..., title='Origin')


class SetGhostVehicleCancelPost(BaseModel):
    vehicle_id: str = Field(..., title='Vehicle Id')
    manual_cancel: bool = Field(..., title='Manual Cancel')


class SetSwitchRequest(BaseModel):
    switch_val_name: str = Field(..., title='Switch Val Name')
    switch_val: str = Field(..., title='Switch Val')
    origin: Optional[str] = Field('', title='Origin')


class SetVesselSchemas(BaseModel):
    vesselVisitId: str = Field(..., title='Vesselvisitid')
    vesselName: str = Field(..., title='Vesselname')
    inVyg: str = Field(..., title='Invyg')
    outVyg: str = Field(..., title='Outvyg')
    bollardFore: int = Field(..., title='Bollardfore')
    bollardAfter: int = Field(..., title='Bollardafter')
    vessel_type: str = Field(..., title='Vessel Type')
    at_list: List = Field(..., title='At List')
    QCAG: List = Field(..., title='Qcag')
    ETA: str = Field(..., title='Eta')
    ETB: Optional[str] = Field('', title='Etb')
    ETD: str = Field(..., title='Etd')
    rta_time: str = Field(..., title='Rta Time')


class UpdateALlInfoSchemas(BaseModel):
    pile_info_all_code: int = Field(..., title='Pile Info All Code')


class UpdateGroupInSchema(BaseModel):
    name: Optional[str] = Field(None, description='用户组名称', title='Name')
    description: Optional[str] = Field(
        None, description='用户组描述', title='Description'
    )
    permission_list: Optional[List[int]] = Field(
        ..., description='拥有权限', title='Permission List'
    )


class UpdateGroupOutPermission(BaseModel):
    id: int = Field(..., title='Id')
    name: str = Field(..., title='Name')
    code: str = Field(..., title='Code')
    belong_type: str = Field(..., title='Belong Type')


class UpdatePasswdInSchema(BaseModel):
    old_password: str = Field(..., description='原密码', title='Old Password')
    new_password: str = Field(..., description='新密码', title='New Password')


class UpdatePermissionInSchema(BaseModel):
    name: Optional[str] = Field(None, description='权限名称', title='Name')
    description: Optional[str] = Field(
        None, description='权限描述', title='Description'
    )
    belong_type: Optional[PermissionBelongType] = Field(None, description='权限类型')
    request_type: Optional[str] = Field(
        None, description='请求类型', title='Request Type'
    )
    path: Optional[str] = Field(None, description='请求路径', title='Path')
    method: Optional[str] = Field(None, description='请求方法/消息名称', title='Method')


class UpdatePermissionOut(BaseModel):
    id: int = Field(..., title='Id')
    name: str = Field(..., title='Name')
    code: str = Field(..., title='Code')
    description: str = Field(..., title='Description')
    belong_type: PermissionBelongType
    request_type: str = Field(..., description='请求类型', title='Request Type')
    path: str = Field(..., description='请求路径', title='Path')
    method: str = Field(..., description='请求方法/消息名称', title='Method')


class UpdatePermissionOutSchema(BaseModel):
    data: UpdatePermissionOut
    code: int = Field(..., title='Code')
    msg: str = Field(..., title='Msg')
    error: str = Field(..., title='Error')


class UpdatePileInfoSchemas(BaseModel):
    charging_station_id: str = Field(..., title='Charging Station Id')
    fms_code: int = Field(..., title='Fms Code')
    gun_id: Optional[str] = Field(None, title='Gun Id')
    gun_fms_code: Optional[int] = Field(None, title='Gun Fms Code')


class UpdateTaskSchema(BaseModel):
    qcId: Optional[str] = Field(None, title='Qcid')
    spreadSize: Optional[str] = Field(None, title='Spreadsize')
    vehicleID: str = Field(..., title='Vehicleid')
    origin: str = Field(..., title='Origin')


class UpdateUserInSchema(BaseModel):
    username: Optional[str] = Field(None, description='用户名', title='Username')
    email: Optional[str] = Field(None, description='邮箱', title='Email')
    first_name: Optional[str] = Field(None, description='名', title='First Name')
    last_name: Optional[str] = Field(None, description='姓', title='Last Name')
    department: Optional[str] = Field(None, description='部门', title='Department')
    group_id: Optional[int] = Field(None, description='组id', title='Group Id')
    question1: Optional[str] = Field(None, description='问题1', title='Question1')
    question2: Optional[str] = Field(None, description='问题2', title='Question2')
    answer1: Optional[str] = Field(None, description='答案1', title='Answer1')
    answer2: Optional[str] = Field(None, description='答案2', title='Answer2')


class UpdateUserOut(BaseModel):
    username: str = Field(..., description='用户名', title='Username')
    email: Optional[str] = Field(..., description='邮箱', title='Email')
    first_name: Optional[str] = Field(..., description='名', title='First Name')
    last_name: Optional[str] = Field(..., description='姓', title='Last Name')


class UpdateUserOutSchema(BaseModel):
    data: UpdateUserOut
    code: int = Field(..., title='Code')
    msg: str = Field(..., title='Msg')
    error: str = Field(..., title='Error')


class UserInfoSchema(BaseModel):
    id: Optional[int] = Field(..., description='普通用户自增主键', title='Id')
    username: Optional[str] = Field(..., description='用户名', title='Username')
    email: Optional[str] = Field(..., description='邮箱', title='Email')
    department: Optional[str] = Field(..., description='部门', title='Department')
    first_name: Optional[str] = Field(..., description='名', title='First Name')
    last_name: Optional[str] = Field(..., description='姓', title='Last Name')
    is_first_login: Optional[bool] = Field(
        ..., description='是否首次登录', title='Is First Login'
    )
    is_super: Optional[bool] = Field(
        ..., description='是否是超级管理员', title='Is Super'
    )
    group_id: int = Field(..., description='组id', title='Group Id')


class UserWithTokenInfoSchema(BaseModel):
    userinfo: Optional[UserInfoSchema]
    username: Optional[str] = Field(..., title='Username')
    access_token: str = Field(..., title='Access Token')
    expires_in: int = Field(
        ..., description='token有效期，单位:分钟', title='Expires In'
    )


class UserWithTokenOutResponseInfoSchema(BaseModel):
    data: UserWithTokenInfoSchema
    code: int = Field(..., title='Code')
    msg: str = Field(..., title='Msg')
    error: str = Field(..., title='Error')


class ValidationError(BaseModel):
    loc: List[Union[str, int]] = Field(..., title='Location')
    msg: str = Field(..., title='Message')
    type: str = Field(..., title='Error Type')


class CreatePermissionInSchema(BaseModel):
    name: str = Field(..., description='权限名称', title='Name')
    description: Optional[str] = Field(
        None, description='权限描述', title='Description'
    )
    belong_type: PermissionBelongType = Field(..., description='权限类型')
    request_type: Optional[str] = Field(
        'http', description='请求类型', title='Request Type'
    )
    path: str = Field(..., description='请求路径', title='Path')
    method: str = Field(..., description='请求方法/消息名称', title='Method')


class CurrentUserGroupPermission(BaseModel):
    id: Optional[int] = Field(..., description='权限id', title='Id')
    name: Optional[str] = Field(..., description='权限名称', title='Name')
    code: Optional[str] = Field(..., description='权限代码', title='Code')
    belong_type: Optional[PermissionBelongType] = Field(..., description='权限类型')


class GetPermissionAllOutSchema(BaseModel):
    data: List[UpdatePermissionOut] = Field(..., title='Data')
    code: int = Field(..., title='Code')
    msg: str = Field(..., title='Msg')
    error: str = Field(..., title='Error')
    total: int = Field(..., title='Total')
    pages: int = Field(..., title='Pages')


class GetPermissionListOutSchema(BaseModel):
    data: List[UpdatePermissionOut] = Field(..., title='Data')
    code: int = Field(..., title='Code')
    msg: str = Field(..., title='Msg')
    error: str = Field(..., title='Error')
    total: int = Field(..., title='Total')
    pages: int = Field(..., title='Pages')


class GetPermissionOutSchema(BaseModel):
    data: UpdatePermissionOut
    code: int = Field(..., title='Code')
    msg: str = Field(..., title='Msg')
    error: str = Field(..., title='Error')


class GetSelfOutWithGroupPermission(BaseModel):
    id: Optional[int] = Field(..., description='权限id', title='Id')
    name: Optional[str] = Field(..., description='权限名称', title='Name')
    code: Optional[str] = Field(..., description='权限代码', title='Code')
    belong_type: Optional[PermissionBelongType] = Field(..., description='权限类型')


class GetUserListOut(BaseModel):
    id: Optional[int] = Field(..., description='id', title='Id')
    username: Optional[str] = Field(..., description='用户名', title='Username')
    first_name: Optional[str] = Field(..., description='名', title='First Name')
    last_name: Optional[str] = Field(..., description='姓', title='Last Name')
    department: Optional[str] = Field(..., description='部门', title='Department')
    is_first_login: Optional[bool] = Field(
        ..., description='是否首次登录', title='Is First Login'
    )
    group: Optional[GetUserListOutWithGroup] = Field(..., description='组信息')
    last_login: Optional[datetime] = Field(
        ..., description='最后登录时间', title='Last Login'
    )
    last_logout: Optional[datetime] = Field(
        ..., description='最后登出时间', title='Last Logout'
    )


class GetUserListOutSchema(BaseModel):
    data: List[GetUserListOut] = Field(..., title='Data')
    code: int = Field(..., title='Code')
    msg: str = Field(..., title='Msg')
    error: str = Field(..., title='Error')
    total: int = Field(..., title='Total')
    pages: int = Field(..., title='Pages')


class HTTPValidationError(BaseModel):
    errors: Optional[List[ValidationError]] = Field(None, title='Errors')


class UpdateGroupOut(BaseModel):
    id: int = Field(..., description='id', title='Id')
    name: str = Field(..., description='用户组名称', title='Name')
    description: str = Field(..., description='用户组描述', title='Description')
    permissions: List[UpdateGroupOutPermission] = Field(
        ..., description='拥有权限', title='Permissions'
    )


class UpdateGroupOutSchema(BaseModel):
    data: UpdateGroupOut
    code: int = Field(..., title='Code')
    msg: str = Field(..., title='Msg')
    error: str = Field(..., title='Error')


class CurrentUserGroupOut(BaseModel):
    id: Optional[int] = Field(..., description='id', title='Id')
    name: Optional[str] = Field(..., description='名称', title='Name')
    description: Optional[str] = Field(..., description='描述', title='Description')
    permissions: Optional[List[CurrentUserGroupPermission]] = Field(
        ..., title='Permissions'
    )


class GetGroupAllOutSchema(BaseModel):
    data: List[UpdateGroupOut] = Field(..., title='Data')
    code: int = Field(..., title='Code')
    msg: str = Field(..., title='Msg')
    error: str = Field(..., title='Error')
    total: int = Field(..., title='Total')
    pages: int = Field(..., title='Pages')


class GetGroupOut(BaseModel):
    username: str = Field(..., description='用户名', title='Username')
    email: Optional[str] = Field(..., description='邮箱', title='Email')
    first_name: Optional[str] = Field(..., description='名', title='First Name')
    last_name: Optional[str] = Field(..., description='姓', title='Last Name')
    department: str = Field(..., description='部门', title='Department')
    group: CurrentUserGroupOut


class GetGroupOutSchema(BaseModel):
    data: Optional[GetGroupOut]
    code: int = Field(..., title='Code')
    msg: str = Field(..., title='Msg')
    error: str = Field(..., title='Error')


class GetSelfOutWithGroup(BaseModel):
    id: Optional[int] = Field(..., description='id', title='Id')
    name: Optional[str] = Field(..., description='名称', title='Name')
    description: Optional[str] = Field(..., description='描述', title='Description')
    permissions: Optional[List[GetSelfOutWithGroupPermission]] = Field(
        ..., title='Permissions'
    )


class GetUserAllOutSchema(BaseModel):
    data: List[GetUserListOut] = Field(..., title='Data')
    code: int = Field(..., title='Code')
    msg: str = Field(..., title='Msg')
    error: str = Field(..., title='Error')
    total: int = Field(..., title='Total')
    pages: int = Field(..., title='Pages')


class GetUserOut(BaseModel):
    id: int = Field(..., title='Id')
    username: str = Field(..., title='Username')
    email: str = Field(..., title='Email')
    department: str = Field(..., title='Department')
    first_name: str = Field(..., title='First Name')
    last_name: str = Field(..., title='Last Name')
    group_id: int = Field(..., title='Group Id')
    is_active: bool = Field(..., title='Is Active')
    last_login: datetime = Field(..., title='Last Login')
    last_logout: datetime = Field(..., title='Last Logout')
    create_id: int = Field(..., title='Create Id')
    update_id: int = Field(..., title='Update Id')
    create_time: datetime = Field(..., title='Create Time')
    update_time: datetime = Field(..., title='Update Time')
    is_first_login: Optional[bool] = Field(..., title='Is First Login')
    super: Optional[bool] = Field(..., title='Super')
    group: CurrentUserGroupOut


class GetUserOutSchema(BaseModel):
    data: GetUserOut
    code: int = Field(..., title='Code')
    msg: str = Field(..., title='Msg')
    error: str = Field(..., title='Error')


class GetSelfOut(BaseModel):
    id: Optional[int] = Field(..., description='id', title='Id')
    username: Optional[str] = Field(..., description='用户名', title='Username')
    super: Optional[bool] = Field(..., description='是否为超级管理员', title='Super')
    first_name: Optional[str] = Field(..., description='名', title='First Name')
    last_name: Optional[str] = Field(..., description='姓', title='Last Name')
    department: Optional[str] = Field(..., description='部门', title='Department')
    last_login: Optional[datetime] = Field(
        ..., description='最后登录时间', title='Last Login'
    )
    last_logout: Optional[datetime] = Field(
        ..., description='最后登出时间', title='Last Logout'
    )
    group: Optional[GetSelfOutWithGroup] = Field(..., description='组信息')


class GetSelfOutSchema(BaseModel):
    data: GetSelfOut
