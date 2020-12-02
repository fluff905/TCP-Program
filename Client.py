import socket
import random

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = solution[]

FORWARD = [255][0][255][0]
BACKWARD = [0][255][0][255]
RIGHTTURN = [255][0][0][255]
LEFTTURN = [0][255][255][0]

c = random.randint(1,4)
if( c =1)
    MESSAGE = FORWARD
if(c=2)
    MESSAGE = BACKWARD
if(c=3)
    MESSAGE = RIGHTTURN
if(c=4)
    MESSAGE = LEFTTURN


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(bytes(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print ("received data:", data)