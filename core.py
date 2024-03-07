# -*- coding: utf-8 -*-
"""
@Version ： python3.9
@Time    ： 2024/3/1 10:29 AM
@Author  ： kai.wang
@Email   :  kai.wang@westwell-lab.com
"""
import collections
import json
import subprocess
from typing import Dict, List
from settings import remote_ip, pip_dir

import requests


def get_openapi_json(config: Dict) -> Dict:
    """

    :param config:
    :return:
    """
    url = f"http://{config.get('ip', remote_ip)}:{config['port']}/{config.get('openapi_url', 'openapi.json')}"
    return requests.get(url).json()


def write_openapi_json(openapi_json: Dict, project_name: str):
    with open(f"./openapi_json/{project_name}.json", "w") as f:
        json.dump(openapi_json, f, indent=4)


def generate_pydantic_model(project_name: str):
    """

    :param project_name:
    :return:
    """
    command: List = [
        "datamodel-codegen",
        "--input",
        f"./openapi_json/{project_name}.json",
        "--output",
        f"./{pip_dir}/schemas/{project_name}.py"
    ]
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


func_name_count = collections.defaultdict(int)


def get_func_name(path: str, method: str):
    """

    :param path:
    :param method:
    :return:
    """
    func_name = None
    path_split = []
    for p in path.split("/"):
        if not p:
            continue
        if p.startswith("{"):
            continue
        if "-" in p:
            p = p.replace("-", "_")
        if "." in p:
            p = p.replace(".", "_")
        path_split.append(p)
        func_name = p
    if func_name_count[func_name] != 0:
        return "_".join(path_split + [method])
    func_name_count[func_name] += 1
    return func_name


def get_param_type(param: Dict):
    type_mapping = {
        "integer": "int",
        "string": "str",
        "null": "None",
        "number": "float",
        "boolean": "bool",
        "array": "List",
        "object": "Dict",
        "file": "File",
        "date": "datetime.date",
        "date-time": "datetime.datetime",
        "binary": "bytes",
    }

    if param["schema"].get("$ref"):
        return param["schema"]["$ref"].split("/")[-1]
    if param["schema"].get("type"):
        return type_mapping[param["schema"]["type"]]
    if param["schema"].get("anyOf"):
        type_of = param["schema"]["anyOf"]
    elif param["schema"].get("allOf"):
        type_of = param["schema"]["allOf"]
    else:
        print(param)
        return

    all_type = []
    for p in type_of:
        if p.get("type"):
            all_type.append(
                type_mapping[p["type"]]
            )
        elif p.get("$ref"):
            all_type.append(p["$ref"].split("/")[-1])
    if len(all_type) == 1:
        return all_type[0]
    return f"Union[{', '.join(all_type)}]"


def get_api_endpoints(project_config: Dict) -> Dict:
    """

    :param project_config:
    :return:
    """
    project_name = project_config["name"]
    port = project_config["port"]

    with open(f"./openapi_json/{project_name}.json", "r") as f:
        data = json.load(f)

    result = {
        "endpoints": [],
        "port": port,
        "cls_name": project_name.title().replace("_", "") + "Request",
        "project_name": project_name,
    }

    for path, methods in data["paths"].items():
        for method, vals in methods.items():
            model = None
            if vals.get("requestBody"):
                if vals["requestBody"]["content"].get("application/json"):
                    schema = vals["requestBody"]["content"]["application/json"]["schema"]
                    model = schema["$ref"].split("/")[-1] if schema.get("$ref") else "object"
                else:
                    continue
            result["endpoints"].append(
                {
                    "method": method,
                    "func_name": get_func_name(path, method),
                    "summary": vals.get("summary"),
                    "description": vals.get("description", ""),
                    "model": model,
                    "path": path,
                    "response_model": vals.get("responses").get("200", {}).get("content", {}).get("application/json", {}).get("schema", {}).get("$ref", "").split("/")[-1],
                    "parameters": [
                        {
                            "name": param["name"],
                            "model": param["schema"]["$ref"].split("/")[-1] if param.get("schema", {}).get("$ref") else None,
                            "type": get_param_type(param),
                            "default": param["schema"]["default"] if param.get("schema", {}).get("default") else None,
                            "required": param["required"]
                        }
                        for param in vals.get("parameters", [])
                    ]
                }
            )
    return result


def generate_api_code(project_config: Dict):
    """

    :param project_config:
    :return:
    """
    from jinja2 import Environment, FileSystemLoader

    # 设置模板环境
    env = Environment(loader=FileSystemLoader(searchpath='.'))

    # 加载模板文件
    template = env.get_template("./template/api_service_template.j2")

    result = get_api_endpoints(project_config)

    # 渲染模板并写入文件
    rendered_content = template.render(**result)

    with open(f"./{pip_dir}/api/{project_config['name']}.py", "w") as f:
        f.write(rendered_content)

    # 写入 api_base.py
    with open(f"./{pip_dir}/api/api_base.py", "w") as f:
        f.write(env.get_template("./template/api_base_template.j2").render())


def format_file(project_name: str):
    command: List = [
        "black",
        f"./{pip_dir}/api/{project_name}.py"
    ]
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
