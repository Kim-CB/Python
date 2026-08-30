import os

from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(os.environ['TWILIO_SID'], os.environ["TWILIO_AUTH_TOKEN"])

    def send_wpp(self, message_body):
        message = self.client.messages.create(
            from_=os.environ["TWILIO_FROM_NUMBER"],
            body=message_body,
            to=os.environ["TWILIO_TO_NUMBER"]
        )
        print(message.sid)