
import schedule
import time
from datetime import datetime

# Task 1: Display a daily reminder
def reminder():
    print("Reminder: Attend your Python class!",
          datetime.now().strftime("%H:%M:%S"))

# Task 2: Generate a report
def generate_report():
    print("Report generated successfully!",
          datetime.now().strftime("%H:%M:%S"))

# Task 3: Back up data
def backup_data():
    print("Data backup completed!",
          datetime.now().strftime("%H:%M:%S"))


# Schedule the tasks at different intervals
schedule.every(1).minutes.do(reminder)
schedule.every(2).minutes.do(generate_report)
schedule.every(3).minutes.do(backup_data)

print("Task scheduler started...")
print("Reminder: Every 1 minute")
print("Report: Every 2 minutes")
print("Backup: Every 3 minutes")
print("Press stop button to stop the program.\n")

try:
    while True:
        schedule.run_pending()
        time.sleep(1)

except KeyboardInterrupt:
    print("Scheduler stopped.")
