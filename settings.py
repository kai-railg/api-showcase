# -*- coding: utf-8 -*-
"""
@Version ： python3.9
@Time    ： 2024/2/29 5:39 PM
@Author  ： kai.wang
@Email   :  kai.wang@westwell-lab.com
"""

pip_dir = "./src/chain_api_showcase"
remote_ip = "192.168.109.15"
projects = [
    {
        "name": "pp",
        "port": 18000,
    },
    {
        "name": "route_interface",
        "port": 55000,
    },
    {
        "name": "inventory",
        "port": 19102,
        "openapi_url": "openapi.json",
    },
    {
        "name": "integrator",
        "port": 10101,
        "ip": "127.0.0.1",

    },
    {
        "name": "task_executor",
        "port": 8100,
        "ip": "127.0.0.1",
    },
    {
        "name": "vehicle_manager",
        "port": 8101,
    },
    {
        "name": "gui_server",
        "port": 8020,
    },
    {
        "name": "task_info",
        "port": 10000,
    },
    {
        "name": "device_info",
        "port": 11000,
    },
    {
        "name": "crane_info",
        "port": 8014,
    },
    {
        "name": "camunda",
        "port": 8099,
        "openapi_url": "v3/api-docs",
    },
    {
        "name": "tos_interface",
        "port": 18998,
    },
    {
        "name": "task_scheduler",
        "port": 26102,
    },
]
