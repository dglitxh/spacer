from common.celery import celery
from fastapi_mail import FastMail, MessageSchema,ConnectionConfig


@celery.task
def hello():
    return "Ydeezzy"

@celery.task
async def send_mail(template: str, email: str):
    try:
        message = MessageSchema(
            subject="Fastapi-Mail module",
            recipients=email,
            body=template,
            subtype="html"
            )
        fm = FastMail(mailer_config)
        await fm.send_message(message)
        print(message)
        return "email sent."
    except Exception as e:
        print(e)
 