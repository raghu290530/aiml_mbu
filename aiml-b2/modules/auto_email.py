import smtplib
from email.message import EmailMessage

sender = "raghug290530@gmail.com"
password = "dbiz rzub reee hczn"
receiver = "takineh131@goldlicai.com"

message = EmailMessage()
message["From"] = sender
message["To"] = receiver
message["Subject"] = "Python Automation Test - Raghu"

message.set_content(
    "Hello!\n\n"
    "This email was sent automatically using Python."
)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender, password)
    server.send_message(message)

print("Email sent successfully!")