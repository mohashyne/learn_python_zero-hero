# send email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

message = message = MIMEMultipart()
message ["from"] = "Muhammad Msa"
message ["to"] = "alkaline4peace@gmail.com"
message ["subject"] = "This is a test"
message. attach (MIMEText ("Body"))

with smtplib.SMTP(host="smtp-gmail.com", port=587) as smtp:
    smtp.ehlo( )
    smtp.starttls()
    smtp.login("testuser@codewithmosh.com", "today")
    smtp.send_message(message)
    print ("Sent...")