# -*- coding: utf-8 -*-
"""
@Version ： python3.9
@Time    ： 2024/3/1 10:23 AM
@Author  ： kai.wang
@Email   :  kai.wang@westwell-lab.com
"""
import os.path

from settings import projects, pip_dir

from core import (
    get_openapi_json,
    write_openapi_json,
    generate_pydantic_model,
    generate_api_code
)

if __name__ == '__main__':
    if not os.path.exists(f"./{pip_dir}"):
        os.mkdir(f"./{pip_dir}")

    for project_config in projects:
        name: str = project_config["name"]
        openapi_json = get_openapi_json(project_config)
        write_openapi_json(openapi_json, name)
        generate_pydantic_model(name)
        generate_api_code(project_config)
        print(f"generate {name} success...")
