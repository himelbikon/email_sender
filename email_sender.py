import os
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib

load_dotenv()


def send_mail(user, receiver, subject, message, password):
    em = EmailMessage()
    em['subject'] = subject
    em.set_content(message)

    smtp = smtplib.SMTP_SSL(
        'smtp.gmail.com',
        465,
        context=ssl.create_default_context()  # SSL security
    )

    smtp.login(user, password)

    smtp.sendmail(
        from_addr=user,
        to_addrs=receiver,
        msg=em.as_string()
    )


message = 'Scraping has finished succefully. You can check it now.'


# send_mail(
#     user=os.environ.get('USER'),
#     password=os.environ.get('PASSWORD'),
#     receiver='receiver@gmail.com',
#     subject='Scraping alert 8',
#     message=message,
# )
