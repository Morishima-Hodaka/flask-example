import json
from jsonschema import validate


def init_jsonschema(app):
    # 定义 JSON Schema 规则
    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "age": {"type": "integer"}
        },
        "required": ["name", "age"]
    }

    # 接收的 JSON 数据
    json_data = '{"name": "Alice", "age": 30}'

    try:
        # 尝试将接收到的 JSON 数据解析为 Python 字典
        data = json.loads(json_data)
        # 使用 jsonschema 进行验证
        validate(instance=data, schema=schema)
        print("JSON 数据验证通过！")
    except json.JSONDecodeError:
        print("无效的 JSON 数据！")
    except Exception as e:
        print("JSON 数据验证失败：{}".format(Exception))
