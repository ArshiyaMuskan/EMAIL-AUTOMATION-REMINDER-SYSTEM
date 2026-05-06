import schedule
import time

class ReminderScheduler:

    def __init__(self, job_function):

        self.job_function = job_function

    def start(self):

        schedule.every(1).minutes.do(
            self.job_function
        )

        print("Scheduler started...")

        while True:

            schedule.run_pending()
            time.sleep(1)