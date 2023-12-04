"""
Apscheduler	基于Quartz的一个Python定时任务框架，提供了基于日期、固定时间间隔以及crontab类型的任务，并且可以持久化作业	支持定时、定期、一次性任务，支持任务持久化及动态添加	配置可选项较多，配置起来较为复杂，有一定的学习成本。
Celery	是一个简单，灵活，可靠的分布式系统，用于处理大量消息，同时为操作提供维护此类系统所需的工具, 也可用于任务调度	支持配置定期任务、支持 crontab 模式配置	不支持一次性定时任务，单独为定时任务功能而搭建celery显得过于重量级。
schedule	轻量级，无需配置的作业调度库	轻量级、无需配置、语法简单	阻塞式调用、无法动态添加或删除任务，无任务状态存储
python-crontab	针对系统 Cron 操作 crontab 文件的作业调度库	支持定时、定期任务，能够动态添加任务	不能实现一次性任务需求，没有状态存储,无法跨平台执行



Celery 是一个开源的分布式任务队列系统，用于处理异步任务和定时任务。
它允许你将任务放入队列中，然后异步执行这些任务，
而不影响主应用程序的性能。Celery 主要用于处理需要在后台运行的任务，
如发送电子邮件、处理图像、执行定时任务等。

"""
from flask import Flask
from celery import Celery


def init_celery(app: Flask):
    celery_app = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
    celery_app.conf.update(app.config)  # 使用flask app的config

    @celery_app.task
    def sms_code(code, mobile, expire=5):
        print(6)

    # 自动发现任务
    celery_app.autodiscover_tasks(['tasks.sms'])
