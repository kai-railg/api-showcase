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
from ..schemas.crane_info import *

__all__ = ["CraneInfoRequest"]


class CraneInfoRequestCls(ApiRequestBaseCls):
    def __init__(self):
        super(CraneInfoRequestCls, self).__init__()
        self.SERVICE_PORT = 8014
        self.SERVICE_NAME = "crane_info"
        self.module_mapping[self.SERVICE_NAME] = self

    async def asc_cps_info_report(
        self, body: CPSInfoRequestModel
    ) -> Tuple[int, CPSInfoResponseModel]:
        """
        Asc Cps Info Report
        CPS数据
        """
        return await self.request(
            request=async_post,
            api="/api/asc_cps_info_report",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CPSInfoResponseModel,
        )

    def asc_cps_info_report_sync(
        self, body: CPSInfoRequestModel
    ) -> Tuple[int, CPSInfoResponseModel]:
        """
        Asc Cps Info Report
        CPS数据
        """
        return self.request_sync(
            request=requests.post,
            api="/api/asc_cps_info_report",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CPSInfoResponseModel,
        )

    async def plc(self, body: PlcDataRequestModel) -> Tuple[int, CommonResponseModel]:
        """
        Plc
        接收TE发过来的opcua数据
        """
        return await self.request(
            request=async_post,
            api="/api/plc",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CommonResponseModel,
        )

    def plc_sync(self, body: PlcDataRequestModel) -> Tuple[int, CommonResponseModel]:
        """
        Plc
        接收TE发过来的opcua数据
        """
        return self.request_sync(
            request=requests.post,
            api="/api/plc",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CommonResponseModel,
        )

    async def application_lane_handler(
        self, body: ApplicationLaneRequestModel
    ) -> Tuple[int, CommonResponseModel]:
        """ """
        return await self.request(
            request=async_post,
            api="/api/application_lane_handler",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CommonResponseModel,
        )

    def application_lane_handler_sync(
        self, body: ApplicationLaneRequestModel
    ) -> Tuple[int, CommonResponseModel]:
        """ """
        return self.request_sync(
            request=requests.post,
            api="/api/application_lane_handler",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CommonResponseModel,
        )

    async def qc_holding_info(
        self, body: QCPointRequestModel
    ) -> Tuple[int, CommonResponseModel]:
        """

                选择qc holding point 等待区
        :return:
        """
        return await self.request(
            request=async_post,
            api="/api/qc_holding_info",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CommonResponseModel,
        )

    def qc_holding_info_sync(
        self, body: QCPointRequestModel
    ) -> Tuple[int, CommonResponseModel]:
        """

                选择qc holding point 等待区
        :return:
        """
        return self.request_sync(
            request=requests.post,
            api="/api/qc_holding_info",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CommonResponseModel,
        )

    async def query_container_point(
        self, body: ContainerPointRequestModel
    ) -> Tuple[int, CommonResponseModel]:
        """

                为inventory提供卸船箱子点位
        :return:
        """
        return await self.request(
            request=async_post,
            api="/api/query_container_point",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CommonResponseModel,
        )

    def query_container_point_sync(
        self, body: ContainerPointRequestModel
    ) -> Tuple[int, CommonResponseModel]:
        """

                为inventory提供卸船箱子点位
        :return:
        """
        return self.request_sync(
            request=requests.post,
            api="/api/query_container_point",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CommonResponseModel,
        )

    async def qc_position(
        self, body: UpdateQCPositionModel
    ) -> Tuple[int, CommonResponseModel]:
        """

                更新qc x
        :return:
        """
        return await self.request(
            request=async_post,
            api="/api/qc_position",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CommonResponseModel,
        )

    def qc_position_sync(
        self, body: UpdateQCPositionModel
    ) -> Tuple[int, CommonResponseModel]:
        """

                更新qc x
        :return:
        """
        return self.request_sync(
            request=requests.post,
            api="/api/qc_position",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CommonResponseModel,
        )

    async def qc_signal(
        self, body: QCSignalRequestModel
    ) -> Tuple[int, CommonResponseModel]:
        """

                创建或释放qc锁闭区
        :return:
        """
        return await self.request(
            request=async_post,
            api="/api/qc_signal",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CommonResponseModel,
        )

    def qc_signal_sync(
        self, body: QCSignalRequestModel
    ) -> Tuple[int, CommonResponseModel]:
        """

                创建或释放qc锁闭区
        :return:
        """
        return self.request_sync(
            request=requests.post,
            api="/api/qc_signal",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CommonResponseModel,
        )

    async def qc_holding_status(
        self, body: QCHoldingRequestModel
    ) -> Tuple[int, CommonResponseModel]:
        """

                {
          "messageName": "QC",
          "messageUniqueID": "",
          "messageTimestamp":"",
          "deviceId": 1,
          "lane": 1
        }
        """
        return await self.request(
            request=async_post,
            api="/api/qc_holding_status",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CommonResponseModel,
        )

    def qc_holding_status_sync(
        self, body: QCHoldingRequestModel
    ) -> Tuple[int, CommonResponseModel]:
        """

                {
          "messageName": "QC",
          "messageUniqueID": "",
          "messageTimestamp":"",
          "deviceId": 1,
          "lane": 1
        }
        """
        return self.request_sync(
            request=requests.post,
            api="/api/qc_holding_status",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CommonResponseModel,
        )

    async def api_response_mixed_area_post(
        self, body: MixedAreaRequestModel
    ) -> Tuple[int, CommonResponseModel]:
        """

                {"messageNumber":8,
        "value":True
        }
        airlock，跨运车在里面申请开门num 8,ceg:atuo 门发10， 手动门发9
        """
        return await self.request(
            request=async_post,
            api="/api/response_mixed_area",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CommonResponseModel,
        )

    def api_response_mixed_area_post_sync(
        self, body: MixedAreaRequestModel
    ) -> Tuple[int, CommonResponseModel]:
        """

                {"messageNumber":8,
        "value":True
        }
        airlock，跨运车在里面申请开门num 8,ceg:atuo 门发10， 手动门发9
        """
        return self.request_sync(
            request=requests.post,
            api="/api/response_mixed_area",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CommonResponseModel,
        )

    async def api_engine_post(
        self, body: EngineRequestModel
    ) -> Tuple[int, CommonResponseModel]:
        """

                {
        "sc":"SC01",
        "value":True,
        "node":engine
        }
        """
        return await self.request(
            request=async_post,
            api="/api/engine",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CommonResponseModel,
        )

    def api_engine_post_sync(
        self, body: EngineRequestModel
    ) -> Tuple[int, CommonResponseModel]:
        """

                {
        "sc":"SC01",
        "value":True,
        "node":engine
        }
        """
        return self.request_sync(
            request=requests.post,
            api="/api/engine",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CommonResponseModel,
        )

    async def update_plc_data(
        self, body: UpdatePlcDataModel
    ) -> Tuple[int, CommonResponseModel]:
        """ """
        return await self.request(
            request=async_post,
            api="/api/update_plc_data",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CommonResponseModel,
        )

    def update_plc_data_sync(
        self, body: UpdatePlcDataModel
    ) -> Tuple[int, CommonResponseModel]:
        """ """
        return self.request_sync(
            request=requests.post,
            api="/api/update_plc_data",
            body={
                "data": body.model_dump_json(),
            },
            resp_model=CommonResponseModel,
        )


CraneInfoRequest = CraneInfoRequestCls()
