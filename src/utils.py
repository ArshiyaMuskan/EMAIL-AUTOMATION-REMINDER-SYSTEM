import logging
import os

def setup_logging():

    if not os.path.exists("logs"):
        os.makedirs("logs")

    logging.basicConfig(
        filename="logs/email.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def ensure_directories():

    folders = [
        "outputs",
        "logs"
    ]

    for folder in folders:

        if not os.path.exists(folder):
            os.makedirs(folder)