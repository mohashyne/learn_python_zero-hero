from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

message = MIMEMultipart()
message["from"] = "Muhammad Msa"
message["to"] = "alkaline4peace@gmail.com"
message["subject"] = "This is a test"
message.attach(MIMEText("Body"))

# Update SMTP host and port
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.set_debuglevel(1)  # Enable debugging
    smtp.ehlo()
    smtp.starttls()
    # Use app password instead of account password
    smtp.login("alkaline4peace@gmail.com", "my_password")
    smtp.send_message(message)
    print("Sent...")
