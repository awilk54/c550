import socket
import sys
import getpass
import hashlib
import re

SERVER_IP=sys.argv[1] #server IP argument
INPUT_PORT=sys.argv[2] 	#port argument
CLIENT_PASS1=sys.argv[3] #client password 1
CLIENT_PASS2=sys.argv[4] #client password 2
CLIENT_PASS3=sys.argv[5] #client password 3
OUTPUT_FILE=sys.argv[6] #output file arguement
OF=str(OUTPUT_FILE) #convert output file name to string
PORT=int(INPUT_PORT) #convert port string to integer before passing to socket connect
SRV_IP=(SERVER_IP) #convert server ip string to integer before passing to socket connect
#print (SRV_IP)

PAYLOAD= ["JOIN_REQ",CLIENT_PASS1,CLIENT_PASS2,CLIENT_PASS3] #password payload packet
s=str(PAYLOAD) #payload string convert
b= bytes(s, 'utf-8') #payload converted to bytes
JR=b'PASS_RESP' #Join Request byte for sending to server
REJECT="PASSREJECT" #reject packet string for IF compare
SRV_ADDRESS= (SRV_IP, PORT) #var tuple for sending server address and port
print()
print ("Welcome to UPD Connect")
print ("Coded by Anthony Wilkinson, CYBER550")
print ()
'''
# Ask for IP address of server
print("Please Enter IPv4 Server Address:")
IP_ADDR= input()
SRV_ADDRESS= (IP_ADDR, PORT) #var tuple for sending server address and port
print()
print ("You Entered IPV4 Server Address:")
print (IP_ADDR)
print ()
print ()
'''
PORT=int(INPUT_PORT) #convert port string to integer before passing to socket connect


clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #INITIATE UDP Socket


while True:
	clientSock.sendto(b, (SRV_IP, PORT))
	data= clientSock.recvfrom(4096) #recieve pass_req
	print ("RX PASS_REQ Packet")
	clientSock.sendto(JR,SRV_ADDRESS)#send pass_resp packet
	print ()
	print ("TX PASS_RESP Packet") 
	data, addr= clientSock.recvfrom(4096) #recieve pass_accept
	deny_data=data.decode("utf-8") #decode reject packet data to string
	deny_data2=deny_data.split(",") #split payload by comma
	TEMP_DENY=deny_data2[0] 
	DENY=re.sub('[^A-Za-z0-9]+', '', TEMP_DENY)#take out random chars
	print ()
	if DENY == REJECT: #if statement to exit if password token is invalid
		print ("Invalid Password...Now Exiting")
		print ("ABORT!!")
		exit()
	print ("RX PASS_ACCEPT Packet")
	data= clientSock.recvfrom(4096) #recieve txt file data and write that crap to output file 
	strdata=str(data)
	new_file= open(OF, "w+")
	new_file.write(strdata)
	new_file.close()
	#print("Server File Data:",data)
	print()
	print ("RX Terminate Packet")
	print ()
	print ("OK")
	data= clientSock.recvfrom(4096)
	break
clientSock.close()