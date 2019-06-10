#!usr/bin/python3

import time
import webbrowser
from googlesearch import search
url=[]
web=input("Please enter topic")
for i in search(web,stop=10):
	print(i)
	time.sleep(3)
	url.append(i)
	print(url)
'''
try:
	from googlesearch import search
except ImportError:
	print("no module name google found")
query="hello"
for j in search(query,tld="com",num=10,stop=10,pause=2):
	print(j)
'''	
