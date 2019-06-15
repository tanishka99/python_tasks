#!usr/bin/python2

import socket
recv_ip="127.0.0.1"
recv_port=4444 # 0-1024 -- you can chck free udp port netstat -nulp

#creating udp socket
# ip type V4,UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#sending data to target
while 4 > 3:

	msg=raw_input("plz enter your msg ,(enter ex to come out of chat")
	if len(msg)>150:
		print("msg length exceeded")
	if msg=="ex":
		break
	else:
	#sending data to target
		s.sendto(msg,(recv_ip,recv_port))
	#recv data from recv
		print(s.recvfrom(10))

