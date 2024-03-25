import os
from celery import Celery
from .db import rds_url


celery = Celery(main="spacer", broker="amqp://localhost:5672", include=["controllers.tasks"])
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "amqp://localhost:5672")
celery.conf.result_backend = os.environ.get('RDS_URL', "redis://localhost:6379")


