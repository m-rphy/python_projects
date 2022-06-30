#!/usr/bin/env python3

#Sockets and Requests

import socket

host = "web.physics.ucsb.edu" 
port = 80 

# creating a socket 
thesocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
 
# connecting to the client 
thesocket.connect((host,port))  
 
# Making a request for HTTP data 
request = "GET /~phys129/lipman/ HTTP/1.1\r\nHost:%s\r\n\r\n" % host
thesocket.send(request.encode())   

# Receiving the HTTP data and closing the socket
response = thesocket.recv(4096)  
http_response = str(repr(response))
thesocket.shutdown(socket.SHUT_RDWR)
thesocket.close()

#Parsing the HTTP data for the desired text
begining = http_response.find('Latest update')
ending = http_response.find('</span></p>')
Latest_update = http_response[begining:ending].replace('<span class="greenss">','').replace('&nbsp;',' ')

#The output
print('')
print('Physics 129L '+Latest_update)
print('')
