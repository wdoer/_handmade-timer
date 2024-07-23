import os
from datetime import datetime, timedelta
from pync import Notifier

def send_notification(title, message):
    Notifier.notify(message, title=title)

def format_time_delta(delta):
    total_seconds = int(delta.total_seconds())
    minutes, seconds = divmod(total_seconds, 60)
    return f"{minutes}:{seconds}"

def check_schedule():
    now = datetime.now()
    
    start_time = now.replace(hour=10, minute=0, second=0, microsecond=0)
    end_time = now.replace(hour=20, minute=0, second=0, microsecond=0)

    current_cycle_start = start_time
    while current_cycle_start + timedelta(hours=2, minutes=30) <= now:
        current_cycle_start += timedelta(hours=2, minutes=30)

    work_period_end = current_cycle_start + timedelta(hours=2)
    rest_period_end = work_period_end + timedelta(minutes=30)
    
    if current_cycle_start <= now < work_period_end:
        time_left = format_time_delta(work_period_end - now)
        send_notification("Job", f"Work end at: {time_left}")
    elif work_period_end <= now < rest_period_end:
        time_left = format_time_delta(rest_period_end - now)
        send_notification("Rest", f"Freedom end at: {time_left}")
    else:
        send_notification("Pomodoro Timer", "Unknown error")

check_schedule()
