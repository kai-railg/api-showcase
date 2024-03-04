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

from ..schemas.task_info import *

FMS_IP_ADDRESS = f"http://{os.environ.get('FMS_IP_ADDRESS', '127.0.0.1')}"


class Task_InfoRequest(object):
    url = FMS_IP_ADDRESS + ":" + "10000"
    
    @classmethod
    async def api_taskInfo_maintain_status_post(cls, ) -> AsyncHttpResponse:
        """
        Service Status
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/maintain/status"
            ),
            
            
        )
         
    @classmethod
    async def deleteAllArea(cls, ) -> AsyncHttpResponse:
        """
        删除所有锁闭区
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/maintain/deleteAllArea"
            ),
            
            
        )
         
    @classmethod
    async def abortAllJob(cls, ) -> AsyncHttpResponse:
        """
        取消所有任务
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/maintain/abortAllJob"
            ),
            
            
        )
         
    @classmethod
    async def kvStore(cls, namespace: str, key: str, json_decode: bool) -> AsyncHttpResponse:
        """
        获取 Key-Value 存储值
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/kvStore"
            ),
            params=dict(namespace=namespace, key=key, json_decode=json_decode)
        )
         
    @classmethod
    async def api_taskInfo_kvStore_post(cls, body: SetKvStoreInSchema) -> AsyncHttpResponse:
        """
        设置 Key-Value 存储
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/kvStore"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def api_taskInfo_kvStore_delete_post(cls, body: DeleteKvStore) -> AsyncHttpResponse:
        """
        删除 Key-Value 存储
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/kvStore/delete"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def api_taskInfo_kvStore_list_get(cls, namespace: str, key: str) -> AsyncHttpResponse:
        """
        获取 Key-Value List 存储值
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/kvStore/list"
            ),
            params=dict(namespace=namespace, key=key)
        )
         
    @classmethod
    async def api_taskInfo_kvStore_list_post(cls, body: SetKvStoreListInSchema) -> AsyncHttpResponse:
        """
        设置 Key-Value List 存储 (添加/移除/清空值)
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/kvStore/list"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def listFind(cls, namespace: str, key: str, value: str) -> AsyncHttpResponse:
        """
        查找 Key-Value List 一个值是否存在
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/kvStore/listFind"
            ),
            params=dict(namespace=namespace, key=key, value=value)
        )
         
    @classmethod
    async def process(cls, job_type: str) -> AsyncHttpResponse:
        """
        获取模板
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/process"
            ),
            params=dict(job_type=job_type)
        )
         
    @classmethod
    async def api_taskInfo_process_post(cls, body: SetBusProcessInSchema) -> AsyncHttpResponse:
        """
        设置模板
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/process"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def api_taskInfo_containerInfo_get(cls, vehicle_id: str) -> AsyncHttpResponse:
        """
        获取箱子信息
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/containerInfo"
            ),
            params=dict(vehicle_id=vehicle_id)
        )
         
    @classmethod
    async def api_taskInfo_containerInfo_post(cls, body: SetContainerInfoInSchema) -> AsyncHttpResponse:
        """
        修改箱子信息
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/containerInfo"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def create(cls, body: object) -> AsyncHttpResponse:
        """
        创建Job
        创建 Job
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/vehicleJob/create"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def api_taskInfo_vehicleJob_status_post(cls, vehicle_id: str, job_status: int, job_id: str, origin: str) -> AsyncHttpResponse:
        """
        更新任务状态
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/vehicleJob/status"
            ),
            
            params=dict(vehicle_id=vehicle_id, job_status=job_status, job_id=job_id, origin=origin)
        )
         
    @classmethod
    async def stage(cls, vehicle_id: str, job_id: str, job_stage: str) -> AsyncHttpResponse:
        """
        更新任务进度
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/vehicleJob/stage"
            ),
            
            params=dict(vehicle_id=vehicle_id, job_id=job_id, job_stage=job_stage)
        )
         
    @classmethod
    async def businessKey(cls, vehicle_id: str) -> AsyncHttpResponse:
        """
        获取正在执行的业务Id
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/vehicleJob/businessKey"
            ),
            params=dict(vehicle_id=vehicle_id)
        )
         
    @classmethod
    async def api_taskInfo_vehicleJob_get(cls, vehicle_id: str) -> AsyncHttpResponse:
        """
        获取车辆的当前任务
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/vehicleJob"
            ),
            params=dict(vehicle_id=vehicle_id)
        )
         
    @classmethod
    async def get(cls, job_id: str) -> AsyncHttpResponse:
        """
        使用 Job Id 获取 Job (Raw)
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/vehicleJob/get"
            ),
            params=dict(job_id=job_id)
        )
         
    @classmethod
    async def getStd(cls, job_id: str) -> AsyncHttpResponse:
        """
        使用 Job Id 获取 Job (Std)
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/vehicleJob/getStd"
            ),
            params=dict(job_id=job_id)
        )
         
    @classmethod
    async def getByMission(cls, mission_id: str) -> AsyncHttpResponse:
        """
        使用 Mission 获取 Job
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/vehicleJob/getByMission"
            ),
            params=dict(mission_id=mission_id)
        )
         
    @classmethod
    async def api_taskInfo_vehicleJob_abort_post(cls, vehicle_id: str, origin: str, cancel_reason: str) -> AsyncHttpResponse:
        """
        中止任务
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/vehicleJob/abort"
            ),
            
            params=dict(vehicle_id=vehicle_id, origin=origin, cancel_reason=cancel_reason)
        )
         
    @classmethod
    async def updateJobDest(cls, body: UpdateJobDest) -> AsyncHttpResponse:
        """
        更新任务目的位置
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/vehicleJob/updateJobDest"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def updatePlanContainers(cls, body: UpdatePlanContainers) -> AsyncHttpResponse:
        """
        更新任务计划箱子
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/vehicleJob/updatePlanContainers"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def complete(cls, vehicle_id: str, job_status: int) -> AsyncHttpResponse:
        """
        正常结束任务
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/vehicleJob/complete"
            ),
            
            params=dict(vehicle_id=vehicle_id, job_status=job_status)
        )
         
    @classmethod
    async def jobMission(cls, job_id: str, mission_id: str) -> AsyncHttpResponse:
        """
        获取 Job Mission
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/vehicleJob/jobMission"
            ),
            params=dict(job_id=job_id, mission_id=mission_id)
        )
         
    @classmethod
    async def api_taskInfo_vehicleJob_jobMission_post(cls, job_id: str, mission_id: str) -> AsyncHttpResponse:
        """
        绑定 Job Mission
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/vehicleJob/jobMission"
            ),
            
            params=dict(job_id=job_id, mission_id=mission_id)
        )
         
    @classmethod
    async def stageTag(cls, vehicle_id: str, job_id: str, job_stage_tag: str) -> AsyncHttpResponse:
        """
        更新任务进度标签
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/vehicleJob/stageTag"
            ),
            
            params=dict(vehicle_id=vehicle_id, job_id=job_id, job_stage_tag=job_stage_tag)
        )
         
    @classmethod
    async def api_taskInfo_vehicleJob_resendJob_post(cls, body: ResendJobPost) -> AsyncHttpResponse:
        """
        重新派发旧任务
        允许 business_keys 或者 resend_jobs 两种形式的请求
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/vehicleJob/resendJob"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def api_taskInfo_vehicleJob_delete_post(cls, body: DeleteJobPost) -> AsyncHttpResponse:
        """
        删除任务
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/vehicleJob/delete"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def api_taskInfo_vehicleJob_query_post(cls, body: QueryJobPost) -> AsyncHttpResponse:
        """
        任务查询
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/vehicleJob/query"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def newest(cls, vehicle_id: str) -> AsyncHttpResponse:
        """
        获取车辆最后执行的任务
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/vehicleJob/newest"
            ),
            params=dict(vehicle_id=vehicle_id)
        )
         
    @classmethod
    async def all_newest_job(cls, ) -> AsyncHttpResponse:
        """
        获取所有车辆最后执行的任务
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/vehicleJob/all_newest_job"
            ),
            
        )
         
    @classmethod
    async def api_taskInfo_vehicleJob_all_current_job_get(cls, ) -> AsyncHttpResponse:
        """
        获取所有当前正在执行的任务
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/vehicleJob/all_current_job"
            ),
            
        )
         
    @classmethod
    async def api_taskInfo_vehicleJob_query_all_post(cls, body: QueryJobAllPost) -> AsyncHttpResponse:
        """
        历史任务查询
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/vehicleJob/query_all"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def all_newest_job_filter(cls, origin: str) -> AsyncHttpResponse:
        """
        查询每个车最新的任务（带过滤器）
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/vehicleJob/all_newest_job_filter"
            ),
            params=dict(origin=origin)
        )
         
    @classmethod
    async def virtual_points(cls, ) -> AsyncHttpResponse:
        """
        获取Virtual任务类型的点位
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/vehicleJob/virtual_points"
            ),
            
        )
         
    @classmethod
    async def api_taskInfo_vehicleJob_virtual_points_post(cls, body: VirtualPointsPost) -> AsyncHttpResponse:
        """
        存储Virtual任务类型的点位
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/vehicleJob/virtual_points"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def workflowConfig(cls, config_item: str) -> AsyncHttpResponse:
        """
        获取工作流配置项
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/workflowConfig"
            ),
            params=dict(config_item=config_item)
        )
         
    @classmethod
    async def api_taskInfo_workflowConfig_post(cls, config_item: str, value: str) -> AsyncHttpResponse:
        """
        设置工作流配置项
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/workflowConfig"
            ),
            
            params=dict(config_item=config_item, value=value)
        )
         
    @classmethod
    async def api_taskInfo_lockArea_get(cls, type: str, tag: str) -> AsyncHttpResponse:
        """
        获取锁闭区
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/lockArea"
            ),
            params=dict(type=type, tag=tag)
        )
         
    @classmethod
    async def api_taskInfo_lockArea_post(cls, body: object) -> AsyncHttpResponse:
        """
        创建锁闭区
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/lockArea"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def api_taskInfo_lockArea_delete_post(cls, body: object) -> AsyncHttpResponse:
        """
        删除锁闭区
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/lockArea/delete"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def api_taskInfo_lockArea_deleteByTag_post(cls, body: object) -> AsyncHttpResponse:
        """
        删除锁闭区(指定 Tag)
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/lockArea/deleteByTag"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def api_taskInfo_lockArea_change_post(cls, body: object) -> AsyncHttpResponse:
        """
        修改锁闭区
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/lockArea/change"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def changeByTag(cls, body: object) -> AsyncHttpResponse:
        """
        通过标签修改锁闭区
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/lockArea/changeByTag"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def api_taskInfo_VesselInfo_SetVesselInfo_post(cls, body: SetVesselInfoSchemas) -> AsyncHttpResponse:
        """
        创建船舶
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/VesselInfo/SetVesselInfo"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def api_taskInfo_VesselInfo_EditVesselInfo_post(cls, body: object) -> AsyncHttpResponse:
        """
        修改船
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/VesselInfo/EditVesselInfo"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def GetVesselInfo(cls, vesselVisitId: str) -> AsyncHttpResponse:
        """
        获取船信息
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/VesselInfo/GetVesselInfo"
            ),
            params=dict(vesselVisitId=vesselVisitId)
        )
         
    @classmethod
    async def DeleteVesselInfo(cls, body: DelVesselInfoSchemas) -> AsyncHttpResponse:
        """
        删除船信息
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/VesselInfo/DeleteVesselInfo"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def api_taskInfo_VesselInfo_SetVesselInfoStatus_post(cls, body: SetVesselInfoStatusSchemas) -> AsyncHttpResponse:
        """
        设置自动建船开关
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/VesselInfo/SetVesselInfoStatus"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def AlarmMessageStart(cls, body: SetAlarmMessage) -> AsyncHttpResponse:
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
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/Message/AlarmMessageStart"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def AlarmMessageStart_bak(cls, body: SetAlarmMessage) -> AsyncHttpResponse:
        """
        单车上报告警信息开始
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/Message/AlarmMessageStart_bak"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def AlarmMessageStop(cls, body: StopAlarmMessage) -> AsyncHttpResponse:
        """
        单车上报告警信息结束
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/Message/AlarmMessageStop"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def GetAlarmMessage(cls, body: AlarmMessageSchema) -> AsyncHttpResponse:
        """
        获取单车告警信息
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/Message/GetAlarmMessage"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def SetFmsMessage(cls, body: SetFMSMessage) -> AsyncHttpResponse:
        """
        Fms告警信息
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/Message/SetFmsMessage"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def GetFmsMessage(cls, body: AlarmMessageSchema) -> AsyncHttpResponse:
        """
        获取Fms告警信息
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/Message/GetFmsMessage"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def set(cls, body: object) -> AsyncHttpResponse:
        """
        设置子任务
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/subTask/set"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def api_taskInfo_subTask_get_get(cls, vin: str) -> AsyncHttpResponse:
        """
        获取子任务
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/subTask/get"
            ),
            params=dict(vin=vin)
        )
         
    @classmethod
    async def api_taskInfo_subTask_clear_post(cls, vin: str) -> AsyncHttpResponse:
        """
        删除子任务
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/subTask/clear"
            ),
            
            params=dict(vin=vin)
        )
         
    @classmethod
    async def fenceEvent(cls, body: CreateFence) -> AsyncHttpResponse:
        """
        上报围栏事件
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/fenceEvent"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def finish(cls, body: FinishFenceEvent) -> AsyncHttpResponse:
        """
        标记围栏事件完成
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/fenceEvent/finish"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def api_taskInfo_fenceEvent_get_post(cls, device_id: str, passing_location: str, passing_event: str, start_time: str, end_time: str) -> AsyncHttpResponse:
        """
        获取围栏事件
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/fenceEvent/get"
            ),
            
            params=dict(device_id=device_id, passing_location=passing_location, passing_event=passing_event, start_time=start_time, end_time=end_time)
        )
         
    @classmethod
    async def api_taskInfo_taskPool_get_post(cls, body: object) -> AsyncHttpResponse:
        """
        Get Task Pool
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/taskPool/get"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def add(cls, body: object) -> AsyncHttpResponse:
        """
        Add Task Pool
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/taskPool/add"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def update(cls, body: object) -> AsyncHttpResponse:
        """
        Update Task Pool
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/taskPool/update"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def api_taskInfo_taskPool_abort_post(cls, body: object) -> AsyncHttpResponse:
        """
        Abort Task Pool
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/taskPool/abort"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def api_taskInfo_taskPool_runImmediate_post(cls, body: object) -> AsyncHttpResponse:
        """
        Runimmediate
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/taskPool/runImmediate"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def api_taskInfo_taskPool_delete_post(cls, body: object) -> AsyncHttpResponse:
        """
        Delete Task Pool
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/taskPool/delete"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def TsRelated(cls, body: object) -> AsyncHttpResponse:
        """
        创建锁站
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/TsRelated"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def api_taskInfo_TsRelated_delete_post(cls, body: object) -> AsyncHttpResponse:
        """
        删除锁站
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/TsRelated/delete"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def Edit(cls, body: object) -> AsyncHttpResponse:
        """
        修改Ts
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/TsRelated/Edit"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def Get(cls, body: GetTsSchemas) -> AsyncHttpResponse:
        """
        获取Ts
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/TsRelated/Get"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def api_taskInfo_EquipmentStatus_post(cls, body: object) -> AsyncHttpResponse:
        """
        设置Cms,Cps状态
        {
    "switch_val_name":"cms",
    "switch_val":"off"
}
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/EquipmentStatus"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def api_taskInfo_EquipmentStatus_Get_get(cls, ) -> AsyncHttpResponse:
        """
        获取Cms,Cps状态
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/EquipmentStatus/Get"
            ),
            
        )
         
    @classmethod
    async def api_taskInfo_EquipmentStatus_SpreaderSize_post(cls, body: object) -> AsyncHttpResponse:
        """
        设置吊具尺寸
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/EquipmentStatus/SpreaderSize"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def GetSpreaderSize(cls, switch_val_name: str) -> AsyncHttpResponse:
        """
        获取吊具尺寸
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/EquipmentStatus/GetSpreaderSize"
            ),
            params=dict(switch_val_name=switch_val_name)
        )
         
    @classmethod
    async def api_taskInfo_PaceGlobal_post(cls, body: object) -> AsyncHttpResponse:
        """
        配置全局速度
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/PaceGlobal"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def api_taskInfo_quayCrane_SetLane_post(cls, body: SetLaneInSchema) -> AsyncHttpResponse:
        """
        设置岸桥作业车道
        {
    "namespace": "guiServer:craneWorkLane",  # "tosInterface:craneWorkLane",
    "key": "Z1",
    "value": "02"
}
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/quayCrane/SetLane"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def GetLane(cls, ) -> AsyncHttpResponse:
        """
        获取设置的岸桥作业车道
        {
    "namespace": "guiServer:craneWorkLane",
    "key": "Z1",
    "value": "02"
}
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/quayCrane/GetLane"
            ),
            
        )
         
    @classmethod
    async def preArrive(cls, body: PreArriveInSchema) -> AsyncHttpResponse:
        """
        上报预到达
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/preArrive"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def ts_switch(cls, ts_type: str, ts_name: str) -> AsyncHttpResponse:
        """
        查询锁站
        
        """
        
        return await async_get(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/ts_switch"
            ),
            params=dict(ts_type=ts_type, ts_name=ts_name)
        )
         
    @classmethod
    async def api_taskInfo_ts_switch_post(cls, body: LockSwitchInSchema) -> AsyncHttpResponse:
        """
        设置更新锁站开关
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/ts_switch"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def sim_start_job(cls, body: object) -> AsyncHttpResponse:
        """
        上报预到达
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/simApi/sim_start_job"
            ),
            json=body.dict(),
            
        )
         
    @classmethod
    async def fullControl(cls, body: FullStopStatus) -> AsyncHttpResponse:
        """
        全场紧停或者恢复
        
        """
        
        return await async_post(
            url=parse.urljoin(
                cls.url, "/api/taskInfo/fullControl"
            ),
            json=body.dict(),
            
        )
         