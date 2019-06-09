#!usr/bin/python3
import os

for i in range(500):
	dirname=str(i)
	os.mkdir(dirname)
	print("directry created",i )

