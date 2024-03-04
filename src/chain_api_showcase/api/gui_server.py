# -*- coding: utf-8 -*-

import os
from typing import Union
from urllib import parse

from pydantic import BaseModel
from chain_http.async_client import (
    get as async_get,
    post as async_post,
    AsyncHttpResponse,
)

from ..schemas.gui_server import *

FMS_IP_ADDRESS = f"http://{os.environ.get('FMS_IP_ADDRESS', '127.0.0.1')}"


class Gui_ServerRequest(object):
    url = FMS_IP_ADDRESS + ":" + "8020"
    
    @classmethod
    async def authentication(cls, body: LoginInSchema) -> AsyncHttpResponse:
        """
        登录
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/authentication/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def auth(cls, ) -> AsyncHttpResponse:
        """
        获取个人信息
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/auth/"
            ),
            
        )
         
    @classmethod
    async def update_passwd(cls, body: UpdatePasswdInSchema,item_id: int) -> AsyncHttpResponse:
        """
        修改用户密码
        
        """
         
    @classmethod
    async def user(cls, body: CreateUserInSchema) -> AsyncHttpResponse:
        """
        创建用户
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/user/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def user_put(cls, body: UpdateUserInSchema,item_id: int) -> AsyncHttpResponse:
        """
        更新用户信息
        
        """
         
    @classmethod
    async def user_get(cls, item_id: int) -> AsyncHttpResponse:
        """
        获取单个用户信息
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/user/{item_id}"
            ),
            params=dict(item_id=item_id)
        )
         
    @classmethod
    async def user_delete(cls, item_id: int) -> AsyncHttpResponse:
        """
        删除用户
        
        """
         
    @classmethod
    async def list(cls, department: Union[str, None], group_id: Union[int, None], per_page: Union[int, None], page: Union[int, None]) -> AsyncHttpResponse:
        """
        分页检索
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/user/list"
            ),
            params=dict(department=department, group_id=group_id, per_page=per_page, page=page)
        )
         
    @classmethod
    async def all(cls, ) -> AsyncHttpResponse:
        """
        获取全部用户
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/user/all"
            ),
            
        )
         
    @classmethod
    async def group(cls, body: CreateGroupInSchema) -> AsyncHttpResponse:
        """
        创建组
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/group/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def group_put(cls, body: UpdateGroupInSchema,item_id: int) -> AsyncHttpResponse:
        """
        更新组
        
        """
         
    @classmethod
    async def group_get(cls, item_id: int) -> AsyncHttpResponse:
        """
        获取单个组
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/group/{item_id}"
            ),
            params=dict(item_id=item_id)
        )
         
    @classmethod
    async def group_delete(cls, item_id: int) -> AsyncHttpResponse:
        """
        删除组
        
        """
         
    @classmethod
    async def group_all_get(cls, ) -> AsyncHttpResponse:
        """
        获取所有组
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/group/all"
            ),
            
        )
         
    @classmethod
    async def permission(cls, body: CreatePermissionInSchema) -> AsyncHttpResponse:
        """
        创建权限
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/permission/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def permission_put(cls, body: UpdatePermissionInSchema,item_id: int) -> AsyncHttpResponse:
        """
        更新权限信息
        
        """
         
    @classmethod
    async def permission_get(cls, item_id: int) -> AsyncHttpResponse:
        """
        获取权限信息
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/permission/{item_id}"
            ),
            params=dict(item_id=item_id)
        )
         
    @classmethod
    async def permission_delete(cls, item_id: int) -> AsyncHttpResponse:
        """
        删除权限
        
        """
         
    @classmethod
    async def permission_all_get(cls, ) -> AsyncHttpResponse:
        """
        获取全部权限
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/permission/all"
            ),
            
        )
         
    @classmethod
    async def permission_list_get(cls, name: Union[str, None], belong_type: Union[PermissionBelongType, None], per_page: Union[int, None], page: Union[int, None]) -> AsyncHttpResponse:
        """
        分页检索
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/permission/list"
            ),
            params=dict(name=name, belong_type=belong_type, per_page=per_page, page=page)
        )
         
    @classmethod
    async def download(cls, file_name: str) -> AsyncHttpResponse:
        """
        文件下载
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/file_transport/download/{file_name}"
            ),
            params=dict(file_name=file_name)
        )
         
    @classmethod
    async def lockArea(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/lockArea/"
            ),
            
        )
         
    @classmethod
    async def api_taskInfo_lockArea_post(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/lockArea/"
            ),
            
            
        )
         
    @classmethod
    async def delete(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/lockArea/delete/"
            ),
            
        )
         
    @classmethod
    async def api_taskInfo_lockArea_delete_post(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/lockArea/delete/"
            ),
            
            
        )
         
    @classmethod
    async def deleteByTag(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/lockArea/deleteByTag/"
            ),
            
        )
         
    @classmethod
    async def api_taskInfo_lockArea_deleteByTag_post(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/lockArea/deleteByTag/"
            ),
            
            
        )
         
    @classmethod
    async def change(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/lockArea/change/"
            ),
            
        )
         
    @classmethod
    async def api_taskInfo_lockArea_change_post(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/lockArea/change/"
            ),
            
            
        )
         
    @classmethod
    async def resendJob(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/vehicleJob/resendJob/"
            ),
            
        )
         
    @classmethod
    async def api_taskInfo_vehicleJob_resendJob_post(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/vehicleJob/resendJob/"
            ),
            
            
        )
         
    @classmethod
    async def message_event_start_get(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/message_event/start/"
            ),
            
        )
         
    @classmethod
    async def message_event_start_post(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/message_event/start/"
            ),
            
            
        )
         
    @classmethod
    async def message_event_abort_get(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/message_event/abort/"
            ),
            
        )
         
    @classmethod
    async def message_event_abort_post(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/message_event/abort/"
            ),
            
            
        )
         
    @classmethod
    async def api_taskInfo_vehicleJob_delete_get(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/vehicleJob/delete/"
            ),
            
        )
         
    @classmethod
    async def api_taskInfo_vehicleJob_delete_post(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/vehicleJob/delete/"
            ),
            
            
        )
         
    @classmethod
    async def runImmediate(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/taskPool/runImmediate"
            ),
            
        )
         
    @classmethod
    async def api_taskInfo_taskPool_runImmediate_post(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/taskPool/runImmediate"
            ),
            
            
        )
         
    @classmethod
    async def api_taskInfo_taskPool_abort_get(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/taskPool/abort"
            ),
            
        )
         
    @classmethod
    async def api_taskInfo_taskPool_abort_post(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/taskPool/abort"
            ),
            
            
        )
         
    @classmethod
    async def trailerStatus(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/trailerStatus"
            ),
            
        )
         
    @classmethod
    async def api_deviceInfo_vehicleStatus_trailerStatus_post(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/trailerStatus"
            ),
            
            
        )
         
    @classmethod
    async def mode(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/mode"
            ),
            
        )
         
    @classmethod
    async def api_deviceInfo_vehicleStatus_mode_post(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/mode"
            ),
            
            
        )
         
    @classmethod
    async def containerInfo(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/containerInfo/"
            ),
            
        )
         
    @classmethod
    async def api_taskInfo_containerInfo_post(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/containerInfo/"
            ),
            
            
        )
         
    @classmethod
    async def message_event_rch_get(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/message_event/rch"
            ),
            
        )
         
    @classmethod
    async def message_event_rch_post(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/message_event/rch"
            ),
            
            
        )
         
    @classmethod
    async def query(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/fms/area/inventory/query/"
            ),
            
        )
         
    @classmethod
    async def fms_area_inventory_query_post(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/fms/area/inventory/query/"
            ),
            
            
        )
         
    @classmethod
    async def api_vehicleManager_power_get(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/power/"
            ),
            
        )
         
    @classmethod
    async def api_vehicleManager_power_post(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/power/"
            ),
            
            
        )
         
    @classmethod
    async def api_vehicleManager_handshake_get(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/handshake/"
            ),
            
        )
         
    @classmethod
    async def api_vehicleManager_handshake_post(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/handshake/"
            ),
            
            
        )
         
    @classmethod
    async def SetOperation(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/SetOperation"
            ),
            
        )
         
    @classmethod
    async def api_deviceInfo_vehicleStatus_SetOperation_post(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/SetOperation"
            ),
            
            
        )
         
    @classmethod
    async def api_vehicleManager_report_speed_ratio_get(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/report_speed_ratio/"
            ),
            
        )
         
    @classmethod
    async def api_vehicleManager_report_speed_ratio_post(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/report_speed_ratio/"
            ),
            
            
        )
         
    @classmethod
    async def api_container_InventoryUpdate_get(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/container/InventoryUpdate"
            ),
            
        )
         
    @classmethod
    async def api_container_InventoryUpdate_post(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/container/InventoryUpdate"
            ),
            
            
        )
         
    @classmethod
    async def SetVesselInfoStatus(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/VesselInfo/SetVesselInfoStatus"
            ),
            
        )
         
    @classmethod
    async def api_taskInfo_VesselInfo_SetVesselInfoStatus_post(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/VesselInfo/SetVesselInfoStatus"
            ),
            
            
        )
         
    @classmethod
    async def query_all(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/vehicleJob/query_all/"
            ),
            
        )
         
    @classmethod
    async def api_taskInfo_vehicleJob_query_all_post(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/vehicleJob/query_all/"
            ),
            
            
        )
         
    @classmethod
    async def PaceGlobal(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/PaceGlobal/"
            ),
            
        )
         
    @classmethod
    async def api_taskInfo_PaceGlobal_post(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/PaceGlobal/"
            ),
            
            
        )
         
    @classmethod
    async def SetLane(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/quayCrane/SetLane/"
            ),
            
        )
         
    @classmethod
    async def api_taskInfo_quayCrane_SetLane_post(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/quayCrane/SetLane/"
            ),
            
            
        )
         
    @classmethod
    async def message_event_update_qc_task_get(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/message_event/update_qc_task/"
            ),
            
        )
         
    @classmethod
    async def message_event_update_qc_task_post(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/message_event/update_qc_task/"
            ),
            
            
        )
         
    @classmethod
    async def vehicleJob(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/vehicleJob/"
            ),
            
        )
         
    @classmethod
    async def api_taskInfo_vehicleJob_post(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/vehicleJob/"
            ),
            
            
        )
         
    @classmethod
    async def all_current_job(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/vehicleJob/all_current_job/"
            ),
            
        )
         
    @classmethod
    async def api_taskInfo_vehicleJob_all_current_job_post(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/vehicleJob/all_current_job/"
            ),
            
            
        )
         
    @classmethod
    async def api_container_EditContainers_get(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/container/EditContainers"
            ),
            
        )
         
    @classmethod
    async def api_container_EditContainers_post(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/container/EditContainers"
            ),
            
            
        )
         
    @classmethod
    async def api_vehicleManager_stop_get(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/stop/"
            ),
            
        )
         
    @classmethod
    async def api_vehicleManager_stop_post(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/stop/"
            ),
            
            
        )
         
    @classmethod
    async def engine(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/engine"
            ),
            
        )
         
    @classmethod
    async def api_engine_post(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/engine"
            ),
            
            
        )
         
    @classmethod
    async def response_mixed_area(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/response_mixed_area"
            ),
            
        )
         
    @classmethod
    async def api_response_mixed_area_post(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/response_mixed_area"
            ),
            
            
        )
         
    @classmethod
    async def points(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/points"
            ),
            
        )
         
    @classmethod
    async def api_vehicleManager_points_post(cls, ) -> AsyncHttpResponse:
        """
        Api Proxy
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/vehicleManager/points"
            ),
            
            
        )
         
    @classmethod
    async def SetVesselInfo(cls, body: SetVesselSchemas) -> AsyncHttpResponse:
        """
        创建船舶
        船头大于船尾左
