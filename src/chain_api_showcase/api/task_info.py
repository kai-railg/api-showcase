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
from ..schemas.task_info import *

__all__ = ["TaskInfoRequest"]


class TaskInfoRequestCls(ApiRequestBaseCls):
    def __init__(self):
        super(TaskInfoRequestCls, self).__init__()
        self.SERVICE_PORT = 10000
        self.SERVICE_NAME = "task_info"
        self.module_mapping[self.SERVICE_NAME] = self

    async def api_taskInfo_maintain_status_post(self) -> Tuple[int, Dict]:
        """
        Service Status

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/maintain/status",
            body={},
            resp_model=None,
        )

    def api_taskInfo_maintain_status_post_sync(self) -> Tuple[int, Dict]:
        """
        Service Status

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/maintain/status",
            body={},
            resp_model=None,
        )

    async def deleteAllArea(self) -> Tuple[int, Dict]:
        """
        删除所有锁闭区

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/maintain/deleteAllArea",
            body={},
            resp_model=None,
        )

    def deleteAllArea_sync(self) -> Tuple[int, Dict]:
        """
        删除所有锁闭区

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/maintain/deleteAllArea",
            body={},
            resp_model=None,
        )

    async def abortAllJob(self) -> Tuple[int, Dict]:
        """
        取消所有任务

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/maintain/abortAllJob",
            body={},
            resp_model=None,
        )

    def abortAllJob_sync(self) -> Tuple[int, Dict]:
        """
        取消所有任务

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/maintain/abortAllJob",
            body={},
            resp_model=None,
        )

    async def kvStore(
        self, namespace: str, key: str, json_decode: bool = str(True).lower()
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        获取 Key-Value 存储值

        """
        return await self.request(
            request=async_get,
            api="/api/taskInfo/kvStore",
            body={
                "params": dict(namespace=namespace, key=key, json_decode=json_decode)
            },
            resp_model=CreateSuccessSchema,
        )

    def kvStore_sync(
        self, namespace: str, key: str, json_decode: bool = str(True).lower()
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        获取 Key-Value 存储值

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/kvStore",
            body={
                "params": dict(namespace=namespace, key=key, json_decode=json_decode)
            },
            resp_model=CreateSuccessSchema,
        )

    async def api_taskInfo_kvStore_post(
        self, body: SetKvStoreInSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置 Key-Value 存储

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/kvStore",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def api_taskInfo_kvStore_post_sync(
        self, body: SetKvStoreInSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置 Key-Value 存储

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/kvStore",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def api_taskInfo_kvStore_delete_post(
        self, body: DeleteKvStore
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        删除 Key-Value 存储

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/kvStore/delete",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def api_taskInfo_kvStore_delete_post_sync(
        self, body: DeleteKvStore
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        删除 Key-Value 存储

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/kvStore/delete",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def api_taskInfo_kvStore_list_get(
        self, namespace: str, key: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        获取 Key-Value List 存储值

        """
        return await self.request(
            request=async_get,
            api="/api/taskInfo/kvStore/list",
            body={"params": dict(namespace=namespace, key=key)},
            resp_model=CreateSuccessSchema,
        )

    def api_taskInfo_kvStore_list_get_sync(
        self, namespace: str, key: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        获取 Key-Value List 存储值

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/kvStore/list",
            body={"params": dict(namespace=namespace, key=key)},
            resp_model=CreateSuccessSchema,
        )

    async def api_taskInfo_kvStore_list_post(
        self, body: SetKvStoreListInSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置 Key-Value List 存储 (添加/移除/清空值)

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/kvStore/list",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def api_taskInfo_kvStore_list_post_sync(
        self, body: SetKvStoreListInSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置 Key-Value List 存储 (添加/移除/清空值)

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/kvStore/list",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def listFind(
        self, namespace: str, key: str, value: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        查找 Key-Value List 一个值是否存在

        """
        return await self.request(
            request=async_get,
            api="/api/taskInfo/kvStore/listFind",
            body={"params": dict(namespace=namespace, key=key, value=value)},
            resp_model=CreateSuccessSchema,
        )

    def listFind_sync(
        self, namespace: str, key: str, value: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        查找 Key-Value List 一个值是否存在

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/kvStore/listFind",
            body={"params": dict(namespace=namespace, key=key, value=value)},
            resp_model=CreateSuccessSchema,
        )

    async def process(self, job_type: str) -> Tuple[int, GetBusProcessOutSchema]:
        """
        获取模板

        """
        return await self.request(
            request=async_get,
            api="/api/taskInfo/process",
            body={"params": dict(job_type=job_type)},
            resp_model=GetBusProcessOutSchema,
        )

    def process_sync(self, job_type: str) -> Tuple[int, GetBusProcessOutSchema]:
        """
        获取模板

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/process",
            body={"params": dict(job_type=job_type)},
            resp_model=GetBusProcessOutSchema,
        )

    async def api_taskInfo_process_post(
        self, body: SetBusProcessInSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置模板

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/process",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def api_taskInfo_process_post_sync(
        self, body: SetBusProcessInSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置模板

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/process",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def api_taskInfo_containerInfo_get(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取箱子信息

        """
        return await self.request(
            request=async_get,
            api="/api/taskInfo/containerInfo",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=None,
        )

    def api_taskInfo_containerInfo_get_sync(self, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取箱子信息

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/containerInfo",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=None,
        )

    async def api_taskInfo_containerInfo_post(
        self, body: SetContainerInfoInSchema
    ) -> Tuple[int, Dict]:
        """
        修改箱子信息

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/containerInfo",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=None,
        )

    def api_taskInfo_containerInfo_post_sync(
        self, body: SetContainerInfoInSchema
    ) -> Tuple[int, Dict]:
        """
        修改箱子信息

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/containerInfo",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def create(self, body: object) -> Tuple[int, CreateSuccessSchema]:
        """
        创建Job
        创建 Job
        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/vehicleJob/create",
            body={
                "data": body,
            },
            resp_model=CreateSuccessSchema,
        )

    def create_sync(self, body: object) -> Tuple[int, CreateSuccessSchema]:
        """
        创建Job
        创建 Job
        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/vehicleJob/create",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def api_taskInfo_vehicleJob_status_post(
        self, vehicle_id: str, job_status: int, job_id: str, origin: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        更新任务状态

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/vehicleJob/status",
            body={
                "params": dict(
                    vehicle_id=vehicle_id,
                    job_status=job_status,
                    job_id=job_id,
                    origin=origin,
                )
            },
            resp_model=CreateSuccessSchema,
        )

    def api_taskInfo_vehicleJob_status_post_sync(
        self, vehicle_id: str, job_status: int, job_id: str, origin: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        更新任务状态

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/vehicleJob/status",
            body={
                "params": dict(
                    vehicle_id=vehicle_id,
                    job_status=job_status,
                    job_id=job_id,
                    origin=origin,
                )
            },
            resp_model=CreateSuccessSchema,
        )

    async def stage(
        self, vehicle_id: str, job_id: str, job_stage: str = "CREATED"
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        更新任务进度

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/vehicleJob/stage",
            body={
                "params": dict(
                    vehicle_id=vehicle_id, job_id=job_id, job_stage=job_stage
                )
            },
            resp_model=CreateSuccessSchema,
        )

    def stage_sync(
        self, vehicle_id: str, job_id: str, job_stage: str = "CREATED"
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        更新任务进度

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/vehicleJob/stage",
            body={
                "params": dict(
                    vehicle_id=vehicle_id, job_id=job_id, job_stage=job_stage
                )
            },
            resp_model=CreateSuccessSchema,
        )

    async def businessKey(self, vehicle_id: str) -> Tuple[int, CreateSuccessSchema]:
        """
        获取正在执行的业务Id

        """
        return await self.request(
            request=async_get,
            api="/api/taskInfo/vehicleJob/businessKey",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=CreateSuccessSchema,
        )

    def businessKey_sync(self, vehicle_id: str) -> Tuple[int, CreateSuccessSchema]:
        """
        获取正在执行的业务Id

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/vehicleJob/businessKey",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=CreateSuccessSchema,
        )

    async def api_taskInfo_vehicleJob_get(
        self, vehicle_id: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        获取车辆的当前任务

        """
        return await self.request(
            request=async_get,
            api="/api/taskInfo/vehicleJob",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=CreateSuccessSchema,
        )

    def api_taskInfo_vehicleJob_get_sync(
        self, vehicle_id: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        获取车辆的当前任务

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/vehicleJob",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=CreateSuccessSchema,
        )

    async def get(self, job_id: str) -> Tuple[int, CreateSuccessSchema]:
        """
        使用 Job Id 获取 Job (Raw)

        """
        return await self.request(
            request=async_get,
            api="/api/taskInfo/vehicleJob/get",
            body={"params": dict(job_id=job_id)},
            resp_model=CreateSuccessSchema,
        )

    def get_sync(self, job_id: str) -> Tuple[int, CreateSuccessSchema]:
        """
        使用 Job Id 获取 Job (Raw)

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/vehicleJob/get",
            body={"params": dict(job_id=job_id)},
            resp_model=CreateSuccessSchema,
        )

    async def getStd(self, job_id: str) -> Tuple[int, CreateSuccessSchema]:
        """
        使用 Job Id 获取 Job (Std)

        """
        return await self.request(
            request=async_get,
            api="/api/taskInfo/vehicleJob/getStd",
            body={"params": dict(job_id=job_id)},
            resp_model=CreateSuccessSchema,
        )

    def getStd_sync(self, job_id: str) -> Tuple[int, CreateSuccessSchema]:
        """
        使用 Job Id 获取 Job (Std)

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/vehicleJob/getStd",
            body={"params": dict(job_id=job_id)},
            resp_model=CreateSuccessSchema,
        )

    async def getByMission(self, mission_id: str) -> Tuple[int, CreateSuccessSchema]:
        """
        使用 Mission 获取 Job

        """
        return await self.request(
            request=async_get,
            api="/api/taskInfo/vehicleJob/getByMission",
            body={"params": dict(mission_id=mission_id)},
            resp_model=CreateSuccessSchema,
        )

    def getByMission_sync(self, mission_id: str) -> Tuple[int, CreateSuccessSchema]:
        """
        使用 Mission 获取 Job

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/vehicleJob/getByMission",
            body={"params": dict(mission_id=mission_id)},
            resp_model=CreateSuccessSchema,
        )

    async def api_taskInfo_vehicleJob_abort_post(
        self, vehicle_id: str, origin: str, cancel_reason: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        中止任务

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/vehicleJob/abort",
            body={
                "params": dict(
                    vehicle_id=vehicle_id, origin=origin, cancel_reason=cancel_reason
                )
            },
            resp_model=CreateSuccessSchema,
        )

    def api_taskInfo_vehicleJob_abort_post_sync(
        self, vehicle_id: str, origin: str, cancel_reason: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        中止任务

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/vehicleJob/abort",
            body={
                "params": dict(
                    vehicle_id=vehicle_id, origin=origin, cancel_reason=cancel_reason
                )
            },
            resp_model=CreateSuccessSchema,
        )

    async def updateJobDest(
        self, body: UpdateJobDest
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        更新任务目的位置

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/vehicleJob/updateJobDest",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def updateJobDest_sync(
        self, body: UpdateJobDest
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        更新任务目的位置

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/vehicleJob/updateJobDest",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def updatePlanContainers(
        self, body: UpdatePlanContainers
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        更新任务计划箱子

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/vehicleJob/updatePlanContainers",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def updatePlanContainers_sync(
        self, body: UpdatePlanContainers
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        更新任务计划箱子

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/vehicleJob/updatePlanContainers",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def api_taskInfo_vehicleJob_complete_post(
        self, vehicle_id: str, job_status: int = "9"
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        正常结束任务

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/vehicleJob/complete",
            body={"params": dict(vehicle_id=vehicle_id, job_status=job_status)},
            resp_model=CreateSuccessSchema,
        )

    def api_taskInfo_vehicleJob_complete_post_sync(
        self, vehicle_id: str, job_status: int = "9"
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        正常结束任务

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/vehicleJob/complete",
            body={"params": dict(vehicle_id=vehicle_id, job_status=job_status)},
            resp_model=CreateSuccessSchema,
        )

    async def jobMission(
        self, job_id: str, mission_id: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        获取 Job Mission

        """
        return await self.request(
            request=async_get,
            api="/api/taskInfo/vehicleJob/jobMission",
            body={"params": dict(job_id=job_id, mission_id=mission_id)},
            resp_model=CreateSuccessSchema,
        )

    def jobMission_sync(
        self, job_id: str, mission_id: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        获取 Job Mission

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/vehicleJob/jobMission",
            body={"params": dict(job_id=job_id, mission_id=mission_id)},
            resp_model=CreateSuccessSchema,
        )

    async def api_taskInfo_vehicleJob_jobMission_post(
        self, job_id: str, mission_id: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        绑定 Job Mission

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/vehicleJob/jobMission",
            body={"params": dict(job_id=job_id, mission_id=mission_id)},
            resp_model=CreateSuccessSchema,
        )

    def api_taskInfo_vehicleJob_jobMission_post_sync(
        self, job_id: str, mission_id: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        绑定 Job Mission

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/vehicleJob/jobMission",
            body={"params": dict(job_id=job_id, mission_id=mission_id)},
            resp_model=CreateSuccessSchema,
        )

    async def stageTag(
        self, vehicle_id: str, job_id: str, job_stage_tag: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        更新任务进度标签

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/vehicleJob/stageTag",
            body={
                "params": dict(
                    vehicle_id=vehicle_id, job_id=job_id, job_stage_tag=job_stage_tag
                )
            },
            resp_model=CreateSuccessSchema,
        )

    def stageTag_sync(
        self, vehicle_id: str, job_id: str, job_stage_tag: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        更新任务进度标签

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/vehicleJob/stageTag",
            body={
                "params": dict(
                    vehicle_id=vehicle_id, job_id=job_id, job_stage_tag=job_stage_tag
                )
            },
            resp_model=CreateSuccessSchema,
        )

    async def api_taskInfo_vehicleJob_resendJob_post(
        self, body: ResendJobPost
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        重新派发旧任务
        允许 business_keys 或者 resend_jobs 两种形式的请求
        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/vehicleJob/resendJob",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def api_taskInfo_vehicleJob_resendJob_post_sync(
        self, body: ResendJobPost
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        重新派发旧任务
        允许 business_keys 或者 resend_jobs 两种形式的请求
        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/vehicleJob/resendJob",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def api_taskInfo_vehicleJob_delete_post(
        self, body: DeleteJobPost
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        删除任务

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/vehicleJob/delete",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def api_taskInfo_vehicleJob_delete_post_sync(
        self, body: DeleteJobPost
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        删除任务

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/vehicleJob/delete",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def api_taskInfo_vehicleJob_query_post(
        self, body: QueryJobPost
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        任务查询

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/vehicleJob/query",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def api_taskInfo_vehicleJob_query_post_sync(
        self, body: QueryJobPost
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        任务查询

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/vehicleJob/query",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def newest(self, vehicle_id: str) -> Tuple[int, CreateSuccessSchema]:
        """
        获取车辆最后执行的任务

        """
        return await self.request(
            request=async_get,
            api="/api/taskInfo/vehicleJob/newest",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=CreateSuccessSchema,
        )

    def newest_sync(self, vehicle_id: str) -> Tuple[int, CreateSuccessSchema]:
        """
        获取车辆最后执行的任务

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/vehicleJob/newest",
            body={"params": dict(vehicle_id=vehicle_id)},
            resp_model=CreateSuccessSchema,
        )

    async def all_newest_job(self) -> Tuple[int, CreateSuccessSchema]:
        """
        获取所有车辆最后执行的任务

        """
        return await self.request(
            request=async_get,
            api="/api/taskInfo/vehicleJob/all_newest_job",
            body={},
            resp_model=CreateSuccessSchema,
        )

    def all_newest_job_sync(self) -> Tuple[int, CreateSuccessSchema]:
        """
        获取所有车辆最后执行的任务

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/vehicleJob/all_newest_job",
            body={},
            resp_model=CreateSuccessSchema,
        )

    async def api_taskInfo_vehicleJob_all_current_job_get(
        self,
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        获取所有当前正在执行的任务

        """
        return await self.request(
            request=async_get,
            api="/api/taskInfo/vehicleJob/all_current_job",
            body={},
            resp_model=CreateSuccessSchema,
        )

    def api_taskInfo_vehicleJob_all_current_job_get_sync(
        self,
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        获取所有当前正在执行的任务

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/vehicleJob/all_current_job",
            body={},
            resp_model=CreateSuccessSchema,
        )

    async def api_taskInfo_vehicleJob_query_all_post(
        self, body: QueryJobAllPost
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        历史任务查询

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/vehicleJob/query_all",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def api_taskInfo_vehicleJob_query_all_post_sync(
        self, body: QueryJobAllPost
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        历史任务查询

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/vehicleJob/query_all",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def all_newest_job_filter(
        self, origin: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        查询每个车最新的任务（带过滤器）

        """
        return await self.request(
            request=async_get,
            api="/api/taskInfo/vehicleJob/all_newest_job_filter",
            body={"params": dict(origin=origin)},
            resp_model=CreateSuccessSchema,
        )

    def all_newest_job_filter_sync(
        self, origin: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        查询每个车最新的任务（带过滤器）

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/vehicleJob/all_newest_job_filter",
            body={"params": dict(origin=origin)},
            resp_model=CreateSuccessSchema,
        )

    async def virtual_points(self) -> Tuple[int, CreateSuccessSchema]:
        """
        获取Virtual任务类型的点位

        """
        return await self.request(
            request=async_get,
            api="/api/taskInfo/vehicleJob/virtual_points",
            body={},
            resp_model=CreateSuccessSchema,
        )

    def virtual_points_sync(self) -> Tuple[int, CreateSuccessSchema]:
        """
        获取Virtual任务类型的点位

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/vehicleJob/virtual_points",
            body={},
            resp_model=CreateSuccessSchema,
        )

    async def api_taskInfo_vehicleJob_virtual_points_post(
        self, body: VirtualPointsPost
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        存储Virtual任务类型的点位

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/vehicleJob/virtual_points",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def api_taskInfo_vehicleJob_virtual_points_post_sync(
        self, body: VirtualPointsPost
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        存储Virtual任务类型的点位

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/vehicleJob/virtual_points",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def workflowConfig(self, config_item: str) -> Tuple[int, CreateSuccessSchema]:
        """
        获取工作流配置项

        """
        return await self.request(
            request=async_get,
            api="/api/taskInfo/workflowConfig",
            body={"params": dict(config_item=config_item)},
            resp_model=CreateSuccessSchema,
        )

    def workflowConfig_sync(self, config_item: str) -> Tuple[int, CreateSuccessSchema]:
        """
        获取工作流配置项

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/workflowConfig",
            body={"params": dict(config_item=config_item)},
            resp_model=CreateSuccessSchema,
        )

    async def api_taskInfo_workflowConfig_post(
        self, config_item: str, value: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置工作流配置项

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/workflowConfig",
            body={"params": dict(config_item=config_item, value=value)},
            resp_model=CreateSuccessSchema,
        )

    def api_taskInfo_workflowConfig_post_sync(
        self, config_item: str, value: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置工作流配置项

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/workflowConfig",
            body={"params": dict(config_item=config_item, value=value)},
            resp_model=CreateSuccessSchema,
        )

    async def api_taskInfo_lockArea_get(
        self, type: str, tag: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        获取锁闭区

        """
        return await self.request(
            request=async_get,
            api="/api/taskInfo/lockArea",
            body={"params": dict(type=type, tag=tag)},
            resp_model=CreateSuccessSchema,
        )

    def api_taskInfo_lockArea_get_sync(
        self, type: str, tag: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        获取锁闭区

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/lockArea",
            body={"params": dict(type=type, tag=tag)},
            resp_model=CreateSuccessSchema,
        )

    async def api_taskInfo_lockArea_post(
        self, body: object
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        创建锁闭区

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/lockArea",
            body={
                "data": body,
            },
            resp_model=CreateSuccessSchema,
        )

    def api_taskInfo_lockArea_post_sync(
        self, body: object
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        创建锁闭区

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/lockArea",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def api_taskInfo_lockArea_delete_post(
        self, body: object
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        删除锁闭区

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/lockArea/delete",
            body={
                "data": body,
            },
            resp_model=CreateSuccessSchema,
        )

    def api_taskInfo_lockArea_delete_post_sync(
        self, body: object
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        删除锁闭区

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/lockArea/delete",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def api_taskInfo_lockArea_deleteByTag_post(
        self, body: object
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        删除锁闭区(指定 Tag)

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/lockArea/deleteByTag",
            body={
                "data": body,
            },
            resp_model=CreateSuccessSchema,
        )

    def api_taskInfo_lockArea_deleteByTag_post_sync(
        self, body: object
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        删除锁闭区(指定 Tag)

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/lockArea/deleteByTag",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def api_taskInfo_lockArea_change_post(
        self, body: object
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        修改锁闭区

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/lockArea/change",
            body={
                "data": body,
            },
            resp_model=CreateSuccessSchema,
        )

    def api_taskInfo_lockArea_change_post_sync(
        self, body: object
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        修改锁闭区

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/lockArea/change",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def changeByTag(self, body: object) -> Tuple[int, CreateSuccessSchema]:
        """
        通过标签修改锁闭区

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/lockArea/changeByTag",
            body={
                "data": body,
            },
            resp_model=CreateSuccessSchema,
        )

    def changeByTag_sync(self, body: object) -> Tuple[int, CreateSuccessSchema]:
        """
        通过标签修改锁闭区

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/lockArea/changeByTag",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def api_taskInfo_VesselInfo_SetVesselInfo_post(
        self, body: SetVesselInfoSchemas
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        创建船舶

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/VesselInfo/SetVesselInfo",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def api_taskInfo_VesselInfo_SetVesselInfo_post_sync(
        self, body: SetVesselInfoSchemas
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        创建船舶

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/VesselInfo/SetVesselInfo",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def api_taskInfo_VesselInfo_EditVesselInfo_post(
        self, body: object
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        修改船

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/VesselInfo/EditVesselInfo",
            body={
                "data": body,
            },
            resp_model=CreateSuccessSchema,
        )

    def api_taskInfo_VesselInfo_EditVesselInfo_post_sync(
        self, body: object
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        修改船

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/VesselInfo/EditVesselInfo",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def GetVesselInfo(
        self, vesselVisitId: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        获取船信息

        """
        return await self.request(
            request=async_get,
            api="/api/taskInfo/VesselInfo/GetVesselInfo",
            body={"params": dict(vesselVisitId=vesselVisitId)},
            resp_model=CreateSuccessSchema,
        )

    def GetVesselInfo_sync(self, vesselVisitId: str) -> Tuple[int, CreateSuccessSchema]:
        """
        获取船信息

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/VesselInfo/GetVesselInfo",
            body={"params": dict(vesselVisitId=vesselVisitId)},
            resp_model=CreateSuccessSchema,
        )

    async def DeleteVesselInfo(
        self, body: DelVesselInfoSchemas
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        删除船信息

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/VesselInfo/DeleteVesselInfo",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def DeleteVesselInfo_sync(
        self, body: DelVesselInfoSchemas
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        删除船信息

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/VesselInfo/DeleteVesselInfo",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def api_taskInfo_VesselInfo_SetVesselInfoStatus_post(
        self, body: SetVesselInfoStatusSchemas
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置自动建船开关

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/VesselInfo/SetVesselInfoStatus",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def api_taskInfo_VesselInfo_SetVesselInfoStatus_post_sync(
        self, body: SetVesselInfoStatusSchemas
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置自动建船开关

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/VesselInfo/SetVesselInfoStatus",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def AlarmMessageStart(
        self, body: SetAlarmMessage
    ) -> Tuple[int, CreateSuccessSchema]:
        """
                单车上报告警信息开始
                {
        "deviceId": "AT01",
        "error_info": [
            {
                "deviceId": "AT01",
                "timestamp": "1699430289",
                "alarmLevel": 3,
                "alarmCode": 1002,
                "alarmType": 0,
                "subCode": 0,
                "description": "Sensor driver level 3 malfunction. AT has stopped immediately. Please click "Reset" to restart the system.",
                "subDescription": "null",
                "messageType": "truck"
            }
        ],
        "error_origin": "system"  # chassis
        }
        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/Message/AlarmMessageStart",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def AlarmMessageStart_sync(
        self, body: SetAlarmMessage
    ) -> Tuple[int, CreateSuccessSchema]:
        """
                单车上报告警信息开始
                {
        "deviceId": "AT01",
        "error_info": [
            {
                "deviceId": "AT01",
                "timestamp": "1699430289",
                "alarmLevel": 3,
                "alarmCode": 1002,
                "alarmType": 0,
                "subCode": 0,
                "description": "Sensor driver level 3 malfunction. AT has stopped immediately. Please click "Reset" to restart the system.",
                "subDescription": "null",
                "messageType": "truck"
            }
        ],
        "error_origin": "system"  # chassis
        }
        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/Message/AlarmMessageStart",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def AlarmMessageStart_bak(
        self, body: SetAlarmMessage
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        单车上报告警信息开始

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/Message/AlarmMessageStart_bak",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def AlarmMessageStart_bak_sync(
        self, body: SetAlarmMessage
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        单车上报告警信息开始

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/Message/AlarmMessageStart_bak",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def AlarmMessageStop(
        self, body: StopAlarmMessage
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        单车上报告警信息结束

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/Message/AlarmMessageStop",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def AlarmMessageStop_sync(
        self, body: StopAlarmMessage
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        单车上报告警信息结束

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/Message/AlarmMessageStop",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def GetAlarmMessage(
        self, body: AlarmMessageSchema
    ) -> Tuple[int, CreateSuccessSchemaCount]:
        """
        获取单车告警信息

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/Message/GetAlarmMessage",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchemaCount,
        )

    def GetAlarmMessage_sync(
        self, body: AlarmMessageSchema
    ) -> Tuple[int, CreateSuccessSchemaCount]:
        """
        获取单车告警信息

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/Message/GetAlarmMessage",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchemaCount,
        )

    async def SetFmsMessage(
        self, body: SetFMSMessage
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Fms告警信息

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/Message/SetFmsMessage",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def SetFmsMessage_sync(
        self, body: SetFMSMessage
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        Fms告警信息

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/Message/SetFmsMessage",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def GetFmsMessage(
        self, body: AlarmMessageSchema
    ) -> Tuple[int, CreateSuccessSchemaCount]:
        """
        获取Fms告警信息

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/Message/GetFmsMessage",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchemaCount,
        )

    def GetFmsMessage_sync(
        self, body: AlarmMessageSchema
    ) -> Tuple[int, CreateSuccessSchemaCount]:
        """
        获取Fms告警信息

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/Message/GetFmsMessage",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchemaCount,
        )

    async def set(self, body: object) -> Tuple[int, CreateSuccessSchema]:
        """
        设置子任务

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/subTask/set",
            body={
                "data": body,
            },
            resp_model=CreateSuccessSchema,
        )

    def set_sync(self, body: object) -> Tuple[int, CreateSuccessSchema]:
        """
        设置子任务

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/subTask/set",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def api_taskInfo_subTask_get_get(
        self, vin: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        获取子任务

        """
        return await self.request(
            request=async_get,
            api="/api/taskInfo/subTask/get",
            body={"params": dict(vin=vin)},
            resp_model=CreateSuccessSchema,
        )

    def api_taskInfo_subTask_get_get_sync(
        self, vin: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        获取子任务

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/subTask/get",
            body={"params": dict(vin=vin)},
            resp_model=CreateSuccessSchema,
        )

    async def api_taskInfo_subTask_clear_post(
        self, vin: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        删除子任务

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/subTask/clear",
            body={"params": dict(vin=vin)},
            resp_model=CreateSuccessSchema,
        )

    def api_taskInfo_subTask_clear_post_sync(
        self, vin: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        删除子任务

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/subTask/clear",
            body={"params": dict(vin=vin)},
            resp_model=CreateSuccessSchema,
        )

    async def fenceEvent(self, body: CreateFence) -> Tuple[int, CreateSuccessSchema]:
        """
        上报围栏事件

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/fenceEvent",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def fenceEvent_sync(self, body: CreateFence) -> Tuple[int, CreateSuccessSchema]:
        """
        上报围栏事件

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/fenceEvent",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def finish(self, body: FinishFenceEvent) -> Tuple[int, CreateSuccessSchema]:
        """
        标记围栏事件完成

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/fenceEvent/finish",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def finish_sync(self, body: FinishFenceEvent) -> Tuple[int, CreateSuccessSchema]:
        """
        标记围栏事件完成

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/fenceEvent/finish",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def api_taskInfo_fenceEvent_get_post(
        self,
        device_id: str,
        passing_location: str,
        passing_event: str,
        start_time: str,
        end_time: str,
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        获取围栏事件

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/fenceEvent/get",
            body={
                "params": dict(
                    device_id=device_id,
                    passing_location=passing_location,
                    passing_event=passing_event,
                    start_time=start_time,
                    end_time=end_time,
                )
            },
            resp_model=CreateSuccessSchema,
        )

    def api_taskInfo_fenceEvent_get_post_sync(
        self,
        device_id: str,
        passing_location: str,
        passing_event: str,
        start_time: str,
        end_time: str,
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        获取围栏事件

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/fenceEvent/get",
            body={
                "params": dict(
                    device_id=device_id,
                    passing_location=passing_location,
                    passing_event=passing_event,
                    start_time=start_time,
                    end_time=end_time,
                )
            },
            resp_model=CreateSuccessSchema,
        )

    async def api_taskInfo_taskPool_get_post(self, body: object) -> Tuple[int, Dict]:
        """
        Get Task Pool

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/taskPool/get",
            body={
                "data": body,
            },
            resp_model=None,
        )

    def api_taskInfo_taskPool_get_post_sync(self, body: object) -> Tuple[int, Dict]:
        """
        Get Task Pool

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/taskPool/get",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def add(self, body: object) -> Tuple[int, Dict]:
        """
        Add Task Pool

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/taskPool/add",
            body={
                "data": body,
            },
            resp_model=None,
        )

    def add_sync(self, body: object) -> Tuple[int, Dict]:
        """
        Add Task Pool

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/taskPool/add",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def api_taskInfo_taskPool_update_post(self, body: object) -> Tuple[int, Dict]:
        """
        Update Task Pool

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/taskPool/update",
            body={
                "data": body,
            },
            resp_model=None,
        )

    def api_taskInfo_taskPool_update_post_sync(self, body: object) -> Tuple[int, Dict]:
        """
        Update Task Pool

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/taskPool/update",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def api_taskInfo_taskPool_abort_post(self, body: object) -> Tuple[int, Dict]:
        """
        Abort Task Pool

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/taskPool/abort",
            body={
                "data": body,
            },
            resp_model=None,
        )

    def api_taskInfo_taskPool_abort_post_sync(self, body: object) -> Tuple[int, Dict]:
        """
        Abort Task Pool

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/taskPool/abort",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def api_taskInfo_taskPool_runImmediate_post(
        self, body: object
    ) -> Tuple[int, Dict]:
        """
        Runimmediate

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/taskPool/runImmediate",
            body={
                "data": body,
            },
            resp_model=None,
        )

    def api_taskInfo_taskPool_runImmediate_post_sync(
        self, body: object
    ) -> Tuple[int, Dict]:
        """
        Runimmediate

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/taskPool/runImmediate",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def api_taskInfo_taskPool_delete_post(self, body: object) -> Tuple[int, Dict]:
        """
        Delete Task Pool

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/taskPool/delete",
            body={
                "data": body,
            },
            resp_model=None,
        )

    def api_taskInfo_taskPool_delete_post_sync(self, body: object) -> Tuple[int, Dict]:
        """
        Delete Task Pool

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/taskPool/delete",
            body={
                "data": body,
            },
            resp_model=None,
        )

    async def TsRelated(self, body: object) -> Tuple[int, CreateSuccessSchema]:
        """
        创建锁站

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/TsRelated",
            body={
                "data": body,
            },
            resp_model=CreateSuccessSchema,
        )

    def TsRelated_sync(self, body: object) -> Tuple[int, CreateSuccessSchema]:
        """
        创建锁站

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/TsRelated",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def api_taskInfo_TsRelated_delete_post(
        self, body: object
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        删除锁站

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/TsRelated/delete",
            body={
                "data": body,
            },
            resp_model=CreateSuccessSchema,
        )

    def api_taskInfo_TsRelated_delete_post_sync(
        self, body: object
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        删除锁站

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/TsRelated/delete",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def Edit(self, body: object) -> Tuple[int, CreateSuccessSchema]:
        """
        修改Ts

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/TsRelated/Edit",
            body={
                "data": body,
            },
            resp_model=CreateSuccessSchema,
        )

    def Edit_sync(self, body: object) -> Tuple[int, CreateSuccessSchema]:
        """
        修改Ts

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/TsRelated/Edit",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def Get(self, body: GetTsSchemas) -> Tuple[int, CreateSuccessSchema]:
        """
        获取Ts

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/TsRelated/Get",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def Get_sync(self, body: GetTsSchemas) -> Tuple[int, CreateSuccessSchema]:
        """
        获取Ts

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/TsRelated/Get",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def api_taskInfo_EquipmentStatus_post(
        self, body: object
    ) -> Tuple[int, CreateSuccessSchema]:
        """
                设置Cms,Cps状态
                {
            "switch_val_name":"cms",
            "switch_val":"off"
        }
        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/EquipmentStatus",
            body={
                "data": body,
            },
            resp_model=CreateSuccessSchema,
        )

    def api_taskInfo_EquipmentStatus_post_sync(
        self, body: object
    ) -> Tuple[int, CreateSuccessSchema]:
        """
                设置Cms,Cps状态
                {
            "switch_val_name":"cms",
            "switch_val":"off"
        }
        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/EquipmentStatus",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def api_taskInfo_EquipmentStatus_Get_get(
        self,
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        获取Cms,Cps状态

        """
        return await self.request(
            request=async_get,
            api="/api/taskInfo/EquipmentStatus/Get",
            body={},
            resp_model=CreateSuccessSchema,
        )

    def api_taskInfo_EquipmentStatus_Get_get_sync(
        self,
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        获取Cms,Cps状态

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/EquipmentStatus/Get",
            body={},
            resp_model=CreateSuccessSchema,
        )

    async def api_taskInfo_EquipmentStatus_SpreaderSize_post(
        self, body: object
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置吊具尺寸

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/EquipmentStatus/SpreaderSize",
            body={
                "data": body,
            },
            resp_model=CreateSuccessSchema,
        )

    def api_taskInfo_EquipmentStatus_SpreaderSize_post_sync(
        self, body: object
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置吊具尺寸

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/EquipmentStatus/SpreaderSize",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def GetSpreaderSize(
        self, switch_val_name: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        获取吊具尺寸

        """
        return await self.request(
            request=async_get,
            api="/api/taskInfo/EquipmentStatus/GetSpreaderSize",
            body={"params": dict(switch_val_name=switch_val_name)},
            resp_model=CreateSuccessSchema,
        )

    def GetSpreaderSize_sync(
        self, switch_val_name: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        获取吊具尺寸

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/EquipmentStatus/GetSpreaderSize",
            body={"params": dict(switch_val_name=switch_val_name)},
            resp_model=CreateSuccessSchema,
        )

    async def api_taskInfo_PaceGlobal_post(
        self, body: object
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        配置全局速度

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/PaceGlobal",
            body={
                "data": body,
            },
            resp_model=CreateSuccessSchema,
        )

    def api_taskInfo_PaceGlobal_post_sync(
        self, body: object
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        配置全局速度

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/PaceGlobal",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def api_taskInfo_quayCrane_SetLane_post(
        self, body: SetLaneInSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
                设置岸桥作业车道
                {
            "namespace": "guiServer:craneWorkLane",  # "tosInterface:craneWorkLane",
            "key": "Z1",
            "value": "02"
        }
        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/quayCrane/SetLane",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def api_taskInfo_quayCrane_SetLane_post_sync(
        self, body: SetLaneInSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
                设置岸桥作业车道
                {
            "namespace": "guiServer:craneWorkLane",  # "tosInterface:craneWorkLane",
            "key": "Z1",
            "value": "02"
        }
        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/quayCrane/SetLane",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def GetLane(self) -> Tuple[int, CreateSuccessSchema]:
        """
                获取设置的岸桥作业车道
                {
            "namespace": "guiServer:craneWorkLane",
            "key": "Z1",
            "value": "02"
        }
        """
        return await self.request(
            request=async_get,
            api="/api/taskInfo/quayCrane/GetLane",
            body={},
            resp_model=CreateSuccessSchema,
        )

    def GetLane_sync(self) -> Tuple[int, CreateSuccessSchema]:
        """
                获取设置的岸桥作业车道
                {
            "namespace": "guiServer:craneWorkLane",
            "key": "Z1",
            "value": "02"
        }
        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/quayCrane/GetLane",
            body={},
            resp_model=CreateSuccessSchema,
        )

    async def preArrive(
        self, body: PreArriveInSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        上报预到达

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/preArrive",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def preArrive_sync(
        self, body: PreArriveInSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        上报预到达

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/preArrive",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def ts_switch(
        self, ts_type: str, ts_name: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        查询锁站

        """
        return await self.request(
            request=async_get,
            api="/api/taskInfo/ts_switch",
            body={"params": dict(ts_type=ts_type, ts_name=ts_name)},
            resp_model=CreateSuccessSchema,
        )

    def ts_switch_sync(
        self, ts_type: str, ts_name: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        查询锁站

        """
        return self.request_sync(
            request=requests.get,
            api="/api/taskInfo/ts_switch",
            body={"params": dict(ts_type=ts_type, ts_name=ts_name)},
            resp_model=CreateSuccessSchema,
        )

    async def api_taskInfo_ts_switch_post(
        self, body: LockSwitchInSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置更新锁站开关

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/ts_switch",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def api_taskInfo_ts_switch_post_sync(
        self, body: LockSwitchInSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置更新锁站开关

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/ts_switch",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def sim_start_job(self, body: object) -> Tuple[int, CreateSuccessSchema]:
        """
        上报预到达

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/simApi/sim_start_job",
            body={
                "data": body,
            },
            resp_model=CreateSuccessSchema,
        )

    def sim_start_job_sync(self, body: object) -> Tuple[int, CreateSuccessSchema]:
        """
        上报预到达

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/simApi/sim_start_job",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    async def fullControl(
        self, body: FullStopStatus
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        全场紧停或者恢复

        """
        return await self.request(
            request=async_post,
            api="/api/taskInfo/fullControl",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )

    def fullControl_sync(self, body: FullStopStatus) -> Tuple[int, CreateSuccessSchema]:
        """
        全场紧停或者恢复

        """
        return self.request_sync(
            request=requests.post,
            api="/api/taskInfo/fullControl",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CreateSuccessSchema,
        )


TaskInfoRequest = TaskInfoRequestCls()
