# -*- coding: utf-8 -*-

from typing import Union, Tuple, Dict
from urllib import parse

import requests
from pydantic import BaseModel
from chain_http.async_client import (
    get as async_get,
    post as async_post,
    put as async_put,
    delete as async_delete,
    AsyncHttpResponse,
)

from .api_base import ApiRequestBaseCls
from ..schemas.gui_server import *

__all__ = ["GuiServerRequest"]


class GuiServerRequestCls(ApiRequestBaseCls):
    def __init__(self):
        super(GuiServerRequestCls, self).__init__()
        self.SERVICE_PORT = 8020
        self.SERVICE_NAME = "gui_server"
        self.module_mapping[self.SERVICE_NAME] = self

    async def authentication(
        self, body: LoginInSchema
    ) -> Tuple[int, UserWithTokenOutResponseInfoSchema]:
        """
        登录

        """
        return await self.request(
            request=async_post,
            api="/authentication/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=UserWithTokenOutResponseInfoSchema,
        )

    def authentication_sync(
        self, body: LoginInSchema
    ) -> Tuple[int, UserWithTokenOutResponseInfoSchema]:
        """
        登录

        """
        return self.request_sync(
            request=requests.post,
            api="/authentication/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=UserWithTokenOutResponseInfoSchema,
        )

    async def auth(self) -> Tuple[int, GetSelfOutSchema]:
        """
        获取个人信息

        """
        return await self.request(
            request=async_get, api="/auth/", body={}, resp_model=GetSelfOutSchema
        )

    def auth_sync(self) -> Tuple[int, GetSelfOutSchema]:
        """
        获取个人信息

        """
        return self.request_sync(
            request=requests.get, api="/auth/", body={}, resp_model=GetSelfOutSchema
        )

    async def update_passwd(
        self, body: UpdatePasswdInSchema, item_id: int
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        修改用户密码

        """
        return await self.request(
            request=async_put,
            api="/auth/update_passwd/{item_id}",
            body={"data": body.model_dump_json(), "params": dict(item_id=item_id)},
            resp_model=CreateSuccessSchema,
        )

    def update_passwd_sync(
        self, body: UpdatePasswdInSchema, item_id: int
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        修改用户密码

        """
        return self.request_sync(
            request=requests.put,
            api="/auth/update_passwd/{item_id}",
            body={"data": body.model_dump_json(), "params": dict(item_id=item_id)},
            resp_model=CreateSuccessSchema,
        )

    async def user(self, body: CreateUserInSchema) -> Tuple[int, CreateSuccessSchema]:
        """
        创建用户

        """
        return await self.request(
            request=async_post,
            api="/user/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def user_sync(self, body: CreateUserInSchema) -> Tuple[int, CreateSuccessSchema]:
        """
        创建用户

        """
        return self.request_sync(
            request=requests.post,
            api="/user/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def user_put(
        self, body: UpdateUserInSchema, item_id: int
    ) -> Tuple[int, UpdateUserOutSchema]:
        """
        更新用户信息

        """
        return await self.request(
            request=async_put,
            api="/user/{item_id}",
            body={"data": body.model_dump_json(), "params": dict(item_id=item_id)},
            resp_model=UpdateUserOutSchema,
        )

    def user_put_sync(
        self, body: UpdateUserInSchema, item_id: int
    ) -> Tuple[int, UpdateUserOutSchema]:
        """
        更新用户信息

        """
        return self.request_sync(
            request=requests.put,
            api="/user/{item_id}",
            body={"data": body.model_dump_json(), "params": dict(item_id=item_id)},
            resp_model=UpdateUserOutSchema,
        )

    async def user_get(self, item_id: int) -> Tuple[int, GetUserOutSchema]:
        """
        获取单个用户信息

        """
        return await self.request(
            request=async_get,
            api="/user/{item_id}",
            body={"params": dict(item_id=item_id)},
            resp_model=GetUserOutSchema,
        )

    def user_get_sync(self, item_id: int) -> Tuple[int, GetUserOutSchema]:
        """
        获取单个用户信息

        """
        return self.request_sync(
            request=requests.get,
            api="/user/{item_id}",
            body={"params": dict(item_id=item_id)},
            resp_model=GetUserOutSchema,
        )

    async def user_delete(self, item_id: int) -> Tuple[int, DeleteSuccessSchema]:
        """
        删除用户

        """
        return await self.request(
            request=async_delete,
            api="/user/{item_id}",
            body={"params": dict(item_id=item_id)},
            resp_model=DeleteSuccessSchema,
        )

    def user_delete_sync(self, item_id: int) -> Tuple[int, DeleteSuccessSchema]:
        """
        删除用户

        """
        return self.request_sync(
            request=requests.delete,
            api="/user/{item_id}",
            body={"params": dict(item_id=item_id)},
            resp_model=DeleteSuccessSchema,
        )

    async def list(
        self,
        department: Union[str, None],
        group_id: Union[int, None],
        per_page: Union[int, None] = "20",
        page: Union[int, None] = "1",
    ) -> Tuple[int, GetUserListOutSchema]:
        """
        分页检索

        """
        return await self.request(
            request=async_get,
            api="/user/list",
            body={
                "params": dict(
                    department=department,
                    group_id=group_id,
                    per_page=per_page,
                    page=page,
                )
            },
            resp_model=GetUserListOutSchema,
        )

    def list_sync(
        self,
        department: Union[str, None],
        group_id: Union[int, None],
        per_page: Union[int, None] = "20",
        page: Union[int, None] = "1",
    ) -> Tuple[int, GetUserListOutSchema]:
        """
        分页检索

        """
        return self.request_sync(
            request=requests.get,
            api="/user/list",
            body={
                "params": dict(
                    department=department,
                    group_id=group_id,
                    per_page=per_page,
                    page=page,
                )
            },
            resp_model=GetUserListOutSchema,
        )

    async def all(self) -> Tuple[int, GetUserAllOutSchema]:
        """
        获取全部用户

        """
        return await self.request(
            request=async_get, api="/user/all", body={}, resp_model=GetUserAllOutSchema
        )

    def all_sync(self) -> Tuple[int, GetUserAllOutSchema]:
        """
        获取全部用户

        """
        return self.request_sync(
            request=requests.get,
            api="/user/all",
            body={},
            resp_model=GetUserAllOutSchema,
        )

    async def group(self, body: CreateGroupInSchema) -> Tuple[int, CreateSuccessSchema]:
        """
        创建组

        """
        return await self.request(
            request=async_post,
            api="/group/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def group_sync(self, body: CreateGroupInSchema) -> Tuple[int, CreateSuccessSchema]:
        """
        创建组

        """
        return self.request_sync(
            request=requests.post,
            api="/group/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def group_put(
        self, body: UpdateGroupInSchema, item_id: int
    ) -> Tuple[int, UpdateGroupOutSchema]:
        """
        更新组

        """
        return await self.request(
            request=async_put,
            api="/group/{item_id}",
            body={"data": body.model_dump_json(), "params": dict(item_id=item_id)},
            resp_model=UpdateGroupOutSchema,
        )

    def group_put_sync(
        self, body: UpdateGroupInSchema, item_id: int
    ) -> Tuple[int, UpdateGroupOutSchema]:
        """
        更新组

        """
        return self.request_sync(
            request=requests.put,
            api="/group/{item_id}",
            body={"data": body.model_dump_json(), "params": dict(item_id=item_id)},
            resp_model=UpdateGroupOutSchema,
        )

    async def group_get(self, item_id: int) -> Tuple[int, GetGroupOutSchema]:
        """
        获取单个组

        """
        return await self.request(
            request=async_get,
            api="/group/{item_id}",
            body={"params": dict(item_id=item_id)},
            resp_model=GetGroupOutSchema,
        )

    def group_get_sync(self, item_id: int) -> Tuple[int, GetGroupOutSchema]:
        """
        获取单个组

        """
        return self.request_sync(
            request=requests.get,
            api="/group/{item_id}",
            body={"params": dict(item_id=item_id)},
            resp_model=GetGroupOutSchema,
        )

    async def group_delete(self, item_id: int) -> Tuple[int, DeleteSuccessSchema]:
        """
        删除组

        """
        return await self.request(
            request=async_delete,
            api="/group/{item_id}",
            body={"params": dict(item_id=item_id)},
            resp_model=DeleteSuccessSchema,
        )

    def group_delete_sync(self, item_id: int) -> Tuple[int, DeleteSuccessSchema]:
        """
        删除组

        """
        return self.request_sync(
            request=requests.delete,
            api="/group/{item_id}",
            body={"params": dict(item_id=item_id)},
            resp_model=DeleteSuccessSchema,
        )

    async def group_all_get(self) -> Tuple[int, GetGroupAllOutSchema]:
        """
        获取所有组

        """
        return await self.request(
            request=async_get,
            api="/group/all",
            body={},
            resp_model=GetGroupAllOutSchema,
        )

    def group_all_get_sync(self) -> Tuple[int, GetGroupAllOutSchema]:
        """
        获取所有组

        """
        return self.request_sync(
            request=requests.get,
            api="/group/all",
            body={},
            resp_model=GetGroupAllOutSchema,
        )

    async def permission(
        self, body: CreatePermissionInSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        创建权限

        """
        return await self.request(
            request=async_post,
            api="/permission/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def permission_sync(
        self, body: CreatePermissionInSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        创建权限

        """
        return self.request_sync(
            request=requests.post,
            api="/permission/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def permission_put(
        self, body: UpdatePermissionInSchema, item_id: int
    ) -> Tuple[int, UpdatePermissionOutSchema]:
        """
        更新权限信息

        """
        return await self.request(
            request=async_put,
            api="/permission/{item_id}",
            body={"data": body.model_dump_json(), "params": dict(item_id=item_id)},
            resp_model=UpdatePermissionOutSchema,
        )

    def permission_put_sync(
        self, body: UpdatePermissionInSchema, item_id: int
    ) -> Tuple[int, UpdatePermissionOutSchema]:
        """
        更新权限信息

        """
        return self.request_sync(
            request=requests.put,
            api="/permission/{item_id}",
            body={"data": body.model_dump_json(), "params": dict(item_id=item_id)},
            resp_model=UpdatePermissionOutSchema,
        )

    async def permission_get(self, item_id: int) -> Tuple[int, GetPermissionOutSchema]:
        """
        获取权限信息

        """
        return await self.request(
            request=async_get,
            api="/permission/{item_id}",
            body={"params": dict(item_id=item_id)},
            resp_model=GetPermissionOutSchema,
        )

    def permission_get_sync(self, item_id: int) -> Tuple[int, GetPermissionOutSchema]:
        """
        获取权限信息

        """
        return self.request_sync(
            request=requests.get,
            api="/permission/{item_id}",
            body={"params": dict(item_id=item_id)},
            resp_model=GetPermissionOutSchema,
        )

    async def permission_delete(self, item_id: int) -> Tuple[int, DeleteSuccessSchema]:
        """
        删除权限

        """
        return await self.request(
            request=async_delete,
            api="/permission/{item_id}",
            body={"params": dict(item_id=item_id)},
            resp_model=DeleteSuccessSchema,
        )

    def permission_delete_sync(self, item_id: int) -> Tuple[int, DeleteSuccessSchema]:
        """
        删除权限

        """
        return self.request_sync(
            request=requests.delete,
            api="/permission/{item_id}",
            body={"params": dict(item_id=item_id)},
            resp_model=DeleteSuccessSchema,
        )

    async def permission_all_get(self) -> Tuple[int, GetPermissionAllOutSchema]:
        """
        获取全部权限

        """
        return await self.request(
            request=async_get,
            api="/permission/all",
            body={},
            resp_model=GetPermissionAllOutSchema,
        )

    def permission_all_get_sync(self) -> Tuple[int, GetPermissionAllOutSchema]:
        """
        获取全部权限

        """
        return self.request_sync(
            request=requests.get,
            api="/permission/all",
            body={},
            resp_model=GetPermissionAllOutSchema,
        )

    async def permission_list_get(
        self,
        name: Union[str, None],
        belong_type: Union[PermissionBelongType, None],
        per_page: Union[int, None] = "20",
        page: Union[int, None] = "1",
    ) -> Tuple[int, GetPermissionListOutSchema]:
        """
        分页检索

        """
        return await self.request(
            request=async_get,
            api="/permission/list",
            body={
                "params": dict(
                    name=name, belong_type=belong_type, per_page=per_page, page=page
                )
            },
            resp_model=GetPermissionListOutSchema,
        )

    def permission_list_get_sync(
        self,
        name: Union[str, None],
        belong_type: Union[PermissionBelongType, None],
        per_page: Union[int, None] = "20",
        page: Union[int, None] = "1",
    ) -> Tuple[int, GetPermissionListOutSchema]:
        """
        分页检索

        """
        return self.request_sync(
            request=requests.get,
            api="/permission/list",
            body={
                "params": dict(
                    name=name, belong_type=belong_type, per_page=per_page, page=page
                )
            },
            resp_model=GetPermissionListOutSchema,
        )

    async def download(self, file_name: str) -> Tuple[int, Dict]:
        """
        文件下载

        """
        return await self.request(
            request=async_get,
            api="/file_transport/download/{file_name}",
            body={"params": dict(file_name=file_name)},
            resp_model=None,
        )

    def download_sync(self, file_name: str) -> Tuple[int, Dict]:
        """
        文件下载

        """
        return self.request_sync(
            request=requests.get,
            api="/file_transport/download/{file_name}",
            body={"params": dict(file_name=file_name)},
            resp_model=None,
        )

    async def lockArea(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_get, api="/api/taskInfo/lockArea/", body={}, resp_model=None
        )

    def lockArea_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/lockArea/",
            body={},
            resp_model=None,
        )

    async def api_taskInfo_lockArea_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_post, api="/api/taskInfo/lockArea/", body={}, resp_model=None
        )

    def api_taskInfo_lockArea_post_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/lockArea/",
            body={},
            resp_model=None,
        )

    async def delete(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_get,
            api="/api/taskInfo/lockArea/delete/",
            body={},
            resp_model=None,
        )

    def delete_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/lockArea/delete/",
            body={},
            resp_model=None,
        )

    async def api_taskInfo_lockArea_delete_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/lockArea/delete/",
            body={},
            resp_model=None,
        )

    def api_taskInfo_lockArea_delete_post_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/lockArea/delete/",
            body={},
            resp_model=None,
        )

    async def deleteByTag(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_get,
            api="/api/taskInfo/lockArea/deleteByTag/",
            body={},
            resp_model=None,
        )

    def deleteByTag_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/lockArea/deleteByTag/",
            body={},
            resp_model=None,
        )

    async def api_taskInfo_lockArea_deleteByTag_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/lockArea/deleteByTag/",
            body={},
            resp_model=None,
        )

    def api_taskInfo_lockArea_deleteByTag_post_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/lockArea/deleteByTag/",
            body={},
            resp_model=None,
        )

    async def change(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_get,
            api="/api/taskInfo/lockArea/change/",
            body={},
            resp_model=None,
        )

    def change_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/lockArea/change/",
            body={},
            resp_model=None,
        )

    async def api_taskInfo_lockArea_change_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/lockArea/change/",
            body={},
            resp_model=None,
        )

    def api_taskInfo_lockArea_change_post_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/lockArea/change/",
            body={},
            resp_model=None,
        )

    async def resendJob(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_get,
            api="/api/taskInfo/vehicleJob/resendJob/",
            body={},
            resp_model=None,
        )

    def resendJob_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/vehicleJob/resendJob/",
            body={},
            resp_model=None,
        )

    async def api_taskInfo_vehicleJob_resendJob_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/vehicleJob/resendJob/",
            body={},
            resp_model=None,
        )

    def api_taskInfo_vehicleJob_resendJob_post_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/vehicleJob/resendJob/",
            body={},
            resp_model=None,
        )

    async def message_event_start_get(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_get, api="/message_event/start/", body={}, resp_model=None
        )

    def message_event_start_get_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.get, api="/message_event/start/", body={}, resp_model=None
        )

    async def message_event_start_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_post, api="/message_event/start/", body={}, resp_model=None
        )

    def message_event_start_post_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.post, api="/message_event/start/", body={}, resp_model=None
        )

    async def message_event_abort_get(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_get, api="/message_event/abort/", body={}, resp_model=None
        )

    def message_event_abort_get_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.get, api="/message_event/abort/", body={}, resp_model=None
        )

    async def message_event_abort_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_post, api="/message_event/abort/", body={}, resp_model=None
        )

    def message_event_abort_post_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.post, api="/message_event/abort/", body={}, resp_model=None
        )

    async def api_taskInfo_vehicleJob_delete_get(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_get,
            api="/api/taskInfo/vehicleJob/delete/",
            body={},
            resp_model=None,
        )

    def api_taskInfo_vehicleJob_delete_get_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/vehicleJob/delete/",
            body={},
            resp_model=None,
        )

    async def api_taskInfo_vehicleJob_delete_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/vehicleJob/delete/",
            body={},
            resp_model=None,
        )

    def api_taskInfo_vehicleJob_delete_post_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/vehicleJob/delete/",
            body={},
            resp_model=None,
        )

    async def runImmediate(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_get,
            api="/api/taskInfo/taskPool/runImmediate",
            body={},
            resp_model=None,
        )

    def runImmediate_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/taskPool/runImmediate",
            body={},
            resp_model=None,
        )

    async def api_taskInfo_taskPool_runImmediate_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/taskPool/runImmediate",
            body={},
            resp_model=None,
        )

    def api_taskInfo_taskPool_runImmediate_post_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/taskPool/runImmediate",
            body={},
            resp_model=None,
        )

    async def api_taskInfo_taskPool_abort_get(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_get,
            api="/api/taskInfo/taskPool/abort",
            body={},
            resp_model=None,
        )

    def api_taskInfo_taskPool_abort_get_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/taskPool/abort",
            body={},
            resp_model=None,
        )

    async def api_taskInfo_taskPool_abort_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/taskPool/abort",
            body={},
            resp_model=None,
        )

    def api_taskInfo_taskPool_abort_post_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/taskPool/abort",
            body={},
            resp_model=None,
        )

    async def trailerStatus(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_get,
            api="/api/deviceInfo/vehicleStatus/trailerStatus",
            body={},
            resp_model=None,
        )

    def trailerStatus_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.get,
            api="/api/deviceInfo/vehicleStatus/trailerStatus",
            body={},
            resp_model=None,
        )

    async def api_deviceInfo_vehicleStatus_trailerStatus_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_post,
            api="/api/deviceInfo/vehicleStatus/trailerStatus",
            body={},
            resp_model=None,
        )

    def api_deviceInfo_vehicleStatus_trailerStatus_post_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.post,
            api="/api/deviceInfo/vehicleStatus/trailerStatus",
            body={},
            resp_model=None,
        )

    async def mode(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_get,
            api="/api/deviceInfo/vehicleStatus/mode",
            body={},
            resp_model=None,
        )

    def mode_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.get,
            api="/api/deviceInfo/vehicleStatus/mode",
            body={},
            resp_model=None,
        )

    async def api_deviceInfo_vehicleStatus_mode_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_post,
            api="/api/deviceInfo/vehicleStatus/mode",
            body={},
            resp_model=None,
        )

    def api_deviceInfo_vehicleStatus_mode_post_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.post,
            api="/api/deviceInfo/vehicleStatus/mode",
            body={},
            resp_model=None,
        )

    async def containerInfo(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_get,
            api="/api/taskInfo/containerInfo/",
            body={},
            resp_model=None,
        )

    def containerInfo_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/containerInfo/",
            body={},
            resp_model=None,
        )

    async def api_taskInfo_containerInfo_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/containerInfo/",
            body={},
            resp_model=None,
        )

    def api_taskInfo_containerInfo_post_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/containerInfo/",
            body={},
            resp_model=None,
        )

    async def message_event_rch_get(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_get, api="/message_event/rch", body={}, resp_model=None
        )

    def message_event_rch_get_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.get, api="/message_event/rch", body={}, resp_model=None
        )

    async def message_event_rch_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_post, api="/message_event/rch", body={}, resp_model=None
        )

    def message_event_rch_post_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.post, api="/message_event/rch", body={}, resp_model=None
        )

    async def query(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_get,
            api="/fms/area/inventory/query/",
            body={},
            resp_model=None,
        )

    def query_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.get,
            api="/fms/area/inventory/query/",
            body={},
            resp_model=None,
        )

    async def fms_area_inventory_query_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_post,
            api="/fms/area/inventory/query/",
            body={},
            resp_model=None,
        )

    def fms_area_inventory_query_post_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.post,
            api="/fms/area/inventory/query/",
            body={},
            resp_model=None,
        )

    async def api_vehicleManager_power_get(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_get,
            api="/api/vehicleManager/power/",
            body={},
            resp_model=None,
        )

    def api_vehicleManager_power_get_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.get,
            api="/api/vehicleManager/power/",
            body={},
            resp_model=None,
        )

    async def api_vehicleManager_power_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/power/",
            body={},
            resp_model=None,
        )

    def api_vehicleManager_power_post_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/power/",
            body={},
            resp_model=None,
        )

    async def api_vehicleManager_handshake_get(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_get,
            api="/api/vehicleManager/handshake/",
            body={},
            resp_model=None,
        )

    def api_vehicleManager_handshake_get_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.get,
            api="/api/vehicleManager/handshake/",
            body={},
            resp_model=None,
        )

    async def api_vehicleManager_handshake_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/handshake/",
            body={},
            resp_model=None,
        )

    def api_vehicleManager_handshake_post_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/handshake/",
            body={},
            resp_model=None,
        )

    async def SetOperation(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_get,
            api="/api/deviceInfo/vehicleStatus/SetOperation",
            body={},
            resp_model=None,
        )

    def SetOperation_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.get,
            api="/api/deviceInfo/vehicleStatus/SetOperation",
            body={},
            resp_model=None,
        )

    async def api_deviceInfo_vehicleStatus_SetOperation_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_post,
            api="/api/deviceInfo/vehicleStatus/SetOperation",
            body={},
            resp_model=None,
        )

    def api_deviceInfo_vehicleStatus_SetOperation_post_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.post,
            api="/api/deviceInfo/vehicleStatus/SetOperation",
            body={},
            resp_model=None,
        )

    async def api_vehicleManager_report_speed_ratio_get(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_get,
            api="/api/vehicleManager/report_speed_ratio/",
            body={},
            resp_model=None,
        )

    def api_vehicleManager_report_speed_ratio_get_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.get,
            api="/api/vehicleManager/report_speed_ratio/",
            body={},
            resp_model=None,
        )

    async def api_vehicleManager_report_speed_ratio_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/report_speed_ratio/",
            body={},
            resp_model=None,
        )

    def api_vehicleManager_report_speed_ratio_post_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/report_speed_ratio/",
            body={},
            resp_model=None,
        )

    async def api_container_InventoryUpdate_get(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_get,
            api="/api/container/InventoryUpdate",
            body={},
            resp_model=None,
        )

    def api_container_InventoryUpdate_get_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.get,
            api="/api/container/InventoryUpdate",
            body={},
            resp_model=None,
        )

    async def api_container_InventoryUpdate_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_post,
            api="/api/container/InventoryUpdate",
            body={},
            resp_model=None,
        )

    def api_container_InventoryUpdate_post_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.post,
            api="/api/container/InventoryUpdate",
            body={},
            resp_model=None,
        )

    async def SetVesselInfoStatus(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_get,
            api="/api/taskInfo/VesselInfo/SetVesselInfoStatus",
            body={},
            resp_model=None,
        )

    def SetVesselInfoStatus_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/VesselInfo/SetVesselInfoStatus",
            body={},
            resp_model=None,
        )

    async def api_taskInfo_VesselInfo_SetVesselInfoStatus_post(
        self,
    ) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/VesselInfo/SetVesselInfoStatus",
            body={},
            resp_model=None,
        )

    def api_taskInfo_VesselInfo_SetVesselInfoStatus_post_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/VesselInfo/SetVesselInfoStatus",
            body={},
            resp_model=None,
        )

    async def query_all(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_get,
            api="/api/taskInfo/vehicleJob/query_all/",
            body={},
            resp_model=None,
        )

    def query_all_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/vehicleJob/query_all/",
            body={},
            resp_model=None,
        )

    async def api_taskInfo_vehicleJob_query_all_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/vehicleJob/query_all/",
            body={},
            resp_model=None,
        )

    def api_taskInfo_vehicleJob_query_all_post_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/vehicleJob/query_all/",
            body={},
            resp_model=None,
        )

    async def PaceGlobal(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_get, api="/api/taskInfo/PaceGlobal/", body={}, resp_model=None
        )

    def PaceGlobal_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/PaceGlobal/",
            body={},
            resp_model=None,
        )

    async def api_taskInfo_PaceGlobal_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/PaceGlobal/",
            body={},
            resp_model=None,
        )

    def api_taskInfo_PaceGlobal_post_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/PaceGlobal/",
            body={},
            resp_model=None,
        )

    async def SetLane(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_get,
            api="/api/taskInfo/quayCrane/SetLane/",
            body={},
            resp_model=None,
        )

    def SetLane_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/quayCrane/SetLane/",
            body={},
            resp_model=None,
        )

    async def api_taskInfo_quayCrane_SetLane_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/quayCrane/SetLane/",
            body={},
            resp_model=None,
        )

    def api_taskInfo_quayCrane_SetLane_post_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/quayCrane/SetLane/",
            body={},
            resp_model=None,
        )

    async def message_event_update_qc_task_get(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_get,
            api="/message_event/update_qc_task/",
            body={},
            resp_model=None,
        )

    def message_event_update_qc_task_get_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.get,
            api="/message_event/update_qc_task/",
            body={},
            resp_model=None,
        )

    async def message_event_update_qc_task_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_post,
            api="/message_event/update_qc_task/",
            body={},
            resp_model=None,
        )

    def message_event_update_qc_task_post_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.post,
            api="/message_event/update_qc_task/",
            body={},
            resp_model=None,
        )

    async def vehicleJob(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_get, api="/api/taskInfo/vehicleJob/", body={}, resp_model=None
        )

    def vehicleJob_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/vehicleJob/",
            body={},
            resp_model=None,
        )

    async def api_taskInfo_vehicleJob_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/vehicleJob/",
            body={},
            resp_model=None,
        )

    def api_taskInfo_vehicleJob_post_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/vehicleJob/",
            body={},
            resp_model=None,
        )

    async def all_current_job(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_get,
            api="/api/taskInfo/vehicleJob/all_current_job/",
            body={},
            resp_model=None,
        )

    def all_current_job_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/vehicleJob/all_current_job/",
            body={},
            resp_model=None,
        )

    async def api_taskInfo_vehicleJob_all_current_job_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/vehicleJob/all_current_job/",
            body={},
            resp_model=None,
        )

    def api_taskInfo_vehicleJob_all_current_job_post_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/vehicleJob/all_current_job/",
            body={},
            resp_model=None,
        )

    async def api_container_EditContainers_get(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_get,
            api="/api/container/EditContainers",
            body={},
            resp_model=None,
        )

    def api_container_EditContainers_get_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.get,
            api="/api/container/EditContainers",
            body={},
            resp_model=None,
        )

    async def api_container_EditContainers_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_post,
            api="/api/container/EditContainers",
            body={},
            resp_model=None,
        )

    def api_container_EditContainers_post_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.post,
            api="/api/container/EditContainers",
            body={},
            resp_model=None,
        )

    async def api_vehicleManager_stop_get(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_get, api="/api/vehicleManager/stop/", body={}, resp_model=None
        )

    def api_vehicleManager_stop_get_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.get,
            api="/api/vehicleManager/stop/",
            body={},
            resp_model=None,
        )

    async def api_vehicleManager_stop_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/stop/",
            body={},
            resp_model=None,
        )

    def api_vehicleManager_stop_post_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/stop/",
            body={},
            resp_model=None,
        )

    async def engine(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_get, api="/api/engine", body={}, resp_model=None
        )

    def engine_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.get, api="/api/engine", body={}, resp_model=None
        )

    async def api_engine_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_post, api="/api/engine", body={}, resp_model=None
        )

    def api_engine_post_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.post, api="/api/engine", body={}, resp_model=None
        )

    async def response_mixed_area(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_get, api="/api/response_mixed_area", body={}, resp_model=None
        )

    def response_mixed_area_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.get,
            api="/api/response_mixed_area",
            body={},
            resp_model=None,
        )

    async def api_response_mixed_area_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_post, api="/api/response_mixed_area", body={}, resp_model=None
        )

    def api_response_mixed_area_post_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.post,
            api="/api/response_mixed_area",
            body={},
            resp_model=None,
        )

    async def points(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_get,
            api="/api/vehicleManager/points",
            body={},
            resp_model=None,
        )

    def points_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.get,
            api="/api/vehicleManager/points",
            body={},
            resp_model=None,
        )

    async def api_vehicleManager_points_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_post,
            api="/api/vehicleManager/points",
            body={},
            resp_model=None,
        )

    def api_vehicleManager_points_post_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.post,
            api="/api/vehicleManager/points",
            body={},
            resp_model=None,
        )

    async def GetAll(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_get,
            api="/api/taskInfo/EquipmentStatus/GetAll",
            body={},
            resp_model=None,
        )

    def GetAll_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/EquipmentStatus/GetAll",
            body={},
            resp_model=None,
        )

    async def api_taskInfo_EquipmentStatus_GetAll_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/EquipmentStatus/GetAll",
            body={},
            resp_model=None,
        )

    def api_taskInfo_EquipmentStatus_GetAll_post_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/EquipmentStatus/GetAll",
            body={},
            resp_model=None,
        )

    async def rc_task(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_get, api="/api/task/rc_task", body={}, resp_model=None
        )

    def rc_task_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.get, api="/api/task/rc_task", body={}, resp_model=None
        )

    async def api_task_rc_task_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_post, api="/api/task/rc_task", body={}, resp_model=None
        )

    def api_task_rc_task_post_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.post, api="/api/task/rc_task", body={}, resp_model=None
        )

    async def api_telep_get(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_get, api="/api/telep", body={}, resp_model=None
        )

    def api_telep_get_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.get, api="/api/telep", body={}, resp_model=None
        )

    async def api_telep_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return await self.request(
            request=async_post, api="/api/telep", body={}, resp_model=None
        )

    def api_telep_post_sync(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        return self.request_sync(
            request=requests.post, api="/api/telep", body={}, resp_model=None
        )

    async def SetVesselInfo(self, body: SetVesselSchemas) -> Tuple[int, Dict]:
        """
                创建船舶
                船头大于船尾左
        船尾大于船头右
        """
        return await self.request(
            request=async_post,
            api="/VesselInfo/SetVesselInfo",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def SetVesselInfo_sync(self, body: SetVesselSchemas) -> Tuple[int, Dict]:
        """
                创建船舶
                船头大于船尾左
        船尾大于船头右
        """
        return self.request_sync(
            request=requests.post,
            api="/VesselInfo/SetVesselInfo",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def ReleaseVesselInfo(self, body: DelVesselSchemas) -> Tuple[int, Dict]:
        """
        删除船

        """
        return await self.request(
            request=async_post,
            api="/VesselInfo/ReleaseVesselInfo",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def ReleaseVesselInfo_sync(self, body: DelVesselSchemas) -> Tuple[int, Dict]:
        """
        删除船

        """
        return self.request_sync(
            request=requests.post,
            api="/VesselInfo/ReleaseVesselInfo",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def GetBertNO(
        self, response_data_type: ReceiveDataType = "list"
    ) -> Tuple[int, Dict]:
        """
        获取泊位号

        """
        return await self.request(
            request=async_get,
            api="/VesselInfo/GetBertNO",
            body={"params": dict(response_data_type=response_data_type)},
            resp_model=None,
        )

    def GetBertNO_sync(
        self, response_data_type: ReceiveDataType = "list"
    ) -> Tuple[int, Dict]:
        """
        获取泊位号

        """
        return self.request_sync(
            request=requests.get,
            api="/VesselInfo/GetBertNO",
            body={"params": dict(response_data_type=response_data_type)},
            resp_model=None,
        )

    async def EditVesselInfo(self, body: object) -> Tuple[int, CreateSuccessSchema]:
        """
                修改船
                {
            "ETA": "1701453720",
            "ETB": "1701543840",
            "vesselVisitId": "111",
            "vesselName": "测试船舶方向12",
            "inVyg": "impor12",
            "phase": "DEPARTED",
            "bollardFore": 1070,
            "bollardAfter": 1010,
            "ETD": "1701934680"
        }
        """
        return await self.request(
            request=async_post,
            api="/VesselInfo/EditVesselInfo",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def EditVesselInfo_sync(self, body: object) -> Tuple[int, CreateSuccessSchema]:
        """
                修改船
                {
            "ETA": "1701453720",
            "ETB": "1701543840",
            "vesselVisitId": "111",
            "vesselName": "测试船舶方向12",
            "inVyg": "impor12",
            "phase": "DEPARTED",
            "bollardFore": 1070,
            "bollardAfter": 1010,
            "ETD": "1701934680"
        }
        """
        return self.request_sync(
            request=requests.post,
            api="/VesselInfo/EditVesselInfo",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def ghostVehicleCancel(
        self, body: SetGhostVehicleCancelPost
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Gui-取消幽灵车

        """
        return await self.request(
            request=async_post,
            api="/api/deviceInfo/vehicleStatus/ghostVehicleCancel",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def ghostVehicleCancel_sync(
        self, body: SetGhostVehicleCancelPost
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Gui-取消幽灵车

        """
        return self.request_sync(
            request=requests.post,
            api="/api/deviceInfo/vehicleStatus/ghostVehicleCancel",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def EquipmentStatus(self, body: SetSwitchRequest) -> Tuple[int, Dict]:
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
        return await self.request(
            request=async_post,
            api="/api/taskInfo/EquipmentStatus/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def EquipmentStatus_sync(self, body: SetSwitchRequest) -> Tuple[int, Dict]:
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
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/EquipmentStatus/",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def SpreaderSize(self, body: SetSwitchRequest) -> Tuple[int, Dict]:
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
        return await self.request(
            request=async_post,
            api="/api/taskInfo/EquipmentStatus/SpreaderSize/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def SpreaderSize_sync(self, body: SetSwitchRequest) -> Tuple[int, Dict]:
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
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/EquipmentStatus/SpreaderSize/",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def GetAllMessage(self, body: GetAllMessageSchemas) -> Tuple[int, Dict]:
        """
            获取所有告警信息
            request params:
        {
        "start_time": "2023-09-01 00:00:00",
        "end_time": "2023-12-07 00:00:00",
        "messageType": "truck",
        "truck_list": ["AT01"],
        "per_page": 10,
        "page": 1
        }
        """
        return await self.request(
            request=async_post,
            api="/message/GetAllMessage",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def GetAllMessage_sync(self, body: GetAllMessageSchemas) -> Tuple[int, Dict]:
        """
            获取所有告警信息
            request params:
        {
        "start_time": "2023-09-01 00:00:00",
        "end_time": "2023-12-07 00:00:00",
        "messageType": "truck",
        "truck_list": ["AT01"],
        "per_page": 10,
        "page": 1
        }
        """
        return self.request_sync(
            request=requests.post,
            api="/message/GetAllMessage",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def GetFileMessage(self, body: GetAllMessageCSVSchemas) -> Tuple[int, Dict]:
        """
        获取历史故障信息文件
        导出告警信息csv
        """
        return await self.request(
            request=async_post,
            api="/message/GetFileMessage",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def GetFileMessage_sync(self, body: GetAllMessageCSVSchemas) -> Tuple[int, Dict]:
        """
        获取历史故障信息文件
        导出告警信息csv
        """
        return self.request_sync(
            request=requests.post,
            api="/message/GetFileMessage",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def UpdatePileInfo(
        self, body: UpdatePileInfoSchemas
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        单个充电桩操作

        """
        return await self.request(
            request=async_post,
            api="/pileinfo/UpdatePileInfo",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def UpdatePileInfo_sync(
        self, body: UpdatePileInfoSchemas
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        单个充电桩操作

        """
        return self.request_sync(
            request=requests.post,
            api="/pileinfo/UpdatePileInfo",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def UpdateAllPileInfo(
        self, body: UpdateALlInfoSchemas
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        所有充电桩操作

        """
        return await self.request(
            request=async_post,
            api="/pileinfo/UpdateAllPileInfo",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def UpdateAllPileInfo_sync(
        self, body: UpdateALlInfoSchemas
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        所有充电桩操作

        """
        return self.request_sync(
            request=requests.post,
            api="/pileinfo/UpdateAllPileInfo",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def ContainerInfoSetup(
        self, body: ContainerSteupSchemas
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        箱子增删改

        """
        return await self.request(
            request=async_post,
            api="/denmarkinfo/ContainerInfoSetup",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def ContainerInfoSetup_sync(
        self, body: ContainerSteupSchemas
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        箱子增删改

        """
        return self.request_sync(
            request=requests.post,
            api="/denmarkinfo/ContainerInfoSetup",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def PlcStatus(self, body: object) -> Tuple[int, CreateSuccessSchema]:
        """
        控制车辆应请

        """
        return await self.request(
            request=async_post,
            api="/denmarkinfo/PlcStatus",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def PlcStatus_sync(self, body: object) -> Tuple[int, CreateSuccessSchema]:
        """
        控制车辆应请

        """
        return self.request_sync(
            request=requests.post,
            api="/denmarkinfo/PlcStatus",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def ServerVersion(self) -> Tuple[int, Dict]:
        """
        所有服务版本号

        """
        return await self.request(
            request=async_get,
            api="/denmarkinfo/ServerVersion",
            body={},
            resp_model=None,
        )

    def ServerVersion_sync(self) -> Tuple[int, Dict]:
        """
        所有服务版本号

        """
        return self.request_sync(
            request=requests.get,
            api="/denmarkinfo/ServerVersion",
            body={},
            resp_model=None,
        )

    async def ForceOverTake(
        self, body: ForceOvertakeSchemas
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Over Take功能

        """
        return await self.request(
            request=async_post,
            api="/TaskCorrelation/ForceOverTake/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def ForceOverTake_sync(
        self, body: ForceOvertakeSchemas
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Over Take功能

        """
        return self.request_sync(
            request=requests.post,
            api="/TaskCorrelation/ForceOverTake/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def update_task(
        self, body: UpdateTaskSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Update Task

        """
        return await self.request(
            request=async_post,
            api="/TaskCorrelation/update_task",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def update_task_sync(
        self, body: UpdateTaskSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Update Task

        """
        return self.request_sync(
            request=requests.post,
            api="/TaskCorrelation/update_task",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def load_first(
        self, body: LoadFirstInSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Load First

        """
        return await self.request(
            request=async_post,
            api="/TaskCorrelation/load_first",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def load_first_sync(
        self, body: LoadFirstInSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Load First

        """
        return self.request_sync(
            request=requests.post,
            api="/TaskCorrelation/load_first",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def redo_task(
        self, body: RedoTaskInSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Redo Task

        """
        return await self.request(
            request=async_post,
            api="/TaskCorrelation/redo_task",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def redo_task_sync(self, body: RedoTaskInSchema) -> Tuple[int, CreateSuccessSchema]:
        """
        Redo Task

        """
        return self.request_sync(
            request=requests.post,
            api="/TaskCorrelation/redo_task",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def CollectionFailTask(
        self, body: FailTaskSchemas
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        收集失败任务信息功能

        """
        return await self.request(
            request=async_post,
            api="/TaskCorrelation/CollectionFailTask/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def CollectionFailTask_sync(
        self, body: FailTaskSchemas
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        收集失败任务信息功能

        """
        return self.request_sync(
            request=requests.post,
            api="/TaskCorrelation/CollectionFailTask/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def event_report(self, body: EventReport) -> Tuple[int, CreateSuccessSchema]:
        """
            手动补事件上报信号
            task executor 返回的响应体共两种：
        第一种：
            {"data": null, "code": 200, "msg": "success", "error": ""}
        第二种：
            {"detail": {
                "code": 15700,
                "msg": "event_listener_malaysia 执行失败, ",
                "error": "RequestExternalError"}
            }
        """
        return await self.request(
            request=async_post,
            api="/TaskCorrelation/event_report",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def event_report_sync(self, body: EventReport) -> Tuple[int, CreateSuccessSchema]:
        """
            手动补事件上报信号
            task executor 返回的响应体共两种：
        第一种：
            {"data": null, "code": 200, "msg": "success", "error": ""}
        第二种：
            {"detail": {
                "code": 15700,
                "msg": "event_listener_malaysia 执行失败, ",
                "error": "RequestExternalError"}
            }
        """
        return self.request_sync(
            request=requests.post,
            api="/TaskCorrelation/event_report",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def TosLoginStatus(self, body: object) -> Tuple[int, CreateSuccessSchema]:
        """
        Tos登录登出

        """
        return await self.request(
            request=async_post,
            api="/TosLoginStatus/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def TosLoginStatus_sync(self, body: object) -> Tuple[int, CreateSuccessSchema]:
        """
        Tos登录登出

        """
        return self.request_sync(
            request=requests.post,
            api="/TosLoginStatus/",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def twistlock_station(
        self, body: CRUDTwistlockStation, operation_type: ReceiveOperationType
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        增删改锁站Ts信息
        CREATE / UPDATE  /  DELETE
        """
        return await self.request(
            request=async_post,
            api="/twistlock_station/",
            body={
                "data": body.model_dump_json(),
                "params": dict(operation_type=operation_type),
            },
            resp_model=CreateSuccessSchema,
        )

    def twistlock_station_sync(
        self, body: CRUDTwistlockStation, operation_type: ReceiveOperationType
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        增删改锁站Ts信息
        CREATE / UPDATE  /  DELETE
        """
        return self.request_sync(
            request=requests.post,
            api="/twistlock_station/",
            body={
                "data": body.model_dump_json(),
                "params": dict(operation_type=operation_type),
            },
            resp_model=CreateSuccessSchema,
        )

    async def GetPtions(self) -> Tuple[int, Dict]:
        """
        获取堆场贝位以及岸桥车道

        """
        return await self.request(
            request=async_post, api="/get_ptions/GetPtions", body={}, resp_model=None
        )

    def GetPtions_sync(self) -> Tuple[int, Dict]:
        """
        获取堆场贝位以及岸桥车道

        """
        return self.request_sync(
            request=requests.post, api="/get_ptions/GetPtions", body={}, resp_model=None
        )


GuiServerRequest = GuiServerRequestCls()
