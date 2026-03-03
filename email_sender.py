import smtplib
import os
from email.message import EmailMessage


class EmailSender:
    def __init__(self, email, password, smtp_server="smtp.gmail.com", smtp_port=587):
        self.email = email
        self.password = password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_email(self, to_email, subject, body, attachment_path=None):
        msg = EmailMessage()
        msg["From"] = self.email
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.set_content(body)

        # Attach resume if provided
        if attachment_path and os.path.exists(attachment_path):
            with open(attachment_path, "rb") as f:
                file_data = f.read()
                file_name = os.path.basename(attachment_path)

            msg.add_attachment(
                file_data,
                maintype="application",
                subtype="pdf",
                filename=file_name
            )

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.email, self.password)
            server.send_message(msg)

        print(f"✅ Email sent to {to_email}")