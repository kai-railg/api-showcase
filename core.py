# -*- coding: utf-8 -*-
"""
@Version ： python3.9
@Time    ： 2024/3/1 10:29 AM
@Author  ： kai.wang
@Email   :  kai.wang@westwell-lab.com
"""
import re
import collections
import json
import os
import subprocess
from enum import Enum
from typing import Dict, List
from settings import remote_ip, pip_dir

import requests


def get_openapi_json(config: Dict) -> Dict:
    """

    :param config:
    :return:
    """
    try:
        url = f"http://{config.get('ip', remote_ip)}:{config['port']}/{config.get('openapi_url', 'openapi.json')}"
        return requests.get(url).json()
    except Exception as e:
        print(f"{config['name']} get openapi json error...... ")
    return {}


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


def generate_protobuf_py(name: str):
    # python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. src/chain_api_showcase/protobuf/inventory/inventory.proto
    os.chdir(f"src/chain_api_showcase/protobuf/{name}/")
    command: List = [
        # "cd",
        # "src/chain_api_showcase/protobuf"
        # "&&",
        "python",
        "-m",
        "grpc_tools.protoc",
        "-I.",
        "--python_out=.",
        "--grpc_python_out=.",
        f"{name}.proto",
    ]
    resp = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(resp.stderr, resp.stdout)
    os.chdir("../../../../")


def insert_lines_to_pb2(filepath, line_number, text):
    # 打开文件并读取所有行
    with open(filepath, 'r') as file:
        lines = file.readlines()

    # 确保line_number在文件的行数范围内
    if line_number < 1 or line_number > len(lines) + 1:
        print(f"Error: line_number {line_number} is out of range.")
        return

    # 插入文本到指定行号前
    lines.insert(line_number - 1, text + '\n')

    # 将更改后的内容写回文件
    with open(filepath, 'w') as file:
        file.writelines(lines)


def update_grpc_pb2_import_path(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # 将导入语句替换为相对导入
    content = re.sub(r'import (.*_pb2) as', r'from . import \1 as', content)

    with open(file_path, 'w') as file:
        file.write(content)


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

    for pm in data and data["paths"].items():
        path, methods = pm
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

    name = project_config["name"]
    # 设置模板环境
    env = Environment(loader=FileSystemLoader(searchpath='.'))

    # 加载模板文件
    template = env.get_template("./template/api_service_template.j2")

    result = get_api_endpoints(project_config)

    with open(f"./{pip_dir}/api/{name}.py", "w") as f:
        f.write(template.render(**result))

    # 写入 api_base.py
    with open(f"./{pip_dir}/api/api_base.py", "w") as f:
        f.write(env.get_template("./template/api_base_template.j2").render())

    template = env.get_template("./template/proto.j2")
    grpc_result = generate_proto(name, result["endpoints"])
    grpc_dir = f"./{pip_dir}/protobuf/{name}"
    if not os.path.exists(grpc_dir):
        os.makedirs(grpc_dir, exist_ok=True)

    with open(f"{grpc_dir}/{name}.proto", "w") as f:
        f.write(template.render(**grpc_result))

    generate_protobuf_py(name)

    insert_lines_to_pb2(
        f"{grpc_dir}/{name}_pb2.py",
        17,
        "\n".join([f"{model} = None" for model in set([func["model"] for func in grpc_result["functions"]])] + ["Response = None"])
    )

    update_grpc_pb2_import_path(f"{grpc_dir}/{name}_pb2_grpc.py")


def format_file(project_name: str):
    command: List = [
        "black",
        f"./{pip_dir}/api/{project_name}.py"
    ]
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


def match_type(s: str, enums: List):
    if s.startswith("Optional"):
        s = s[len("Optional") + 1:-1]
        return match_type(s, enums)
    if s.startswith("Union"):
        s = s[len("Union") + 1:-1]
        return match_type(s, enums)
    if s.startswith("Dict["):
        return "map<string, google.protobuf.Any>"
    elif s.startswith("List["):
        s = "repeated " + match_type(s[len('List['):-1], enums)
        if s.startswith("repeated map"):
            return s[len("repeated "):]
        elif s.startswith("repeated repeated"):
            return s[len("repeated "):]
        return s
    elif s in enums:
        return "string"
    elif "," in s:
        if "float" in s:
            return "float"
        elif "int" in s:
            return "sint32"
        elif "str" in s:
            return "string"
        return s.split(",")[0]
    elif "List" == s:
        return "repeated google.protobuf.Any"
    elif "datetime" == s:
        return "string"
    elif "float" == s:
        return "float"
    elif "int" == s:
        return "sint32"
    elif "bool" == s:
        return "bool"
    elif "str" == s:
        return "string"
    elif "Any" == s:
        return "google.protobuf.Any"
    else:
        return s


def generate_proto(project_name: str, endpoints: List):
    import importlib
    from pydantic import BaseModel
    module = importlib.import_module(f"src.chain_api_showcase.schemas.{project_name}")
    # print(module.__dict__)
    # 筛选出所有 BaseModel 的子类
    base_model_subclasses = []
    # Enum 类列表
    enums = []
    for attribute_name in dir(module):
        attribute = getattr(module, attribute_name)
        if isinstance(attribute, type) and issubclass(attribute, BaseModel) and attribute is not BaseModel:
            base_model_subclasses.append(attribute)
        if isinstance(attribute, type) and issubclass(attribute, Enum):
            enums.append(attribute.__name__)

    result = {
        "module_name": project_name.title(),
        "service_name": project_name.title(),
        "functions": [
            {
                "name": e["func_name"],
                "model": e["model"] if e["model"] and e["model"] != "object" else "Request"
            } for e in endpoints
        ],
        "requests": []

    }

    # 输出找到的 BaseModel 子类列表
    for cls in base_model_subclasses:
        # print(cls.__name__)
        cls = getattr(module, cls.__name__)

        # 打印字段名称和类型
        request_kvs = {
            "name": cls.__name__,
            "params": []
        }
        index = 1
        for field_name, field_type in cls.__annotations__.items():
            # print(f"{field_name},  {field_type}")
            request_kvs["params"].append(
                {
                    "type": match_type(field_type, enums),
                    "name": field_name,
                    "index": index,
                }
            )
            index += 1
        result["requests"].append(request_kvs)
    return result


if __name__ == '__main__':
    for i in [
        "camunda",
        "crane_info",
        "device_info",
        "gui_server",
        "integrator",
        "pp",
        "route_interface",
        "task_executor",
        "task_info",
        "task_scheduler",
        "tos_interface",
        "vehicle_manager",
    ]:
        generate_proto(i, [])
