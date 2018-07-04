# -*- coding:utf-8 -*-
from flask_celery import Celery
from flask_apscheduler import APScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from common.db import url

# 使用Flask-Celery-Helper 进行celery 的 flask 扩展
celery = Celery()


class Config(object):
    # SCHEDULER_JOBSTORES = {
    #     'default': RedisJobStore(host=redis_host, port=redis_port, db=1, password=redis_pwd, decode_responses=True)
    # }
    SCHEDULER_JOBSTORES = {
        # url="mysql+pymysql://root:123456@127.0.0.1/saltshaker_plus"
        'default': SQLAlchemyJobStore(url=url)
    }
    SCHEDULER_EXECUTORS = {
        'default': {'type': 'threadpool', 'max_workers': 20}
    }
    SCHEDULER_JOB_DEFAULTS = {
        'coalesce': False,
        'max_instances': 3
    }
    SCHEDULER_API_ENABLED = True


scheduler = APScheduler()
