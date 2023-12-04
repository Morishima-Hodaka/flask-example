from marshmallow import Schema, fields, EXCLUDE

"""
fields: 用于指定包含在模式中的字段列表。可以是字段名称的字符串列表，或是 marshmallow.fields.Field 实例的列表。
exclude: 用于指定要排除在模式中的字段列表。可以是字段名称的字符串列表。
load_only: 用于指定只在反序列化时加载的字段列表。可以是字段名称的字符串列表。
dump_only: 用于指定只在序列化时包含的字段列表。可以是字段名称的字符串列表。
ordered: 一个布尔值，用于指定是否保持字段的顺序。默认为 False。////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
unknown: 指定如何处理未知字段。可以是 'exclude'（排除未知字段），'include'（包含未知字段）或一个 marshmallow.fields.Field 子类。
strict: 一个布尔值，用于指定是否启用严格模式。在严格模式下，当加载或转换数据时，如果遇到未知字段或验证错误，将引发 marshmallow.ValidationError。默认为 False。
其他自定义选项：你还可以在 class Meta 中定义其他自定义的选项，以满足你的特定需求。

在 Python 中，class Meta 是一个常用的约定，用于在类定义中指定元数据。它通常用于与类相关的配置和选项。

class Meta 并不是 Python 语言本身的特性，而是一种约定。
在使用 class Meta 时，你可以在类中定义一个内部类，并将其命名为 Meta。
然后在 Meta 类中定义各种选项和配置，以定制类的行为。

"""


class UserIn(Schema):
    parent_id = fields.Integer()
    username = fields.String(required=True)
    password = fields.String(required=True)

    class Meta:
        unknown = EXCLUDE
        # 指定要排除的字段
        exclude = ['id']
