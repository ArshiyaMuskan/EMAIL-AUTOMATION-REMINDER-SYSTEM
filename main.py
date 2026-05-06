import os
import pandas as pd

from dotenv import load_dotenv
from datetime import datetime

from src.utils import (
    setup_logging,
    ensure_directories
)

from src.template_manager import (
    load_template,
    personalize_template
)

from src.email_sender import EmailSender
from src.report_generator import ReportGenerator

# -------------------------------------
# LOAD ENVIRONMENT VARIABLES
# -------------------------------------

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# -------------------------------------
# CREATE REQUIRED DIRECTORIES
# -------------------------------------

ensure_directories()

# -------------------------------------
# SETUP LOGGING
# -------------------------------------

setup_logging()

# -------------------------------------
# DRY RUN MODE
# -------------------------------------

# True  -> Simulate emails
# False -> Send real emails

DRY_RUN = True

# -------------------------------------
# LOAD CSV FILES
# -------------------------------------

contacts_df = pd.read_csv(
    "data/contacts.csv"
)

reminders_df = pd.read_csv(
    "data/reminders.csv"
)

# -------------------------------------
# LOAD EMAIL TEMPLATE
# -------------------------------------

template = load_template(
    "templates/email_template.txt"
)

# -------------------------------------
# CREATE OBJECTS
# -------------------------------------

email_sender = EmailSender(
    EMAIL,
    PASSWORD,
    dry_run=DRY_RUN
)

report_generator = ReportGenerator()

# -------------------------------------
# MAIN FUNCTION
# -------------------------------------

def process_reminders():

    print("\nProcessing reminders...\n")

    for _, reminder in reminders_df.iterrows():

        contact = contacts_df[
            contacts_df["id"]
            ==
            reminder["contact_id"]
        ]

        if contact.empty:

            print("Contact not found.")
            continue

        name = contact.iloc[0]["name"]
        email = contact.iloc[0]["email"]

        subject = reminder["subject"]
        task = reminder["task"]

        personalized_message = personalize_template(
            template,
            name,
            task
        )

        status = email_sender.send_email(
            email,
            subject,
            personalized_message
        )

        report_generator.add_result(
            name,
            email,
            task,
            status,
            datetime.now()
        )

    report_generator.generate_report()

    print("\nReminder process completed.\n")

# -------------------------------------
# RUN APPLICATION
# -------------------------------------

if __name__ == "__main__":

    print("=" * 50)
    print("EMAIL AUTOMATION SYSTEM STARTED")
    print("=" * 50)

    process_reminders()