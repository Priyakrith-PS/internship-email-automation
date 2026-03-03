import pandas as pd
import time
from email_sender import EmailSender


class InternshipOutreach:
    def __init__(self, sender_email, sender_password, resume_path):
        self.sender = EmailSender(sender_email, sender_password)
        self.resume_path = resume_path

    def load_template(self, template_file):
        with open(template_file, "r") as file:
            content = file.read()

        subject_line = content.split("\n")[0]
        subject = subject_line.replace("SUBJECT: ", "").strip()
        body = "\n".join(content.split("\n")[1:])

        return subject, body

    def run_campaign(self, contacts):
        subject_template, body_template = self.load_template("templates.txt")

        print(f"Loaded {len(contacts)} contacts.\n")

        for index, contact in enumerate(contacts, start=1):
            try:
                subject = subject_template.format(company=contact["company"])
                body = body_template.format(
                    name=contact["name"],
                    company=contact["company"]
                )

                self.sender.send_email(
                    to_email=contact["email"],
                    subject=subject,
                    body=body,
                    attachment_path=self.resume_path
                )

                time.sleep(5)  # delay to avoid spam detection

            except Exception as e:
                print(f"❌ Failed for {contact['email']} → {e}")