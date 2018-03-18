import socket
import sys
import getpass
import hashlib

#UDP_PORT1=sys.argv[1]
UDP_PORT= 8900
Message = b'Sending Test Message' #Testing Send Data to Server

print ("Welcome to UPD Connect")
print ()

# Ask for IP address of server
print("Please Enter IPv4 Address:")
IP_ADDR= input()
print()
print ("You entered IPv4:")
print (IP_ADDR)

user_pass = input('please enter pass: ')
bytes= bytearray()
bytes.extend(map(ord,user_pass))

while True:
	clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	clientSock.connect((IP_ADDR, UDP_PORT))
	clientSock.send(bytes)
	clientSock.close()
	break
	

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSock.connect((IP_ADDR, UDP_PORT))
#clientSock.send(bytes)
clientSock.sendto(Message, (IP_ADDR, UDP_PORT))

data= clientSock.recvfrom(4096)
strdata=str(data)
new_file= open("Output.txt", "w+")
new_file.write(strdata)
new_file.close()


print("Server File Data:",data)
'''
f = open ('test.txt', 'wb')
f.write(data)
f.close()

'''
#print ("You sent the server the following information :" ,data)
'''
with open('newfile.txt', 'w') as f:
	f.write(data3)

'''	
'''
while True:
	clientSock.connect((IP_ADDR, UDP_PORT))
	f= open(data, 'wb')
	data =clientSock.recvfrom(2048)
	while (data):
		print ("Recieving File..")
		f.write(data)
		data =clientSock.recvfrom(2048)
	f.close()
	print ("done receving")
	clientSock.close()
	
	'''
		


print ("OK")
clientSock.close()