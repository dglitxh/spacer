import os
from celery import Celery


celery = Celery("spacer")
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "localhost:15672")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "localhost:15672")
celery.autodiscover_tasks()