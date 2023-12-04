# encoding:utf-8
# 提交事务 写入数据库
from flask import jsonify, g
from sqlalchemy.exc import SQLAlchemyError

from application.config import RET
from application.extensions import db



# 添加 数据库操作
def commit_affairs_add(instance, json_data):
    instance.from_dict(json_data)
    db.session.add(instance)
    db.session.commit()
    try:
        db.session.commit()
        return jsonify(msg="添加成功", errno=RET.OK)



    except SQLAlchemyError as e:
        print(e)
        db.session.rollback()
        return jsonify(msg="添加失败", errno=RET.FAIL)


# 删除 数据库操作
def commit_affairs_delete(instance):
    if instance is None:
        return jsonify(msg="删除id 不存在", RET=RET.OK)
    db.session.delete(instance)
    db.session.commit()
    try:
        db.session.commit()
        return jsonify(msg="删除成功", RET=RET.OK)



    except SQLAlchemyError as e:
        print(e)
        db.session.rollback()
        return jsonify(msg="删除败", RET=RET.FAIL)


# 查询 数据库操作
def commit_affairs_get(instance):
    if instance is None:
        return jsonify(msg="id不存在", RET=RET.OK)

    temp_list = []

    for i in instance:
        temp_list.append(i.to_dict())
    return jsonify(data=temp_list, RET=RET.OK, msg="查询成功")


# 修改 数据库操作
def commit_affairs_update(instance, data):
    if instance is None:
        return jsonify(msg="不存在", RET=RET.OK)

    instance.update_from_dict(data)
    try:
        db.session.commit()
        return jsonify(msg="更新成功", RET=RET.OK)



    except SQLAlchemyError as e:
        print(e)
        db.session.rollback()
        return jsonify(msg="更新失败", RET=RET.FAIL)


# 分页查询
def commit_affairs_get_by_paginate(query_instance):
    if query_instance is None:
        return jsonify(msg="不存在", errno=RET.FAIL)

    temp_list = []
    size=g.size
    page=g.page

    pagination = query_instance.paginate(per_page=size, page=page)

    items = pagination.items
    total_pages = pagination.pages
    total = pagination.total

    # 构造分页结果
    result = {

        'page': page,
        'size': size,
        'total_pages': total_pages,
        'total': total
    }

    for i in items:
        temp_list.append(i.to_dict())
    return jsonify(data=temp_list, errno=RET.OK, msg="查询成功", **result)


