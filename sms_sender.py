# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# Import load_dotenv from dotenv
from dotenv import load_dotenv

# Run load_dotenv() to make the .env file accessible as your source of environment variables
load_dotenv()


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='Hello Gregory!',
         from_=os.getenv("MY_TWILIO_PHONE_NUMBER"),
         to=os.getenv("MY_PHONE_NUMBER")
     )

print(message.sid)