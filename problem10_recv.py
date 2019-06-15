#!usr/bin/python2

import socket
recv_ip="127.0.0.1"
recv_port=4444 # 0-1024 -- you can chck free udp port netstat -nulp

#creating udp socket
# ip type V4,UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#fitting ip and port with udp socket
s.bind((recv_ip,recv_port))

#receiving data from sender
i=1
while i==1:
	data=s.recvfrom(100)
	print("message from sender",data[0])
#reply to sender
	rply=raw_input("type your rply:")
	s.sendto(rply,data[1])
	i=input("Press 1 for continue and 0 for end")

s.close()
