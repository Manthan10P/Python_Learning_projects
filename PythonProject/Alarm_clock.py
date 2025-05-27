import time
import datetime
import os

# Step 1: Get user input
alarm_time = input("Set the alarm time (HH:MM:SS, 24-hour format): ")
print(f"Alarm is set for {alarm_time}")

# Step 2: Loop until the time matches
while True:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    if current_time == alarm_time:
        print("Wake up! Alarm time reached!")
        # Optional: Play sound (requires alarm.mp3 file)
        # os.system("start alarm.mp3")  # Windows
        # os.system("afplay alarm.mp3")  # macOS
        break
    time.sleep(1)