船尾大于船头右
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/VesselInfo/SetVesselInfo"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def ReleaseVesselInfo(cls, body: DelVesselSchemas) -> AsyncHttpResponse:
        """
        删除船
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/VesselInfo/ReleaseVesselInfo"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def GetBertNO(cls, response_data_type: ReceiveDataType) -> AsyncHttpResponse:
        """
        获取泊位号
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/VesselInfo/GetBertNO"
            ),
            params=dict(response_data_type=response_data_type)
        )
         
    @classmethod
    async def EditVesselInfo(cls, body: object) -> AsyncHttpResponse:
        """
        修改船
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/VesselInfo/EditVesselInfo"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def ghostVehicleCancel(cls, body: SetGhostVehicleCancelPost) -> AsyncHttpResponse:
        """
        Gui-取消幽灵车
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/deviceInfo/vehicleStatus/ghostVehicleCancel"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def EquipmentStatus(cls, body: SetSwitchRequest) -> AsyncHttpResponse:
        """
        设置开关状态[Cps,Cms...]
        request_params:
    {
        "switch_val_name":"cms",
        "switch_val":"on"
    }
response_params:
    {
        "data": null,
        "code": 200,
        "msg": "success",
        "error": ""
    }
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/EquipmentStatus/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def SpreaderSize(cls, body: SetSwitchRequest) -> AsyncHttpResponse:
        """
        设置吊具尺寸
        request_params:
    {
        "switch_val_name":"Z11",
        "switch_val":"20"
    }
