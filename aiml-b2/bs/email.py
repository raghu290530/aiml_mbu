import smtplib
from email.message import EmailMessage

sender = "nedunooririshivarun47@gmail.com"
password = "pilwtdxkficheuhl"
receiver = "yanivam998@comzx.com"

message = EmailMessage()
message["From"] = sender
message["To"] = receiver
message["Subject"] = "Python Automation Test"

message.set_content(
    "Hello!\n\n"
    "This email was sent automatically using Python."
)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender, password)
    server.send_message(message)

print("Email sent successfully!")