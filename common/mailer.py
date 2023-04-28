from dotenv import load_dotenv
from fastapi_mail import ConnectionConfig
import os

load_dotenv()
print(os.getenv("MAIL"))
mailer_config = ConnectionConfig(
   MAIL_USERNAME=os.getenv("MAIL"),
   MAIL_PASSWORD=os.getenv("MAILPASS"),
   MAIL_FROM="daboii@m.com",
   MAIL_PORT=587,
   MAIL_SERVER="smtp.gmail.com",
   MAIL_STARTTLS=True,
   MAIL_SSL_TLS=False
)

