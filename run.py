from twilio.rest import Client
import os

def send_message():
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    twilio_phone = os.environ.get('TWILIO_PHONE_NUMBER')
    recipient_phone = os.environ.get('RECIPIENT_PHONE')  # Retrieve recipient phone from secrets

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Hello! This is your scheduled message.",
        from_=twilio_phone,
        to=recipient_phone
    )

    print("Message sent:", message.sid)

if __name__ == "__main__":
    send_message()