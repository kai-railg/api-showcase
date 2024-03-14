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
from ..schemas.pp import *

__all__ = ["PpRequest"]


class PpRequestCls(ApiRequestBaseCls):
    def __init__(self):
        super(PpRequestCls, self).__init__()
        self.SERVICE_PORT = 18000
        self.SERVICE_NAME = "pp"
        self.module_mapping[self.SERVICE_NAME] = self


PpRequest = PpRequestCls()
