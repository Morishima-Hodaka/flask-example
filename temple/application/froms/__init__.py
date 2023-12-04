# encoding: utf-8
# froms/__init__.py
# 表单校验
from marshmallow import fields
from .user import UserIn

fields.Field.default_error_messages["required"] = "对不起，必须填写 缺少必填字段的数据"
fields.Field.default_error_messages["null"] = "字段不能为空"
fields.Field.default_error_messages["validator_failed"] = "无效值"
fields.Field.default = None


#  参数校验
def parameter_verification(json_data, checker):
    # 反序列化

    ck = checker()

    instance = ck.load(json_data)
    return instance
