# coding:utf-8
# application/models/base.py
from datetime import datetime
from sqlalchemy.orm import class_mapper
from application.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash


class Base(object):
    def __init__(self):
        pass

    # object 类提供的 __repr__() 方法总是返回一个对象（类名 + obejct at + 内存地址）
    def __repr__(self):
        pass

    def to_dict(self, exclude=None):
        print("exclude:", exclude)
        """
        我们定义了一个自定义的to_dict函数，它接受一个model对象和要排除的列列表。
        函数内部使用class_mapper获取模型的列信息，然后根据排除列表构建要返回的字典。
        """
        if exclude is None:
            exclude = ['password']
        columns = [c.key for c in class_mapper(self.__class__).columns if c.key not in exclude]

        # 格式化返回的时间
        return_dict = {c: getattr(self, c) for c in columns}
        return_dict['create_time'] = return_dict['create_time'].strftime('%Y-%m-%d %H:%M:%S')
        return_dict['update_time'] = return_dict['update_time'].strftime('%Y-%m-%d %H:%M:%S')

        return return_dict

    # 写入数据库
    def from_dict(self, data):
        """
        我们定义了一个自定义的from_dict函数，它接受一个字典和要排除的列列表。
        函数内部使用class_mapper获取模型的列信息，然后根据排除列表过滤字典。


        """

        # 获取模型中存在的键
        model_keys = [c.key for c in class_mapper(self.__class__).columns]

        # 过滤出存在于模型中的键的字典
        filtered_data = {key: value for key, value in data.items() if key in model_keys}
        # 设置属性
        for key, value in filtered_data.items():
            setattr(self, key, value)

    # 更新数据库
    def update_from_dict(self, data):
        # 获取模型中存在的键
        model_keys = [c.key for c in class_mapper(self.__class__).columns]

        # 过滤出存在于模型中的键的字典
        filtered_data = {key: value for key, value in data.items() if key in model_keys}
        # 设置属性
        for key, value in filtered_data.items():
            setattr(self, key, value)

    # 删除
    def delete(self):
        db.session.delete(self)

    create_time = db.Column(db.DateTime, default=datetime.now, comment="创建时间")
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='更新时间')


class UserBase(object):

    # hash密码

    def set_password(self, password):
        self.password = generate_password_hash(password)

        # 验证

    def validate_password(self, password):
        return check_password_hash(self.password, password)
