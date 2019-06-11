Question 
Write a code  will take  input as your name and greet you with
good morning , good evening , goodafter noon , good night as per the current time your system :
      
Solution
!usr/bin/python3
import datetime
cur_time=datetime.datetime.now()
cur_time.hour
if cur_time.hour<12:
	print("goodmornning!")
elif 12>=cur_time.hour<18:
	print("goodafternoon!")
elif: 17> cur_time.hour<21
	print("goodeveniing")
else:
	print("goodnight")
