````markdown
# 📧 Email Automation & Reminder System

A Python + Streamlit based Email Automation & Reminder System that automates reminder emails using CSV contact data, customizable templates, SMTP integration, scheduling, logging, and report generation.

---

# 🚀 Project Overview

This project helps automate repetitive email communication tasks such as:

- Reminder emails
- Follow-up notifications
- Task alerts
- Meeting reminders
- Webinar notifications
- Payment reminders

The system reads contact and reminder data from CSV files, generates personalized emails using templates, and sends emails automatically using SMTP.

A Streamlit dashboard is included for interactive usage.

---

# 🎯 Industry Relevance

This project simulates real-world automation systems used by:

- HR Teams
- Operations Teams
- Training Departments
- Sales Teams
- Customer Support Teams
- Productivity Automation Systems

It demonstrates:
- Backend automation
- Email workflows
- CSV processing
- Scheduling systems
- Logging & reporting
- Streamlit dashboard deployment

---

# ✨ Features

## ✅ Email Automation
Automatically sends reminder emails.

## ✅ Personalized Templates
Uses dynamic placeholders like:

{name}

{task}

## ✅ CSV-Based Workflow
Uploads:
- contacts.csv
- reminders.csv

## ✅ Dry Run Mode
Safely test automation without sending real emails.

## ✅ SMTP Integration
Supports Gmail SMTP.

## ✅ Logging System
Tracks:
- successful emails
- failed emails

## ✅ CSV Report Generation
Generates downloadable reports.

## ✅ Streamlit Dashboard
Interactive web-based UI.

---

# 🛠 Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core Programming |
| Streamlit | Web Dashboard |
| Pandas | CSV Processing |
| SMTP | Email Sending |
| schedule | Scheduling |
| dotenv | Environment Variables |
| logging | Logging System |

---

# 📁 Project Structure

EMAIL-AUTOMATION-REMINDER-SYSTEM/

├── data/
│   ├── contacts.csv
│   └── reminders.csv
│
├── templates/
│   └── email_template.txt
│
├── src/
│   ├── email_sender.py
│   ├── report_generator.py
│   ├── scheduler.py
│   ├── template_manager.py
│   └── utils.py
│
├── outputs/
├── logs/
├── images/
├── docs/
│
├── app.py
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/email-automation-reminder-system.git
```

---

## 2️⃣ Navigate to Project Folder

```bash
cd email-automation-reminder-system
```

---

## 3️⃣ Create Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate:

```bash
.\.venv\Scripts\activate
```

---

### Mac/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file:

```env
EMAIL=your_email@gmail.com
PASSWORD=your_app_password
```

⚠ Never upload `.env` to GitHub.

---

# 📂 Sample CSV Files

## contacts.csv

```csv
id,name,email
1,Arshiya Muskan,arshiya.muskan@gmail.com
2,Rahul Sharma,rahul.sharma@outlook.com
```

---

## reminders.csv

```csv
contact_id,subject,task
1,Python Project Reminder,Submit Email Automation Project before Friday
2,Meeting Reminder,Attend Zoom meeting at 4 PM today
```

---

# ▶️ Run Streamlit App

```bash
python -m streamlit run app.py
```

---

# 🌐 Local URL

http://localhost:8501

---

# 🧪 Dry Run Mode

Dry Run Mode simulates email sending without actually sending emails.

Inside sidebar:

✅ Enable Dry Run Mode


# 🔥 Example Personalized Email

Subject: Python Project Reminder

Hello Arshiya Muskan,

This is a friendly reminder regarding:

Submit Email Automation Project before Friday

Please complete it on time.

Best Regards,  
Automation Team

---

# 🚀 Future Improvements

- Authentication System
- SQLite Database
- Analytics Dashboard
- Email Scheduling UI
- AI Email Generator
- Multi-template Support
- Email History Tracking
- Bulk Email Campaigns

---

# 💼 Learning Outcomes

This project helped in learning:

- Python Automation
- SMTP Email Systems
- Streamlit Dashboard Development
- CSV Data Processing
- Logging & Reporting
- Environment Variable Security
- GitHub Project Management

---

# 👩‍💻 Author

Arshiya Muskan

---

# 📜 License

This project is for educational and portfolio purposes.
````
