"""
JWT（JSON Web Token）是一种用于在网络上传递信息的开放标准（RFC 7519）。
它以紧凑且自包含的方式表示信息，可以安全地在用户和服务之间传递，并可以被验证和信任。
"""
from datetime import datetime, timedelta


import jwt
from flask import jsonify




def init_jwt():
    pass


SECRET_KEY = "666666666666666666"


# 生成令牌的函数
def generate_token(phone=None):
    expiration = datetime.utcnow() + timedelta(hours=1)  # 令牌的过期时间
    token = jwt.encode({ 'exp': expiration, 'phone': phone}, SECRET_KEY,
                       algorithm='HS256')
    return token
    # return token.decode('utf-8')


# 验证令牌的装饰器
def token_required(token):
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        current_phone = data['phone']
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token has expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token'}), 401

    return current_phone
