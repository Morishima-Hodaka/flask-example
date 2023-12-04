import os
from dotenv import load_dotenv

"""
python-dotenv 是一个 Python 包，
用于从文件中加载环境变量。它通常用于在开发环境中配置敏感信息，
例如数据库连接信息、API 密钥等，而不希望这些信息直接硬编码到源代码中。
"""

root_path = os.path.abspath(os.path.dirname(__file__)).split('app')[0]
dot_env_path = os.path.join(root_path, '.env')
flask_env_path = os.path.join(root_path, '.flaskenv')


def init_dotenv() -> None:
    # if os.path.exists(dot_env_path):
    #     load_dotenv(dot_env_path)

    if os.path.exists(flask_env_path):
        print(flask_env_path)
        print(os.environ)

        load_dotenv(flask_env_path)
