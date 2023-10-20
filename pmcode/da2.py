import os
import datetime
import time
from pygame import mixer

invalid = True

while(invalid):
    # Get a valid user input for the alarm time
    print("Set a valid time for the alarm (Ex. 06:30)")
    userInput = input(">> ")
    alarmTime = [int(n) for n in userInput.split(":")]
    if alarmTime[0] >= 24 or alarmTime[0] < 0:
        invalid = True
    elif alarmTime[1] >= 60 or alarmTime[1] < 0:
        invalid = True
    else:
        invalid = False

# Number of seconds in an Hour, Minute, and Second
seconds_hms = [3600, 60, 1]

# Convert the alarm time to seconds
alarmSeconds = sum([a*b for a,b in zip(seconds_hms[:len(alarmTime)], alarmTime)])

now = datetime.datetime.now()
currentTimeInSeconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])

secondsUntilAlarm = alarmSeconds - currentTimeInSeconds

if secondsUntilAlarm < 0:
    secondsUntilAlarm += 86400 # number of seconds in a day

print("Alarm is set!")
print("The alarm will ring at %s" % datetime.timedelta(seconds=secondsUntilAlarm))

time.sleep(secondsUntilAlarm)

# Initialize mixer and play sound
mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
mixer.music.load("Báo Thức Bá Đạo.mp3")
mixer.music.play()

print("Ring Ring... time to wake up!")
