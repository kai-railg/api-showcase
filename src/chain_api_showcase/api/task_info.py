# -*- coding: utf-8 -*-

import os
from typing import Union, Tuple, Dict
from urllib import parse

from pydantic import BaseModel
from chain_http.async_client import (
    get as async_get,
    post as async_post,
    AsyncHttpResponse,
)

from ..schemas.task_info import *

FMS_IP_ADDRESS = f"http://{os.environ.get('FMS_IP_ADDRESS', '127.0.0.1')}"


class Task_InfoRequest(object):
    url = FMS_IP_ADDRESS + ":" + "10000"

    @classmethod
    async def api_taskInfo_maintain_status_post(cls) -> Tuple[int, Dict]:
        """
        Service Status

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/maintain/status"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/maintain/status, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def deleteAllArea(cls) -> Tuple[int, Dict]:
        """
        删除所有锁闭区

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/maintain/deleteAllArea"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/maintain/deleteAllArea, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def abortAllJob(cls) -> Tuple[int, Dict]:
        """
        取消所有任务

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/maintain/abortAllJob"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/maintain/abortAllJob, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def kvStore(
        cls, namespace: str, key: str, json_decode: bool = str(True).lower()
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        获取 Key-Value 存储值

        """
        resp = await async_get(
            url=parse.urljoin(cls.url, "/api/taskInfo/kvStore"),
            params=dict(namespace=namespace, key=key, json_decode=json_decode),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/kvStore, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_kvStore_post(
        cls, body: SetKvStoreInSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置 Key-Value 存储

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/kvStore"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/kvStore, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_kvStore_delete_post(
        cls, body: DeleteKvStore
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        删除 Key-Value 存储

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/kvStore/delete"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/kvStore/delete, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_kvStore_list_get(
        cls, namespace: str, key: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        获取 Key-Value List 存储值

        """
        resp = await async_get(
            url=parse.urljoin(cls.url, "/api/taskInfo/kvStore/list"),
            params=dict(namespace=namespace, key=key),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/kvStore/list, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_kvStore_list_post(
        cls, body: SetKvStoreListInSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置 Key-Value List 存储 (添加/移除/清空值)

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/kvStore/list"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/kvStore/list, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def listFind(
        cls, namespace: str, key: str, value: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        查找 Key-Value List 一个值是否存在

        """
        resp = await async_get(
            url=parse.urljoin(cls.url, "/api/taskInfo/kvStore/listFind"),
            params=dict(namespace=namespace, key=key, value=value),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/kvStore/listFind, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def process(cls, job_type: str) -> Tuple[int, GetBusProcessOutSchema]:
        """
        获取模板

        """
        resp = await async_get(
            url=parse.urljoin(cls.url, "/api/taskInfo/process"),
            params=dict(job_type=job_type),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/process, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, GetBusProcessOutSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_process_post(
        cls, body: SetBusProcessInSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置模板

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/process"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/process, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_containerInfo_get(cls, vehicle_id: str) -> Tuple[int, Dict]:
        """
        获取箱子信息

        """
        resp = await async_get(
            url=parse.urljoin(cls.url, "/api/taskInfo/containerInfo"),
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/containerInfo, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def api_taskInfo_containerInfo_post(
        cls, body: SetContainerInfoInSchema
    ) -> Tuple[int, Dict]:
        """
        修改箱子信息

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/containerInfo"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/containerInfo, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def create(cls, body: object) -> Tuple[int, CreateSuccessSchema]:
        """
        创建Job
        创建 Job
        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/vehicleJob/create"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/vehicleJob/create, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_vehicleJob_status_post(
        cls, vehicle_id: str, job_status: int, job_id: str, origin: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        更新任务状态

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/vehicleJob/status"),
            params=dict(
                vehicle_id=vehicle_id,
                job_status=job_status,
                job_id=job_id,
                origin=origin,
            ),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/vehicleJob/status, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def stage(
        cls, vehicle_id: str, job_id: str, job_stage: str = "CREATED"
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        更新任务进度

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/vehicleJob/stage"),
            params=dict(vehicle_id=vehicle_id, job_id=job_id, job_stage=job_stage),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/vehicleJob/stage, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def stage_vehicle(
        cls, vehicle_id: str, job_id: str, job_stage_vehicle: int
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        更新任务进度

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/vehicleJob/stage_vehicle"),
            params=dict(
                vehicle_id=vehicle_id,
                job_id=job_id,
                job_stage_vehicle=job_stage_vehicle,
            ),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/vehicleJob/stage_vehicle, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def businessKey(cls, vehicle_id: str) -> Tuple[int, CreateSuccessSchema]:
        """
        获取正在执行的业务Id

        """
        resp = await async_get(
            url=parse.urljoin(cls.url, "/api/taskInfo/vehicleJob/businessKey"),
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/vehicleJob/businessKey, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_vehicleJob_get(
        cls, vehicle_id: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        获取车辆的当前任务

        """
        resp = await async_get(
            url=parse.urljoin(cls.url, "/api/taskInfo/vehicleJob"),
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/vehicleJob, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def get(cls, job_id: str) -> Tuple[int, CreateSuccessSchema]:
        """
        使用 Job Id 获取 Job (Raw)

        """
        resp = await async_get(
            url=parse.urljoin(cls.url, "/api/taskInfo/vehicleJob/get"),
            params=dict(job_id=job_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/vehicleJob/get, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def getStd(cls, job_id: str) -> Tuple[int, CreateSuccessSchema]:
        """
        使用 Job Id 获取 Job (Std)

        """
        resp = await async_get(
            url=parse.urljoin(cls.url, "/api/taskInfo/vehicleJob/getStd"),
            params=dict(job_id=job_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/vehicleJob/getStd, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def getByMission(cls, mission_id: str) -> Tuple[int, CreateSuccessSchema]:
        """
        使用 Mission 获取 Job

        """
        resp = await async_get(
            url=parse.urljoin(cls.url, "/api/taskInfo/vehicleJob/getByMission"),
            params=dict(mission_id=mission_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/vehicleJob/getByMission, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_vehicleJob_abort_post(
        cls, vehicle_id: str, origin: str, cancel_reason: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        中止任务

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/vehicleJob/abort"),
            params=dict(
                vehicle_id=vehicle_id, origin=origin, cancel_reason=cancel_reason
            ),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/vehicleJob/abort, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def updateJobDest(
        cls, body: UpdateJobDest
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        更新任务目的位置

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/vehicleJob/updateJobDest"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/vehicleJob/updateJobDest, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def updateJobTask(
        cls, body: UpdateJobTask
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        更新任务

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/vehicleJob/updateJobTask"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/vehicleJob/updateJobTask, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def updatePlanContainers(
        cls, body: UpdatePlanContainers
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        更新任务计划箱子

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/vehicleJob/updatePlanContainers"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/vehicleJob/updatePlanContainers, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def updateAdditionalInfo(
        cls, body: UpdateAdditionalInfo
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        更新附加信息

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/vehicleJob/updateAdditionalInfo"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/vehicleJob/updateAdditionalInfo, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_vehicleJob_complete_post(
        cls, vehicle_id: str, job_status: int = "9"
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        正常结束任务

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/vehicleJob/complete"),
            params=dict(vehicle_id=vehicle_id, job_status=job_status),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/vehicleJob/complete, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def jobMission(
        cls, job_id: str, mission_id: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        获取 Job Mission

        """
        resp = await async_get(
            url=parse.urljoin(cls.url, "/api/taskInfo/vehicleJob/jobMission"),
            params=dict(job_id=job_id, mission_id=mission_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/vehicleJob/jobMission, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_vehicleJob_jobMission_post(
        cls, job_id: str, mission_id: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        绑定 Job Mission

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/vehicleJob/jobMission"),
            params=dict(job_id=job_id, mission_id=mission_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/vehicleJob/jobMission, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def stageTag(
        cls, vehicle_id: str, job_id: str, job_stage_tag: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        更新任务进度标签

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/vehicleJob/stageTag"),
            params=dict(
                vehicle_id=vehicle_id, job_id=job_id, job_stage_tag=job_stage_tag
            ),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/vehicleJob/stageTag, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_vehicleJob_resendJob_post(
        cls, body: ResendJobPost
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        重新派发旧任务
        允许 business_keys 或者 resend_jobs 两种形式的请求
        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/vehicleJob/resendJob"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/vehicleJob/resendJob, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_vehicleJob_delete_post(
        cls, body: DeleteJobPost
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        删除任务

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/vehicleJob/delete"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/vehicleJob/delete, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_vehicleJob_query_post(
        cls, body: QueryJobPost
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        任务查询

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/vehicleJob/query"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/vehicleJob/query, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def newest(cls, vehicle_id: str) -> Tuple[int, CreateSuccessSchema]:
        """
        获取车辆最后执行的任务

        """
        resp = await async_get(
            url=parse.urljoin(cls.url, "/api/taskInfo/vehicleJob/newest"),
            params=dict(vehicle_id=vehicle_id),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/vehicleJob/newest, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def all_newest_job(cls) -> Tuple[int, CreateSuccessSchema]:
        """
        获取所有车辆最后执行的任务

        """
        resp = await async_get(
            url=parse.urljoin(cls.url, "/api/taskInfo/vehicleJob/all_newest_job"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/vehicleJob/all_newest_job, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_vehicleJob_all_current_job_get(
        cls,
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        获取所有当前正在执行的任务

        """
        resp = await async_get(
            url=parse.urljoin(cls.url, "/api/taskInfo/vehicleJob/all_current_job"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/vehicleJob/all_current_job, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_vehicleJob_query_all_post(
        cls, body: QueryJobAllPost
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        历史任务查询

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/vehicleJob/query_all"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/vehicleJob/query_all, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def all_newest_job_filter(
        cls, origin: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        查询每个车最新的任务（带过滤器）

        """
        resp = await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/vehicleJob/all_newest_job_filter"
            ),
            params=dict(origin=origin),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/vehicleJob/all_newest_job_filter, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def virtual_points(cls) -> Tuple[int, CreateSuccessSchema]:
        """
        获取Virtual任务类型的点位

        """
        resp = await async_get(
            url=parse.urljoin(cls.url, "/api/taskInfo/vehicleJob/virtual_points"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/vehicleJob/virtual_points, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_vehicleJob_virtual_points_post(
        cls, body: VirtualPointsPost
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        存储Virtual任务类型的点位

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/vehicleJob/virtual_points"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/vehicleJob/virtual_points, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def workflowNodes(
        cls, body: SetWorkflowNodes
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        记录节点

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/vehicleJob/workflowNodes"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/vehicleJob/workflowNodes, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def workflowConfig(cls, config_item: str) -> Tuple[int, CreateSuccessSchema]:
        """
        获取工作流配置项

        """
        resp = await async_get(
            url=parse.urljoin(cls.url, "/api/taskInfo/workflowConfig"),
            params=dict(config_item=config_item),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/workflowConfig, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_workflowConfig_post(
        cls, config_item: str, value: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置工作流配置项

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/workflowConfig"),
            params=dict(config_item=config_item, value=value),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/workflowConfig, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_lockArea_get(
        cls, type: str, tag: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        获取锁闭区

        """
        resp = await async_get(
            url=parse.urljoin(cls.url, "/api/taskInfo/lockArea"),
            params=dict(type=type, tag=tag),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/lockArea, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_lockArea_post(
        cls, body: object
    ) -> Tuple[int, CreateSuccessSchema]:
        """
            创建锁闭区
            request params:
        {
            "name": "aqwef",
            "subtype": "lock",
            "type": "lock",
            "created_by": "",
            "describe": "",
            "polygon": [
            {
            "x": 171.6608123779297,
            "y": 165.42526245117188
            },
            {
            "x": 148.29757690429688,
            "y": 165.42526245117188
            },
            {
            "x": 148.29757690429688,
            "y": 146.14132690429688
            },
            {
            "x": 171.6608123779297,
            "y": 146.14132690429688
            },
            {
            "x": 171.6608123779297,
            "y": 165.42526245117188
            }
        ]
        }
        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/lockArea"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/lockArea, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_lockArea_delete_post(
        cls, body: object
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        删除锁闭区

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/lockArea/delete"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/lockArea/delete, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_lockArea_deleteByTag_post(
        cls, body: object
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        删除锁闭区(指定 Tag)

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/lockArea/deleteByTag"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/lockArea/deleteByTag, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_lockArea_change_post(
        cls, body: object
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        修改锁闭区

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/lockArea/change"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/lockArea/change, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def changeByTag(cls, body: object) -> Tuple[int, CreateSuccessSchema]:
        """
        通过标签修改锁闭区

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/lockArea/changeByTag"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/lockArea/changeByTag, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def update_or_create(cls, body: object) -> Tuple[int, CreateSuccessSchema]:
        """
        创建或者修改锁闭区

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/lockArea/update_or_create"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/lockArea/update_or_create, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_VesselInfo_SetVesselInfo_post(
        cls, body: SetVesselInfoSchemas
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        创建船舶

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/VesselInfo/SetVesselInfo"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/VesselInfo/SetVesselInfo, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_VesselInfo_EditVesselInfo_post(
        cls, body: object
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        修改船

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/VesselInfo/EditVesselInfo"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/VesselInfo/EditVesselInfo, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def GetVesselInfo(cls, vesselVisitId: str) -> Tuple[int, CreateSuccessSchema]:
        """
        获取船信息

        """
        resp = await async_get(
            url=parse.urljoin(cls.url, "/api/taskInfo/VesselInfo/GetVesselInfo"),
            params=dict(vesselVisitId=vesselVisitId),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/VesselInfo/GetVesselInfo, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def DeleteVesselInfo(
        cls, body: DelVesselInfoSchemas
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        删除船信息

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/VesselInfo/DeleteVesselInfo"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/VesselInfo/DeleteVesselInfo, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_VesselInfo_SetVesselInfoStatus_post(
        cls, body: SetVesselInfoStatusSchemas
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置自动建船开关

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/VesselInfo/SetVesselInfoStatus"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/VesselInfo/SetVesselInfoStatus, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def AlarmMessageStart(
        cls, body: SetAlarmMessage
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
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/Message/AlarmMessageStart"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/Message/AlarmMessageStart, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def AlarmMessageStart_bak(
        cls, body: SetAlarmMessage
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        单车上报告警信息开始

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/Message/AlarmMessageStart_bak"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/Message/AlarmMessageStart_bak, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def AlarmMessageStop(
        cls, body: StopAlarmMessage
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        单车上报告警信息结束

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/Message/AlarmMessageStop"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/Message/AlarmMessageStop, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def GetAlarmMessage(
        cls, body: AlarmMessageSchema
    ) -> Tuple[int, CreateSuccessSchemaCount]:
        """
        获取单车告警信息

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/Message/GetAlarmMessage"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/Message/GetAlarmMessage, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchemaCount.model_validate_json(resp)

    @classmethod
    async def SetFmsMessage(
        cls, body: SetFMSMessage
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置Fms告警信息

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/Message/SetFmsMessage"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/Message/SetFmsMessage, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def GetFmsMessage(
        cls, body: AlarmMessageSchema
    ) -> Tuple[int, CreateSuccessSchemaCount]:
        """
        获取Fms告警信息

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/Message/GetFmsMessage"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/Message/GetFmsMessage, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchemaCount.model_validate_json(resp)

    @classmethod
    async def set(cls, body: object) -> Tuple[int, CreateSuccessSchema]:
        """
        设置子任务

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/subTask/set"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/subTask/set, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_subTask_get_get(
        cls, vin: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        获取子任务

        """
        resp = await async_get(
            url=parse.urljoin(cls.url, "/api/taskInfo/subTask/get"),
            params=dict(vin=vin),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/subTask/get, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_subTask_clear_post(
        cls, vin: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        删除子任务

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/subTask/clear"),
            params=dict(vin=vin),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/subTask/clear, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def fenceEvent(cls, body: CreateFence) -> Tuple[int, CreateSuccessSchema]:
        """
        上报围栏事件

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/fenceEvent"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/fenceEvent, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def finish(cls, body: FinishFenceEvent) -> Tuple[int, CreateSuccessSchema]:
        """
        标记围栏事件完成

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/fenceEvent/finish"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/fenceEvent/finish, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_fenceEvent_get_post(
        cls,
        device_id: str,
        passing_location: str,
        passing_event: str,
        start_time: str,
        end_time: str,
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        获取围栏事件

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/fenceEvent/get"),
            params=dict(
                device_id=device_id,
                passing_location=passing_location,
                passing_event=passing_event,
                start_time=start_time,
                end_time=end_time,
            ),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/fenceEvent/get, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_taskPool_get_post(cls, body: object) -> Tuple[int, Dict]:
        """
        Get Task Pool

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/taskPool/get"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/taskPool/get, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def add(cls, body: object) -> Tuple[int, Dict]:
        """
        Add Task Pool

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/taskPool/add"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/taskPool/add, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def reject(cls, body: object) -> Tuple[int, Dict]:
        """
        Add Task Pool Reject

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/taskPool/reject"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/taskPool/reject, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def update(cls, body: object) -> Tuple[int, Dict]:
        """
        Update Task Pool

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/taskPool/update"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/taskPool/update, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def api_taskInfo_taskPool_abort_post(cls, body: object) -> Tuple[int, Dict]:
        """
        Abort Task Pool

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/taskPool/abort"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/taskPool/abort, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def api_taskInfo_taskPool_runImmediate_post(
        cls, body: object
    ) -> Tuple[int, Dict]:
        """
        Runimmediate

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/taskPool/runImmediate"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/taskPool/runImmediate, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def api_taskInfo_taskPool_delete_post(cls, body: object) -> Tuple[int, Dict]:
        """
        Delete Task Pool

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/taskPool/delete"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/taskPool/delete, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, resp.json()

    @classmethod
    async def TsRelated(cls, body: object) -> Tuple[int, CreateSuccessSchema]:
        """
        创建锁站

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/TsRelated"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/TsRelated, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_TsRelated_delete_post(
        cls, body: object
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        删除锁站

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/TsRelated/delete"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/TsRelated/delete, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def Edit(cls, body: object) -> Tuple[int, CreateSuccessSchema]:
        """
        修改Ts

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/TsRelated/Edit"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/TsRelated/Edit, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def Get(cls, body: GetTsSchemas) -> Tuple[int, CreateSuccessSchema]:
        """
        获取Ts

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/TsRelated/Get"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/TsRelated/Get, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_EquipmentStatus_post(
        cls, body: object
    ) -> Tuple[int, CreateSuccessSchema]:
        """
                设置Cms,Cps状态
                {
            "switch_val_name":"cms",
            "switch_val":"off"
        }
        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/EquipmentStatus"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/EquipmentStatus, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_EquipmentStatus_GetAll_get(
        cls,
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        获取Cms,Cps状态

        """
        resp = await async_get(
            url=parse.urljoin(cls.url, "/api/taskInfo/EquipmentStatus/GetAll"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/EquipmentStatus/GetAll, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_EquipmentStatus_Get_get(
        cls,
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        获取Cms,Cps状态

        """
        resp = await async_get(
            url=parse.urljoin(cls.url, "/api/taskInfo/EquipmentStatus/Get"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/EquipmentStatus/Get, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_EquipmentStatus_SpreaderSize_post(
        cls, body: object
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置吊具尺寸

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/EquipmentStatus/SpreaderSize"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/EquipmentStatus/SpreaderSize, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def GetSpreaderSize(
        cls, switch_val_name: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        获取吊具尺寸

        """
        resp = await async_get(
            url=parse.urljoin(cls.url, "/api/taskInfo/EquipmentStatus/GetSpreaderSize"),
            params=dict(switch_val_name=switch_val_name),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/EquipmentStatus/GetSpreaderSize, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_PaceGlobal_post(
        cls, body: object
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        配置全局速度

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/PaceGlobal"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/PaceGlobal, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_quayCrane_SetLane_post(
        cls, body: SetLaneInSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
                设置岸桥作业车道
                {
            "namespace": "guiServer:craneWorkLane",  # "tosInterface:craneWorkLane",
            "key": "Z1",
            "value": "02"
        }
        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/quayCrane/SetLane"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/quayCrane/SetLane, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def GetLane(cls) -> Tuple[int, CreateSuccessSchema]:
        """
                获取设置的岸桥作业车道
                {
            "namespace": "guiServer:craneWorkLane",
            "key": "Z1",
            "value": "02"
        }
        """
        resp = await async_get(
            url=parse.urljoin(cls.url, "/api/taskInfo/quayCrane/GetLane"),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/quayCrane/GetLane, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def preArrive(
        cls, body: PreArriveInSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        上报预到达

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/preArrive"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/preArrive, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def ts_switch(
        cls, ts_type: str, ts_name: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        查询锁站

        """
        resp = await async_get(
            url=parse.urljoin(cls.url, "/api/taskInfo/ts_switch"),
            params=dict(ts_type=ts_type, ts_name=ts_name),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/ts_switch, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_ts_switch_post(
        cls, body: LockSwitchInSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置更新锁站开关

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/ts_switch"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/ts_switch, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def automatic(
        cls, ts_type: str, ts_name: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        查询锁站

        """
        resp = await async_get(
            url=parse.urljoin(cls.url, "/api/taskInfo/ts_switch/automatic"),
            params=dict(ts_type=ts_type, ts_name=ts_name),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/ts_switch/automatic, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_ts_switch_automatic_post(
        cls, body: AutomaticTsSwitchSchema
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        设置更新锁站开关

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/ts_switch/automatic"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/ts_switch/automatic, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def api_taskInfo_ts_switch_automatic_delete(
        cls, ts_name: str
    ) -> Tuple[int, CreateSuccessSchema]:
        """
        删除锁站

        """
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/ts_switch/automatic, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def sim_start_job(cls, body: object) -> Tuple[int, CreateSuccessSchema]:
        """
        上报预到达

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/simApi/sim_start_job"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/simApi/sim_start_job, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)

    @classmethod
    async def fullControl(cls, body: FullStopStatus) -> Tuple[int, CreateSuccessSchema]:
        """
        全场紧停或者恢复

        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/taskInfo/fullControl"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/taskInfo/fullControl, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CreateSuccessSchema.model_validate_json(resp)
