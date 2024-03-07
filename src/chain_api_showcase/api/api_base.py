# -*- coding: utf-8 -*-

import os

from chain_nacos.service_manager import ServiceManager


class ApiRequestBaseCls(object):
    def __init__(self):
        self.USE_NACOS = os.environ.get('USE_NACOS', True)
        self.NACOS_SERVER = os.environ.get('NACOS_SERVER', '127.0.0.1')
        self.NACOS_PORT = os.environ.get('NACOS_PORT', '8848')
        self.FMS_HOST = os.environ.get('FMS_HOST', '127.0.0.1')
        self.SERVICE_PORT: int = 0
        self.SERVICE_NAME: str = ""
        self.protocol: str = "http"

    @property
    def nacos_address(self):
        return f"{self.protocol}://{self.NACOS_SERVER}:{self.NACOS_PORT}"

    @property
    def url(self):
        if not self.USE_NACOS:
            return f"{self.protocol}://{self.FMS_HOST}:{self.SERVICE_PORT}"

        service = ServiceManager(self.nacos_address)
        ins = service.get_random_instance(self.SERVICE_NAME)
        host, port = ins["ip"], ins["port"]
        return f"{self.protocol}://{host}:{port}"