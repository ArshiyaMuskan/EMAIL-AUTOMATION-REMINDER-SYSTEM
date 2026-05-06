import smtplib
import logging

from email.message import EmailMessage

class EmailSender:

    def __init__(self, sender_email, sender_password, dry_run=True):

        self.sender_email = sender_email
        self.sender_password = sender_password
        self.dry_run = dry_run

    def send_email(self, recipient, subject, body):

        try:

            if self.dry_run:

                print(f"[DRY RUN] Simulated email to: {recipient}")

                logging.info(
                    f"[DRY RUN] Simulated email to: {recipient}"
                )

                return "DRY_RUN_SUCCESS"

            msg = EmailMessage()

            msg["Subject"] = subject
            msg["From"] = self.sender_email
            msg["To"] = recipient

            msg.set_content(body)

            with smtplib.SMTP_SSL(
                "smtp.gmail.com",
                465
            ) as smtp:

                smtp.login(
                    self.sender_email,
                    self.sender_password
                )

                smtp.send_message(msg)

            print(f"Email sent to {recipient}")

            logging.info(
                f"SUCCESS → {recipient}"
            )

            return "SUCCESS"

        except Exception as error:

            print(
                f"Failed to send email to {recipient}"
            )

            logging.error(
                f"FAILED → {recipient} → {error}"
            )

            return "FAILED"