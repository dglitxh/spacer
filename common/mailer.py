from fastapi_mail import FastMail, MessageSchema,ConnectionConfig
from dotenv import load_dotenv
import os

load_dotenv()

conf = ConnectionConfig(
   MAIL_USERNAME=os.getenv("MAIL"),
   MAIL_PASSWORD=os.getenv("MAILPASS"),
   MAIL_PORT=587,
   MAIL_SERVER="smtp.gmail.com",
   MAIL_TLS=True,
   MAIL_SSL=False
)

async def send_mail(template: str):
    try:
        message = MessageSchema(
            subject="Fastapi-Mail module",
            recipients=email.dict().get("email"),  # List of recipients, as many as you can pass
            body=template,
            subtype="html"
            )
        fm = FastMail(conf)
        await fm.send_message(message)
        print(message)
    except Exception as e:
        print(e)
 