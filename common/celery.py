import os
from celery import Celery


celery = Celery("spacer", broker="amqp://localhost:5672", include=["controllers.tasks"])
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "amqp://localhost:5672")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")


