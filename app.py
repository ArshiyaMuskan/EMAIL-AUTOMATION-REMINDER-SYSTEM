import os
import pandas as pd
import streamlit as st

from dotenv import load_dotenv
from datetime import datetime

from src.template_manager import (
    load_template,
    personalize_template
)

from src.email_sender import EmailSender
from src.report_generator import ReportGenerator

# -----------------------------------------
# PAGE CONFIG
# -----------------------------------------

st.set_page_config(
    page_title="Email Automation System",
    layout="wide"
)

# -----------------------------------------
# LOAD ENVIRONMENT VARIABLES
# -----------------------------------------

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# -----------------------------------------
# TITLE
# -----------------------------------------

st.title("📧 Email Automation & Reminder System")

st.markdown("""
Automate reminders, notifications, and follow-up emails using Python + Streamlit.
""")

# -----------------------------------------
# SIDEBAR
# -----------------------------------------

st.sidebar.header("Settings")

dry_run = st.sidebar.checkbox(
    "Enable Dry Run Mode",
    value=True
)

# -----------------------------------------
# FILE UPLOADS
# -----------------------------------------

st.header("📂 Upload CSV Files")

contacts_file = st.file_uploader(
    "Upload Contacts CSV",
    type=["csv"]
)

reminders_file = st.file_uploader(
    "Upload Reminders CSV",
    type=["csv"]
)

# -----------------------------------------
# TEMPLATE
# -----------------------------------------

st.header("📝 Email Template")

default_template = """
Hello {name},

This is a friendly reminder regarding:

{task}

Please complete it on time.

Best Regards,
Automation Team
"""

template = st.text_area(
    "Edit Email Template",
    value=default_template,
    height=250
)

# -----------------------------------------
# PROCESS BUTTON
# -----------------------------------------

if st.button("🚀 Run Email Automation"):

    if contacts_file and reminders_file:

        contacts_df = pd.read_csv(
            contacts_file
        )

        reminders_df = pd.read_csv(
            reminders_file
        )

        st.success("Files uploaded successfully.")

        email_sender = EmailSender(
            EMAIL,
            PASSWORD,
            dry_run=dry_run
        )

        report_generator = ReportGenerator()

        results = []

        st.subheader("📨 Processing Emails")

        for _, reminder in reminders_df.iterrows():

            contact = contacts_df[
                contacts_df["id"]
                ==
                reminder["contact_id"]
            ]

            if contact.empty:
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

            result = {
                "name": name,
                "email": email,
                "task": task,
                "status": status,
                "timestamp": datetime.now()
            }

            results.append(result)

            st.write(
                f"✅ {name} → {status}"
            )

        # ---------------------------------
        # GENERATE REPORT
        # ---------------------------------

        report_df = pd.DataFrame(results)

        if not os.path.exists("outputs"):
            os.makedirs("outputs")

        report_path = "outputs/report.csv"

        report_df.to_csv(
            report_path,
            index=False
        )

        st.success("Automation completed.")

        st.subheader("📊 Report")

        st.dataframe(report_df)

        # ---------------------------------
        # DOWNLOAD BUTTON
        # ---------------------------------

        with open(report_path, "rb") as file:

            st.download_button(
                label="⬇ Download Report CSV",
                data=file,
                file_name="report.csv",
                mime="text/csv"
            )

    else:

        st.error(
            "Please upload both CSV files."
        )