response_params:
    {
        "data": null,
        "code": 200,
        "msg": "success",
        "error": ""
    }
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/EquipmentStatus/SpreaderSize/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def GetAllMessage(cls, body: GetAllMessageSchemas) -> AsyncHttpResponse:
        """
        获取所有告警信息
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/message/GetAllMessage"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def GetFileMessage(cls, body: GetAllMessageCSVSchemas) -> AsyncHttpResponse:
        """
        获取历史故障信息文件
        导出告警信息csv
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/message/GetFileMessage"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def UpdatePileInfo(cls, body: UpdatePileInfoSchemas) -> AsyncHttpResponse:
        """
        单个充电桩操作
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/pileinfo/UpdatePileInfo"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def UpdateAllPileInfo(cls, body: UpdateALlInfoSchemas) -> AsyncHttpResponse:
        """
        所有充电桩操作
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/pileinfo/UpdateAllPileInfo"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def ContainerInfoSetup(cls, body: ContainerSteupSchemas) -> AsyncHttpResponse:
        """
        箱子增删改
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/denmarkinfo/ContainerInfoSetup"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def PlcStatus(cls, body: object) -> AsyncHttpResponse:
        """
        控制车辆应请
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/denmarkinfo/PlcStatus"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def ServerVersion(cls, ) -> AsyncHttpResponse:
        """
        所有服务版本号
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/denmarkinfo/ServerVersion"
            ),
            
        )
         
    @classmethod
    async def ForceOverTake(cls, body: ForceOvertakeSchemas) -> AsyncHttpResponse:
        """
        Over Take功能
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/TaskCorrelation/ForceOverTake/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def update_task(cls, body: UpdateTaskSchema) -> AsyncHttpResponse:
        """
        Update Task
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/TaskCorrelation/update_task"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def load_first(cls, body: LoadFirstInSchema) -> AsyncHttpResponse:
        """
        Load First
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/TaskCorrelation/load_first"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def redo_task(cls, body: RedoTaskInSchema) -> AsyncHttpResponse:
        """
        Redo Task
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/TaskCorrelation/redo_task"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def CollectionFailTask(cls, body: FailTaskSchemas) -> AsyncHttpResponse:
        """
        收集失败任务信息功能
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/TaskCorrelation/CollectionFailTask/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def TosLoginStatus(cls, body: object) -> AsyncHttpResponse:
        """
        Tos登录登出
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/TosLoginStatus/"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def twistlock_station(cls, body: CRUDTwistlockStation,operation_type: ReceiveOperationType) -> AsyncHttpResponse:
        """
        增删改锁站Ts信息
        CREATE / UPDATE  /  DELETE
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/twistlock_station/"
            ),
            json=body.dict(),
            params=dict(operation_type=operation_type)
        )
         
    @classmethod
    async def GetPtions(cls, ) -> AsyncHttpResponse:
        """
        获取堆场贝位以及岸桥车道
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/get_ptions/GetPtions"
            ),
            
            
        )
         