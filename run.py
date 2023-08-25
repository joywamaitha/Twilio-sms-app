from twilio.rest import Client
from datetime import datetime
import os

def send_message():
       account_sid = os.environ.get('TWILIO_SID')
       auth_token = os.environ.get('TWILIO_TOKEN')
       twilio_phone = os.environ.get('TWILIO_PHONE')
       recipient_phone = os.environ.get('RECIPIENT_PHONE')

       client = Client(account_sid, auth_token)

       message = client.messages.create(
           body="Hello! This is your scheduled message.",
           from_=twilio_phone,
           to=recipient_phone
       )

       print("Message sent:", message.sid)

def main():
       now = datetime.now()
       if now.hour == 9:  # Adjust this to your time zone
           send_message()

if __name__ == "__main__":
       main()