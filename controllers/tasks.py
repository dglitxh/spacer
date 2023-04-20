from common.celery import celery

@celery.task
def hello():
    return "Ydeezzy"