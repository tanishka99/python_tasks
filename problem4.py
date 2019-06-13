#!usr/bin/python3

import os
name=input("enter your username")
check=0
num=[0,1,2,3,4,5,6,7,8,9]
for i in name:
	if i in str(num):
		check=1
if check==1:
	print("invalid username")
else:
	psswd="hello"+name
	os.system("useradd " +psswd+" " +name)
	print("a user is added")

