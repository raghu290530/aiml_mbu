import schedule
import time
from datetime import datetime

def reminder():
    current_time = datetime.now()

    print("Automation task executed at:",
          current_time.strftime("%H:%M:%S"))

# Schedule the task every 10 seconds
schedule.every(2).seconds.do(reminder)

print("Scheduler started...")

while True:
    schedule.run_pending()
    time.sleep(1)