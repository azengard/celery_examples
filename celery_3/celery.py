from __future__ import absolute_import
from celery import Celery


app = Celery('celery_3',
             broker='amqp://carlos:123@localhost/carlos_host',
             backend='rpc://',
             include=['celery_3.tasks'])