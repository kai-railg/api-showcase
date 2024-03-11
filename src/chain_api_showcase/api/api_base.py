# -*- coding: utf-8 -*-
import asyncio
import os
from typing import Dict
from urllib import parse
import requests

from chain_nacos.service_manager import ServiceManager


class ApiRequestBaseCls(object):
    module_mapping: Dict[str, 'ApiRequestBaseCls'] = {}

    def __init__(self):
        self.USE_NACOS = os.environ.get('USE_NACOS', False)
        self.NACOS_SERVER = os.environ.get('NACOS_SERVER', '127.0.0.1')
        self.NACOS_PORT = os.environ.get('NACOS_PORT', '8848')
        self.FMS_HOST = os.environ.get('FMS_HOST', '127.0.0.1')
        self.SERVICE_PORT: int = 0
        self.SERVICE_NAME: str = ""
        self.protocol: str = "http"
        self.timeout: int = os.environ.get('timeout', 6)
        self._nacos = None
        self.max_retry_count = 3

    @property
    def nacos(self):
        if not self._nacos:
            self._nacos = ServiceManager(self.nacos_address)
        return self._nacos

    @property
    def nacos_address(self):
        return f"{self.protocol}://{self.NACOS_SERVER}:{self.NACOS_PORT}"

    @property
    def url(self) -> str:
        if not self.USE_NACOS:
            return f"{self.protocol}://{self.FMS_HOST}:{self.SERVICE_PORT}"

        ins = self.nacos.get_random_instance(self.SERVICE_NAME)
        host, port = ins["ip"], ins["port"]
        return f"{self.protocol}://{host}:{port}"

    def get_url_from_module_name(self, module_name: str) -> str:
        obj = self.module_mapping.get(module_name)
        return obj and obj.url

    def request_sync(self, request, api, body: Dict, resp_model=None, max_retry_count=1) -> Dict:
        url = parse.urljoin(self.url, api)
        try:
            resp = request(
                {
                    **body,
                    **{
                        "url": url,
                        "timeout": self.timeout,
                    },
                }
            )
            if resp.status != 200:
                print(
                    f"Request failed: {resp.status}, url:  {url}, response: {resp.text}"
                )
                return resp.status, resp.text
            return resp.status, resp.json() if resp_model is None else resp_model.model_validate(resp.json())

        except requests.Timeout as e:
            if max_retry_count >= self.max_retry_count:
                print(f"The request failed because the number of requests exceeded the maximum {self.max_retry_count}. {url}")
                return 400, str(e)
            return self.request_sync(request, api, body, resp_model, max_retry_count + 1)

        except Exception as e:
            print(f"Request failed: {e}, url: {url}")
            return 400, str(e)

    async def request(self, request, api, body: Dict, resp_model=None, max_retry_count=1) -> Dict:
        url = parse.urljoin(self.url, api)
        try:
            resp = await request(
                {
                    **body,
                    **{
                        "url": url,
                        "timeout": self.timeout,
                    },
                }
            )
            if resp.status != 200:
                print(
                    f"Request failed: {resp.status}, url:  {url}, response: {resp.text}"
                )
                return resp.status, resp.text
            return resp.status, resp.json() if resp_model is None else resp_model.model_validate(resp.json())

        except asyncio.TimeoutError as e:
            if max_retry_count >= self.max_retry_count:
                print(f"The request failed because the number of requests exceeded the maximum {self.max_retry_count}. {url}")
                return 400, str(e)
            return await self.request(request, api, body, resp_model, max_retry_count + 1)

        except Exception as e:
            print(f"Request failed: {e}, url: {url}")
            return 400, str(e)
