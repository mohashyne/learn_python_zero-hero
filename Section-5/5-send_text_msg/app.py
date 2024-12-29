from twilio.rest import Client
import config

acct_sid = config.acct_sid
auth_token = config.auth_token

client = Client(acct_sid, auth_token)

    
call = client.messages.create(
    to="++2348036559220",
    from_="+14404674893",
    body="Hello from Twilio!"
)
print(call.sid)  # Output: <MessageSid: 1234567890abcdef>
print("Message sent successfully!")