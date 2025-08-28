import time
import subprocess

def show_notification(message):
    subprocess.call(['osascript', '-e', f'display notification "{message}" with title "Reminder"'])

while True:
    show_notification("clear claude code context")
    time.sleep(300)  # 5 minutes