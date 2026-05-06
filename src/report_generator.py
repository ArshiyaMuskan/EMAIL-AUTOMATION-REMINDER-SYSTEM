import pandas as pd

class ReportGenerator:

    def __init__(self):

        self.results = []

    def add_result(
        self,
        name,
        email,
        task,
        status,
        timestamp
    ):

        self.results.append({
            "name": name,
            "email": email,
            "task": task,
            "status": status,
            "timestamp": timestamp
        })

    def generate_report(self):

        report_df = pd.DataFrame(self.results)

        report_df.to_csv(
            "outputs/report.csv",
            index=False
        )

        print("CSV report generated.")