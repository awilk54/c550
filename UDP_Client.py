import socket
import sys
import getpass
import hashlib


INPUT_PORT=sys.argv[1] 	#port arugement
CLIENT_PASS1=sys.argv[2] #client password 1
CLIENT_PASS2=sys.argv[3] #client password 2
CLIENT_PASS3=sys.argv[4] #client password 3
OUTPUT_FILE=sys.argv[5] #output file arguement
OF=str(OUTPUT_FILE) #convert output file name to string
PORT=int(INPUT_PORT) #convert port string to integer before passing to socket connect

PAYLOAD= ["JOIN_REQ",CLIENT_PASS1,CLIENT_PASS2,CLIENT_PASS3] #password payload packet
s=str(PAYLOAD) #payload string convert
b= bytes(s, 'utf-8') #payload converted to bytes



PASS1 = b'Sending Test Message' #Testing Send Data to Server

print ("Welcome to UPD Connect")
print ()

# Ask for IP address of server
print("Please Enter IPv4 Address:")
IP_ADDR= input()
print()
print ("You entered IPv4:")
print (IP_ADDR)
PORT=int(INPUT_PORT) #convert port string to integer before passing to socket connect


clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #INITIATE UDP Socket


while True:
	clientSock.sendto(b, (IP_ADDR, PORT))
	data= clientSock.recvfrom(4096)
	strdata=str(data)
	new_file= open(OF, "w+")
	new_file.write(strdata)
	new_file.close()
	#print("Server File Data:",data)
	print()
	print ("OK")
	break
clientSock.close()