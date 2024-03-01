import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import settings


def send_email(subject, plain, html):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = settings.email_from
    msg["To"] = settings.email_to

    msg.attach(MIMEText(plain, "plain"))
    msg.attach(MIMEText(html, "html"))

    try:
        with smtplib.SMTP(settings.email_server, settings.email_port) as s:
            s.ehlo()
            s.starttls()
            s.login(settings.email_username, settings.email_password)
            for recipient in settings.email_recipients:
                s.sendmail(settings.email_sender, recipient["email"], msg.as_string())
                time.sleep(0.5)
    except Exception as e:
        print(f"Error: {e}")
