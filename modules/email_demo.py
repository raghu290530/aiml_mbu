
import smtplib
import ssl
from email.message import EmailMessage

sender = "raghu290530@gmail.com"
receiver = "takineh131@goldlicai.com"

# Replace with your Gmail App Password
password = "dbiz rzub reee hczn"

message = EmailMessage()
message["From"] = sender
message["To"] = receiver
message["Subject"] = "Python Automation- AIMLB5"

message.set_content(
    "Hello!\n\n"
    "This email was sent automatically using Python.\n\n"
    "Regards,\n"
    "Python Automation"
)

try:
    context = ssl.create_default_context()

    # Connect securely to Gmail using SSL
    with smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465,
        context=context,
        timeout=30
    ) as server:

        print("Connected to Gmail SMTP server")

        server.login(sender, password)
        print("Login successful")

        server.send_message(message)
        print("Email sent successfully!")

except smtplib.SMTPAuthenticationError:
    print("Login failed. Check your Gmail address and App Password.")

except smtplib.SMTPServerDisconnected:
    print("Server disconnected. Check your internet, firewall,")
    print("and try SMTP port 587 with STARTTLS.")

except (OSError, smtplib.SMTPException) as error:
    print("Email sending failed:", error)
