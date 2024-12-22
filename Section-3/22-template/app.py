from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from string import Template
import smtplib

template = Template(Path("Section-3/22-template/template.html").read_text)
# template.substitute()

message = MIMEMultipart()
message["from"] = "Muhammad Msa"
message["to"] = "alkaline4peace@gmail.com"
message["subject"] = "This is a test"
# message.attach(MIMEText("Body", "plain"))
body = template.substitute({"name": "Muhammad"})
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("Section-3/21-sending_email/placeholder.jpg").read_bytes()))

# Update SMTP host and port
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.set_debuglevel(1)  # Enable debugging
    smtp.ehlo()
    smtp.starttls()
    # Use app password instead of account password
    smtp.login("alkaline4peace@gmail.com", "my_password")
    smtp.send_message(message)
    print("Sent...")
