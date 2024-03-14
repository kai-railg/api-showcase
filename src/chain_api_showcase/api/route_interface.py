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
from ..schemas.route_interface import *

__all__ = ["RouteInterfaceRequest"]


class RouteInterfaceRequestCls(ApiRequestBaseCls):
    def __init__(self):
        super(RouteInterfaceRequestCls, self).__init__()
        self.SERVICE_PORT = 55000
        self.SERVICE_NAME = "route_interface"
        self.module_mapping[self.SERVICE_NAME] = self

    async def update(self, body: UpdateRequest) -> Tuple[int, Dict]:
        """
        Update Navigation

        """
        return await self.request(
            request=async_post,
            api="/RoutingInterface/navigation/update",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def update_sync(self, body: UpdateRequest) -> Tuple[int, Dict]:
        """
        Update Navigation

        """
        return self.request_sync(
            request=requests.post,
            api="/RoutingInterface/navigation/update",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    async def get_path(
        self,
        device_id: str,
        trans_id: str,
        task_id: str,
        timestamp: int,
        traj_type: int,
    ) -> Tuple[int, Dict]:
        """
        Get Navigation

        """
        return await self.request(
            request=async_get,
            api="/RoutingInterface/navigation/get_path",
            body={
                "params": dict(
                    device_id=device_id,
                    trans_id=trans_id,
                    task_id=task_id,
                    timestamp=timestamp,
                    traj_type=traj_type,
                )
            },
            resp_model=None,
        )

    def get_path_sync(
        self,
        device_id: str,
        trans_id: str,
        task_id: str,
        timestamp: int,
        traj_type: int,
    ) -> Tuple[int, Dict]:
        """
        Get Navigation

        """
        return self.request_sync(
            request=requests.get,
            api="/RoutingInterface/navigation/get_path",
            body={
                "params": dict(
                    device_id=device_id,
                    trans_id=trans_id,
                    task_id=task_id,
                    timestamp=timestamp,
                    traj_type=traj_type,
                )
            },
            resp_model=None,
        )

    async def navi_status(self, body: UpdateRequest) -> Tuple[int, Dict]:
        """
        Update Navigation

        """
        return await self.request(
            request=async_post,
            api="/RoutingInterface/navigation/navi_status",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def navi_status_sync(self, body: UpdateRequest) -> Tuple[int, Dict]:
        """
        Update Navigation

        """
        return self.request_sync(
            request=requests.post,
            api="/RoutingInterface/navigation/navi_status",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )


RouteInterfaceRequest = RouteInterfaceRequestCls()
