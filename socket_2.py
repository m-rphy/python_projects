#!/usr/bin/env python3

# Author : William Murphy, with help from Professor Lipman
# Date   : 07May22

# Description : 
#			
#	This program creates a socket server, and sends
#	the current time to any client that connects to
#	the port 55555. This program is listening to all 
#	availble IPv4 addresses possible, though it is shut
#	immediately after sending the data packet.


import socket
import time


#Creates a socket and binds to a TCP port "prt"

def bind_port(prt):

   host = ''  #Bind to all available interfaces
	
	#Creates a socket, binds to it and listens
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   s.bind((host, prt))
   s.listen(1)
    
   return(s)


#Creating a packet of data to send
seconds = time.time()
local_time = time.ctime(seconds)
time_str = 'Local time: '+str(local_time)
msg = str.encode(time_str, 'utf-8')

print('Waiting for connection to be established...')

#Defining the TCP port to bind to
port = 55555

#Naming the socket and inputting the port
thesocket = bind_port(port)

#Sending the data (The current time)
connection, peer = thesocket.accept()
connection.sendall(msg) 
connection.shutdown(socket.SHUT_RDWR)
connection.close()

print('Data Packet Sent')
