"""Using Twilio to send SMS"""
from twilio.rest import Client
import config

ACCT_SID = config.acct_sid
AUTH_TOKEN = config.auth_token

client = Client(ACCT_SID, AUTH_TOKEN)  # Create a Twilio client
call = client.messages.create(
    to="++2348036559220",
    from_="+14404674893",
    body="Hello from Twilio!"
)

print(call.sid)  # Output: <MessageSid: 1234567890abcdef>
print("Message sent successfully!")  # Output: Message sent successfully!
