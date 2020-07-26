import webbrowser
import datetime
import re
from time import sleep
from sys import argv

alarm_time = datetime.timedelta()
alarm_hour = 0
alarm_minute = 0
url = "https://www.youtube.com/watch?v=lgtoypeY9yg&list=PLLU7Oh2-moMV2MEeCt6GgXSCCaSlP3LIR"

#-Checking for wakeup time or asking for it----------------------
if len(argv) > 1:
	intime = datetime.datetime.strptime(str(argv[1]), "%H%M").time()
	alarm_hour = intime.hour
	alarm_minute = intime.minute

else:
	print("What time do you want to wake up?\n")

	print("Enter hour (0-23)")
	alarm_hour =int(input(">>> "))

	print("\nEnter minutes(0-59)")
	alarm_minute = int(input(">>> "))
#----------------------------------------------------------------

#-Checking if there is a URL or using the default----------------
if len(argv) > 2:
		url = str(argv[2])
#----------------------------------------------------------------

#-Enabling autoplay if not set-----------------------------------
if re.match(r"&autoplay=1", url):
	pass
else:
	url += "&autoplay=1"
#----------------------------------------------------------------


ntime = datetime.datetime.now()

current_time = datetime.timedelta(hours = ntime.hour, minutes = ntime.minute, seconds = ntime.second)

alarm_time = datetime.timedelta(hours = alarm_hour, minutes = alarm_minute, seconds = 0)

sleep_time = alarm_time - current_time


print("\n\n    Current Time:")
print("    ", current_time)

print("\n    Alarm Time:")
if sleep_time < datetime.timedelta():
	print("    Tomorrow")
	sleep_time += datetime.timedelta(days = 1)
else:
	print("    Today")
print("    ", alarm_time)

print("\n    Amount of sleep:")
print("    ", sleep_time)


sleep(sleep_time.total_seconds())

webbrowser.open(url, new=0)
