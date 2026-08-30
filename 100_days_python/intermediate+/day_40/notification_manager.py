import os
import smtplib

from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

class NotificationManager:

    def __init__(self):
        self.smtp_adrress = os.getenv("EMAIL_PROVIDER_SMTP_ADDRESS")
        self.email = os.getenv("MY_EMAIL", "")
        self.email_password = os.getenv("MY_EMAIL_PASSWORD", "")
        self.client = Client(os.getenv('TWILIO_SID'), os.getenv("TWILIO_AUTH_TOKEN"))
        self.connection = smtplib.SMTP("smtp.gmail.com", port=587)

    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_=os.environ["TWILIO_WHATSAPP_NUMBER"],
            body=message_body,
            to=os.environ["TWILIO_VERIFIED_NUMBER"]
        )
        print(message.sid)


    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{os.environ["TWILIO_WHATSAPP_NUMBER"]}',
            body=message_body,
            to=f'whatsapp:{os.environ["TWILIO_VERIFIED_NUMBER"]}'
        )
        print(message.sid)

    def send_emails(self, email_list, email_body):
            with self.connection:
                self.connection.starttls()
                self.connection.login(self.email, self.email_password)
                for email in email_list:
                    self.connection.sendmail(
                        from_addr=self.email,
                        to_addrs=email,
                        msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8')  # noqa: UP012
                    )