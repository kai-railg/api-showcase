# -*- coding: utf-8 -*-

from typing import Union, Tuple, Dict
from urllib import parse

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

    async def authentication(
        self, body: LoginInSchema
    ) -> Tuple[int, UserWithTokenOutResponseInfoSchema]:
        """
        登录

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/authentication/"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /authentication/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, UserWithTokenOutResponseInfoSchema.model_validate_json(resp)

    async def auth(self) -> Tuple[int, GetSelfOutSchema]:
        """
        获取个人信息

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/auth/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /auth/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, GetSelfOutSchema.model_validate_json(resp)

    async def update_passwd(
        self, body: UpdatePasswdInSchema, item_id: int
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        修改用户密码

        """
        resp = await async_put(
            url=parse.urljoin(self.url, "/auth/update_passwd/{item_id}"),
            json=body.dict(),
            params=dict(item_id=item_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /auth/update_passwd/{item_id}, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    async def user(self, body: CreateUserInSchema) -> Tuple[int, CreateSuccessSchema]:
        """
        创建用户

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/user/"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /user/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    async def user_put(
        self, body: UpdateUserInSchema, item_id: int
    ) -> Tuple[int, UpdateUserOutSchema]:
        """
        更新用户信息

        """
        resp = await async_put(
            url=parse.urljoin(self.url, "/user/{item_id}"),
            json=body.dict(),
            params=dict(item_id=item_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /user/{item_id}, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, UpdateUserOutSchema.model_validate_json(resp)

    async def user_get(self, item_id: int) -> Tuple[int, GetUserOutSchema]:
        """
        获取单个用户信息

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/user/{item_id}"), params=dict(item_id=item_id)
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /user/{item_id}, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, GetUserOutSchema.model_validate_json(resp)

    async def user_delete(self, item_id: int) -> Tuple[int, DeleteSuccessSchema]:
        """
        删除用户

        """
        resp = await async_delete(
            url=parse.urljoin(self.url, "/user/{item_id}"), params=dict(item_id=item_id)
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /user/{item_id}, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, DeleteSuccessSchema.model_validate_json(resp)

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
        resp = await async_get(
            url=parse.urljoin(self.url, "/user/list"),
            params=dict(
                department=department, group_id=group_id, per_page=per_page, page=page
            ),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /user/list, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, GetUserListOutSchema.model_validate_json(resp)

    async def all(self) -> Tuple[int, GetUserAllOutSchema]:
        """
        获取全部用户

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/user/all"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /user/all, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, GetUserAllOutSchema.model_validate_json(resp)

    async def group(self, body: CreateGroupInSchema) -> Tuple[int, CreateSuccessSchema]:
        """
        创建组

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/group/"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /group/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    async def group_put(
        self, body: UpdateGroupInSchema, item_id: int
    ) -> Tuple[int, UpdateGroupOutSchema]:
        """
        更新组

        """
        resp = await async_put(
            url=parse.urljoin(self.url, "/group/{item_id}"),
            json=body.dict(),
            params=dict(item_id=item_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /group/{item_id}, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, UpdateGroupOutSchema.model_validate_json(resp)

    async def group_get(self, item_id: int) -> Tuple[int, GetGroupOutSchema]:
        """
        获取单个组

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/group/{item_id}"),
            params=dict(item_id=item_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /group/{item_id}, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, GetGroupOutSchema.model_validate_json(resp)

    async def group_delete(self, item_id: int) -> Tuple[int, DeleteSuccessSchema]:
        """
        删除组

        """
        resp = await async_delete(
            url=parse.urljoin(self.url, "/group/{item_id}"),
            params=dict(item_id=item_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /group/{item_id}, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, DeleteSuccessSchema.model_validate_json(resp)

    async def group_all_get(self) -> Tuple[int, GetGroupAllOutSchema]:
        """
        获取所有组

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/group/all"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /group/all, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, GetGroupAllOutSchema.model_validate_json(resp)

    async def permission(
        self, body: CreatePermissionInSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        创建权限

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/permission/"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /permission/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    async def permission_put(
        self, body: UpdatePermissionInSchema, item_id: int
    ) -> Tuple[int, UpdatePermissionOutSchema]:
        """
        更新权限信息

        """
        resp = await async_put(
            url=parse.urljoin(self.url, "/permission/{item_id}"),
            json=body.dict(),
            params=dict(item_id=item_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /permission/{item_id}, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, UpdatePermissionOutSchema.model_validate_json(resp)

    async def permission_get(self, item_id: int) -> Tuple[int, GetPermissionOutSchema]:
        """
        获取权限信息

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/permission/{item_id}"),
            params=dict(item_id=item_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /permission/{item_id}, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, GetPermissionOutSchema.model_validate_json(resp)

    async def permission_delete(self, item_id: int) -> Tuple[int, DeleteSuccessSchema]:
        """
        删除权限

        """
        resp = await async_delete(
            url=parse.urljoin(self.url, "/permission/{item_id}"),
            params=dict(item_id=item_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /permission/{item_id}, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, DeleteSuccessSchema.model_validate_json(resp)

    async def permission_all_get(self) -> Tuple[int, GetPermissionAllOutSchema]:
        """
        获取全部权限

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/permission/all"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /permission/all, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, GetPermissionAllOutSchema.model_validate_json(resp)

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
        resp = await async_get(
            url=parse.urljoin(self.url, "/permission/list"),
            params=dict(
                name=name, belong_type=belong_type, per_page=per_page, page=page
            ),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /permission/list, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, GetPermissionListOutSchema.model_validate_json(resp)

    async def download(self, file_name: str) -> Tuple[int, Dict]:
        """
        文件下载

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/file_transport/download/{file_name}"),
            params=dict(file_name=file_name),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /file_transport/download/{file_name}, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def lockArea(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/taskInfo/lockArea/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/taskInfo/lockArea/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def api_taskInfo_lockArea_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/taskInfo/lockArea/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/taskInfo/lockArea/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def delete(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/taskInfo/lockArea/delete/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/taskInfo/lockArea/delete/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def api_taskInfo_lockArea_delete_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/taskInfo/lockArea/delete/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/taskInfo/lockArea/delete/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def deleteByTag(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/taskInfo/lockArea/deleteByTag/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/taskInfo/lockArea/deleteByTag/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def api_taskInfo_lockArea_deleteByTag_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/taskInfo/lockArea/deleteByTag/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/taskInfo/lockArea/deleteByTag/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def change(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/taskInfo/lockArea/change/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/taskInfo/lockArea/change/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def api_taskInfo_lockArea_change_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/taskInfo/lockArea/change/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/taskInfo/lockArea/change/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def resendJob(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/taskInfo/vehicleJob/resendJob/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/taskInfo/vehicleJob/resendJob/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def api_taskInfo_vehicleJob_resendJob_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/taskInfo/vehicleJob/resendJob/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/taskInfo/vehicleJob/resendJob/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def message_event_start_get(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/message_event/start/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /message_event/start/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def message_event_start_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/message_event/start/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /message_event/start/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def message_event_abort_get(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/message_event/abort/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /message_event/abort/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def message_event_abort_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/message_event/abort/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /message_event/abort/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def api_taskInfo_vehicleJob_delete_get(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/taskInfo/vehicleJob/delete/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/taskInfo/vehicleJob/delete/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def api_taskInfo_vehicleJob_delete_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/taskInfo/vehicleJob/delete/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/taskInfo/vehicleJob/delete/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def runImmediate(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/taskInfo/taskPool/runImmediate"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/taskInfo/taskPool/runImmediate, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def api_taskInfo_taskPool_runImmediate_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/taskInfo/taskPool/runImmediate"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/taskInfo/taskPool/runImmediate, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def api_taskInfo_taskPool_abort_get(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/taskInfo/taskPool/abort"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/taskInfo/taskPool/abort, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def api_taskInfo_taskPool_abort_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/taskInfo/taskPool/abort"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/taskInfo/taskPool/abort, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def trailerStatus(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/trailerStatus"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/trailerStatus, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def api_deviceInfo_vehicleStatus_trailerStatus_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/trailerStatus"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/trailerStatus, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def mode(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/mode"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/mode, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def api_deviceInfo_vehicleStatus_mode_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/mode"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/mode, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def containerInfo(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/taskInfo/containerInfo/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/taskInfo/containerInfo/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def api_taskInfo_containerInfo_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/taskInfo/containerInfo/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/taskInfo/containerInfo/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def message_event_rch_get(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/message_event/rch"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /message_event/rch, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def message_event_rch_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/message_event/rch"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /message_event/rch, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def query(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/fms/area/inventory/query/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /fms/area/inventory/query/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def fms_area_inventory_query_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/fms/area/inventory/query/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /fms/area/inventory/query/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def api_vehicleManager_power_get(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/vehicleManager/power/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/power/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def api_vehicleManager_power_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/vehicleManager/power/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/power/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def api_vehicleManager_handshake_get(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/vehicleManager/handshake/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/handshake/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def api_vehicleManager_handshake_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/vehicleManager/handshake/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/handshake/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def SetOperation(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/SetOperation"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/SetOperation, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def api_deviceInfo_vehicleStatus_SetOperation_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/deviceInfo/vehicleStatus/SetOperation"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/SetOperation, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def api_vehicleManager_report_speed_ratio_get(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/vehicleManager/report_speed_ratio/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/report_speed_ratio/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def api_vehicleManager_report_speed_ratio_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/vehicleManager/report_speed_ratio/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/report_speed_ratio/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def api_container_InventoryUpdate_get(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/container/InventoryUpdate"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/container/InventoryUpdate, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def api_container_InventoryUpdate_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/container/InventoryUpdate"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/container/InventoryUpdate, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def SetVesselInfoStatus(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/taskInfo/VesselInfo/SetVesselInfoStatus"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/taskInfo/VesselInfo/SetVesselInfoStatus, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def api_taskInfo_VesselInfo_SetVesselInfoStatus_post(
        self,
    ) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/taskInfo/VesselInfo/SetVesselInfoStatus"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/taskInfo/VesselInfo/SetVesselInfoStatus, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def query_all(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/taskInfo/vehicleJob/query_all/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/taskInfo/vehicleJob/query_all/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def api_taskInfo_vehicleJob_query_all_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/taskInfo/vehicleJob/query_all/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/taskInfo/vehicleJob/query_all/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def PaceGlobal(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/taskInfo/PaceGlobal/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/taskInfo/PaceGlobal/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def api_taskInfo_PaceGlobal_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/taskInfo/PaceGlobal/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/taskInfo/PaceGlobal/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def SetLane(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/taskInfo/quayCrane/SetLane/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/taskInfo/quayCrane/SetLane/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def api_taskInfo_quayCrane_SetLane_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/taskInfo/quayCrane/SetLane/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/taskInfo/quayCrane/SetLane/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def message_event_update_qc_task_get(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/message_event/update_qc_task/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /message_event/update_qc_task/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def message_event_update_qc_task_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/message_event/update_qc_task/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /message_event/update_qc_task/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def vehicleJob(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/taskInfo/vehicleJob/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/taskInfo/vehicleJob/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def api_taskInfo_vehicleJob_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/taskInfo/vehicleJob/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/taskInfo/vehicleJob/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def all_current_job(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/taskInfo/vehicleJob/all_current_job/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/taskInfo/vehicleJob/all_current_job/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def api_taskInfo_vehicleJob_all_current_job_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/taskInfo/vehicleJob/all_current_job/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/taskInfo/vehicleJob/all_current_job/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def api_container_EditContainers_get(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/container/EditContainers"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/container/EditContainers, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def api_container_EditContainers_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/container/EditContainers"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/container/EditContainers, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def api_vehicleManager_stop_get(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/vehicleManager/stop/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/stop/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def api_vehicleManager_stop_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/vehicleManager/stop/"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/stop/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def engine(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/engine"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/engine, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def api_engine_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/engine"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/engine, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def response_mixed_area(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/response_mixed_area"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/response_mixed_area, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def api_response_mixed_area_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/response_mixed_area"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/response_mixed_area, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def points(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/vehicleManager/points"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/points, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def api_vehicleManager_points_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/vehicleManager/points"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/vehicleManager/points, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def GetAll(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/taskInfo/EquipmentStatus/GetAll"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/taskInfo/EquipmentStatus/GetAll, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def api_taskInfo_EquipmentStatus_GetAll_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/taskInfo/EquipmentStatus/GetAll"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/taskInfo/EquipmentStatus/GetAll, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def rc_task(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/task/rc_task"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/task/rc_task, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def api_task_rc_task_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/task/rc_task"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/task/rc_task, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def telep(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/api/telep"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/telep, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def api_telep_post(self) -> Tuple[int, Dict]:
        """
        Api Proxy

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/telep"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/telep, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def SetVesselInfo(self, body: SetVesselSchemas) -> Tuple[int, Dict]:
        """
                创建船舶
                船头大于船尾左
        船尾大于船头右
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/VesselInfo/SetVesselInfo"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /VesselInfo/SetVesselInfo, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def ReleaseVesselInfo(self, body: DelVesselSchemas) -> Tuple[int, Dict]:
        """
        删除船

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/VesselInfo/ReleaseVesselInfo"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /VesselInfo/ReleaseVesselInfo, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def GetBertNO(
        self, response_data_type: ReceiveDataType = "list"
    ) -> Tuple[int, Dict]:
        """
        获取泊位号

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/VesselInfo/GetBertNO"),
            params=dict(response_data_type=response_data_type),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /VesselInfo/GetBertNO, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

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
        resp = await async_post(
            url=parse.urljoin(self.url, "/VesselInfo/EditVesselInfo"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /VesselInfo/EditVesselInfo, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    async def ghostVehicleCancel(
        self, body: SetGhostVehicleCancelPost
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Gui-取消幽灵车

        """
        resp = await async_post(
            url=parse.urljoin(
                self.url, "/api/deviceInfo/vehicleStatus/ghostVehicleCancel"
            ),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/deviceInfo/vehicleStatus/ghostVehicleCancel, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

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
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/taskInfo/EquipmentStatus/"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/taskInfo/EquipmentStatus/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

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
        resp = await async_post(
            url=parse.urljoin(self.url, "/api/taskInfo/EquipmentStatus/SpreaderSize/"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /api/taskInfo/EquipmentStatus/SpreaderSize/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

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
        resp = await async_post(
            url=parse.urljoin(self.url, "/message/GetAllMessage"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /message/GetAllMessage, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def GetFileMessage(self, body: GetAllMessageCSVSchemas) -> Tuple[int, Dict]:
        """
        获取历史故障信息文件
        导出告警信息csv
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/message/GetFileMessage"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /message/GetFileMessage, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def UpdatePileInfo(
        self, body: UpdatePileInfoSchemas
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        单个充电桩操作

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/pileinfo/UpdatePileInfo"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /pileinfo/UpdatePileInfo, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    async def UpdateAllPileInfo(
        self, body: UpdateALlInfoSchemas
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        所有充电桩操作

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/pileinfo/UpdateAllPileInfo"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /pileinfo/UpdateAllPileInfo, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    async def ContainerInfoSetup(
        self, body: ContainerSteupSchemas
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        箱子增删改

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/denmarkinfo/ContainerInfoSetup"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /denmarkinfo/ContainerInfoSetup, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    async def PlcStatus(self, body: object) -> Tuple[int, CreateSuccessSchema]:
        """
        控制车辆应请

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/denmarkinfo/PlcStatus"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /denmarkinfo/PlcStatus, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    async def ServerVersion(self) -> Tuple[int, Dict]:
        """
        所有服务版本号

        """
        resp = await async_get(
            url=parse.urljoin(self.url, "/denmarkinfo/ServerVersion"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /denmarkinfo/ServerVersion, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    async def ForceOverTake(
        self, body: ForceOvertakeSchemas
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Over Take功能

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/TaskCorrelation/ForceOverTake/"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /TaskCorrelation/ForceOverTake/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    async def update_task(
        self, body: UpdateTaskSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Update Task

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/TaskCorrelation/update_task"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /TaskCorrelation/update_task, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    async def load_first(
        self, body: LoadFirstInSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Load First

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/TaskCorrelation/load_first"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /TaskCorrelation/load_first, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    async def redo_task(
        self, body: RedoTaskInSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Redo Task

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/TaskCorrelation/redo_task"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /TaskCorrelation/redo_task, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    async def CollectionFailTask(
        self, body: FailTaskSchemas
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        收集失败任务信息功能

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/TaskCorrelation/CollectionFailTask/"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /TaskCorrelation/CollectionFailTask/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

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
        resp = await async_post(
            url=parse.urljoin(self.url, "/TaskCorrelation/event_report"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /TaskCorrelation/event_report, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    async def TosLoginStatus(self, body: object) -> Tuple[int, CreateSuccessSchema]:
        """
        Tos登录登出

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/TosLoginStatus/"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /TosLoginStatus/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    async def twistlock_station(
        self, body: CRUDTwistlockStation, operation_type: ReceiveOperationType
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        增删改锁站Ts信息
        CREATE / UPDATE  /  DELETE
        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/twistlock_station/"),
            json=body.dict(),
            params=dict(operation_type=operation_type),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /twistlock_station/, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    async def GetPtions(self) -> Tuple[int, Dict]:
        """
        获取堆场贝位以及岸桥车道

        """
        resp = await async_post(
            url=parse.urljoin(self.url, "/get_ptions/GetPtions"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {self.url}, api: /get_ptions/GetPtions, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()


GuiServerRequest = GuiServerRequestCls()
