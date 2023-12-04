import os
from flask import Flask
from loguru import logger
import sys

"""
Loguru 是一个功能强大且易于使用的 Python 日志库。
它提供了直观的 API，使得日志记录变得简单，
同时支持一些高级功能，例如异步日志记录和自动日志文件旋转

自动日志文件旋转是指在日志文件达到一定大小或者一定时间间隔后，
系统自动创建一个新的日志文件，并将日志信息写入新文件。
这有助于限制单个日志文件的大小，防止其无限增长，同时方便对历史日志进行管理和分析。
"""

"""
Loguru 提供了以下日志级别：
TRACE：最低级别的日志级别，用于追踪程序的详细执行信息。
DEBUG：用于调试程序的日志级别，输出详细的调试信息。
INFO：用于输出程序的一般信息，表明程序正常运行。
SUCCESS：用于输出成功的信息，表示程序成功完成了某个任务。
WARNING：用于输出警告信息，表示程序遇到了一些非致命的问题。
ERROR：用于输出错误信息，表示程序遇到了一些错误，但仍然可以继续执行。
CRITICAL：最高级别的日志级别，用于输出严重错误信息，表示程序遇到了无法继续执行的严重问题。
"""


def init_loguru(app: Flask):
    LOG_PATH = app.config['LOG_PATH']

    # 添加输出到终端的处理器 屏幕
    logger.add(
        level="INFO",
        sink=sys.stdout,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {file} | {line} | {message}",
        enqueue=True

    )

    # 添加输出到文件的处理器  INFO
    logger.add(
        level="INFO",
        sink=os.path.join(LOG_PATH, "info/info.log"),
        format="{time} {level} {message}",
        enqueue=True,
        rotation="1 day",
        retention="7 days",
        compression="zip"
    )

    # 添加输出到文件的处理器  WARNING
    logger.add(
        level="WARNING",
        sink=os.path.join(LOG_PATH, "warning/warning.log"),
        format="{time} {level} {message}",
        enqueue=True,
        rotation="1 week",
        retention="30 days",
        compression="zip"
    )

    # 添加输出到文件的处理器  WARNING
    logger.add(
        level="ERROR",
        sink=os.path.join(LOG_PATH, "error/error.log"),
        format="{time} {level} {message}",
        enqueue=True,
        rotation="1 week",
        retention="30 days",
        compression="zip"
    )
    logger.warning("gunicorn 重启")

    # 在应用中使用 Loguru 记录器
    # app.logger.disabled = True
    # app.logger = logger
