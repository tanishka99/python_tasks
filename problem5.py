#!usr/bin/python3
import datetime
cur_time=datetime.datetime.now()
cur_time.hour
if cur_time.hour<12:
	print("goodmornning!")
elif 12<=cur_time.hour<18:
	print("goodafternoon!")
else:
	print("goodeveniing")
