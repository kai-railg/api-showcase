# -*- coding: utf-8 -*-

import os
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

from ..schemas.crane_info import *

FMS_IP_ADDRESS = f"http://{os.environ.get('FMS_IP_ADDRESS', '127.0.0.1')}"


class Crane_InfoRequest(object):
    url = FMS_IP_ADDRESS + ":" + "8014"

    @classmethod
    async def asc_cps_info_report(
        cls, body: CPSInfoRequestModel
    ) -> Tuple[int, CPSInfoResponseModel]:
        """
        Asc Cps Info Report
        CPS数据
        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/asc_cps_info_report"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/asc_cps_info_report, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CPSInfoResponseModel.model_validate_json(resp)

    @classmethod
    async def plc(cls, body: PlcDataRequestModel) -> Tuple[int, CommonResponseModel]:
        """
        Plc
        接收TE发过来的opcua数据
        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/plc"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/plc, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CommonResponseModel.model_validate_json(resp)

    @classmethod
    async def application_lane_handler(
        cls, body: ApplicationLaneRequestModel
    ) -> Tuple[int, CommonResponseModel]:
        """ """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/application_lane_handler"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/application_lane_handler, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CommonResponseModel.model_validate_json(resp)

    @classmethod
    async def qc_holding_info(
        cls, body: QCPointRequestModel
    ) -> Tuple[int, CommonResponseModel]:
        """

                选择qc holding point 等待区
        :return:
        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/qc_holding_info"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/qc_holding_info, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CommonResponseModel.model_validate_json(resp)

    @classmethod
    async def query_container_point(
        cls, body: ContainerPointRequestModel
    ) -> Tuple[int, CommonResponseModel]:
        """

                为inventory提供卸船箱子点位
        :return:
        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/query_container_point"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/query_container_point, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CommonResponseModel.model_validate_json(resp)

    @classmethod
    async def qc_position(
        cls, body: UpdateQCPositionModel
    ) -> Tuple[int, CommonResponseModel]:
        """

                更新qc x
        :return:
        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/qc_position"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/qc_position, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CommonResponseModel.model_validate_json(resp)

    @classmethod
    async def qc_signal(
        cls, body: QCSignalRequestModel
    ) -> Tuple[int, CommonResponseModel]:
        """

                创建或释放qc锁闭区
        :return:
        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/qc_signal"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/qc_signal, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CommonResponseModel.model_validate_json(resp)

    @classmethod
    async def qc_holding_status(
        cls, body: QCHoldingRequestModel
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
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/qc_holding_status"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/qc_holding_status, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CommonResponseModel.model_validate_json(resp)

    @classmethod
    async def api_response_mixed_area_post(
        cls, body: MixedAreaRequestModel
    ) -> Tuple[int, CommonResponseModel]:
        """

                {"messageNumber":8,
        "value":True
        }
        airlock，跨运车在里面申请开门num 8,ceg:atuo 门发10， 手动门发9
        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/response_mixed_area"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/response_mixed_area, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CommonResponseModel.model_validate_json(resp)

    @classmethod
    async def api_engine_post(
        cls, body: EngineRequestModel
    ) -> Tuple[int, CommonResponseModel]:
        """

                {
        "sc":"SC01",
        "value":True,
        "node":engine
        }
        """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/engine"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/engine, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CommonResponseModel.model_validate_json(resp)

    @classmethod
    async def update_plc_data(
        cls, body: UpdatePlcDataModel
    ) -> Tuple[int, CommonResponseModel]:
        """ """
        resp = await async_post(
            url=parse.urljoin(cls.url, "/api/update_plc_data"),
            json=body.dict(),
        )
        if resp.status != 200:
            print(
                f"Request failed: {resp.status}, url: {cls.url}, api: /api/update_plc_data, response: {resp.text}"
            )
            return resp.status, resp.text
        return resp.status, CommonResponseModel.model_validate_json(resp)
