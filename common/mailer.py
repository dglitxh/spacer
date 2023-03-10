from fastapi_mail import FastMail, MessageSchema,ConnectionConfig
from dotenv import load_dotenv
import os

load_dotenv()
print(os.getenv("MAIL"))
conf = ConnectionConfig(
   MAIL_USERNAME=os.getenv("MAIL"),
   MAIL_PASSWORD=os.getenv("MAILPASS"),
   MAIL_FROM="daboii@m.com",
   MAIL_PORT=587,
   MAIL_SERVER="smtp.gmail.com",
   MAIL_STARTTLS=True,
   MAIL_SSL_TLS=False
)

async def send_mail(template: str, email: str):
    try:
        message = MessageSchema(
            subject="Fastapi-Mail module",
            recipients=email,
            body=template,
            subtype="html"
            )
        fm = FastMail(conf)
        await fm.send_message(message)
        print(message)
    except Exception as e:
        print(e)
 