# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+14156514181',
                     to='+14845093855'
                 )

print(message.sid)
