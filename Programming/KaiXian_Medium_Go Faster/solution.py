#!/usr/bin/python3
import socket
import time
import hashlib
import socket

host = "192.168.42.131"
port = 4000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print("Connected")
while True:
	result = s.recv(1024).strip();
	print(result.decode())
	string = result[-20:]
	md5 = hashlib.md5(string.decode('utf-8').encode()).hexdigest().encode()
	s.send(md5 + "\n".encode())
	print('Send: ' + md5.decode())
