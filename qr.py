'''
try:
	from googlesearch import search
except ImportError:
	print("NO MODULE")
query="Geeksfrogeeks"

for i in search (query,tld="co.in",num=10,stop=3,):
	print(i)
'''
import pyqrcode
from pyqrcode import QRCode
s="www.geeksforgeeks"
url=pyqrcode.create(s)
url.svg("myqr.svg",scale=8)
