import socket
import sys
import time
import re
import hashlib

PORT= sys.argv[1] #Port specified by arugment when running script
SERVER_PASSWORD= sys.argv[2] #Server password send when running script
INPUT_FILE= sys.argv[3] #Text file input when running script

UDP_SERVER_VER = "1.0"
UDP_SERVER_IP = "127.0.0.1"
UDP_BUFFER=4096
#SERVER_PASS= "CYBER"
SECRET_PASS=str(SERVER_PASSWORD)
#print(SECRET_PASS)

ACCEPT= "PASS_ACCEPT"
s1=str(ACCEPT)
b1= bytes(s1, 'utf-8')
REJECT= "PASS_REJECT"
s2=str(REJECT)
b2= bytes(s2, 'utf-8')
PR=b'PASS_REQ' # pass_req packet variable as byte
TERM=b'TERMINATE' #TERMINATE packet varaible as byte

NEW_PORT=int(PORT) #Convert port to integer
addr2= (UDP_SERVER_IP, NEW_PORT)



print ()
print ("Server Version: ", UDP_SERVER_VER) #print server info
print ()
print ("Server IP: ", UDP_SERVER_IP, "Listenting on Port:", PORT) #Print Port and IP
print()




UDPSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Create UDP Socket
print ('Socket Initialized...')
UDPSock.bind((UDP_SERVER_IP, NEW_PORT)) #Bind the socket to IP/Port
#data, addr = UDPSock.recvfrom(UDP_BUFFER)
print ()
print ()


while True: #Keep socket running, recieve message from client and send data back
	data, addr = UDPSock.recvfrom(UDP_BUFFER)
	print ("RX JOIN_REQ Packet")
	UDPSock.sendto(PR,addr)#send Pass_REQ packet
	data, addr = UDPSock.recvfrom(UDP_BUFFER)
	print ("A Client Machine Has Just Connected From IP:", addr)
	print ()
	#print ("Client Sent:", data.decode("utf-8"))
	PR=UDPSock.recvfrom(UDP_BUFFER)
	print ("RX PASS_RESP Packet")
	print ()
	payload_data=data.decode("utf-8") #decode payload data to string
	payload_data2=payload_data.split(",") #split payload by comma
	#Temp_REQ=payload_data2[0] 
	#SEND_REQ=re.sub('[^A-Za-z0-9]+', '', Temp_REQ)#strip crap
	PASS1=payload_data2[0]
	NEW_PASS1=re.sub('[^A-Za-z0-9]+', '', PASS1)#strip crap
	PASS2=payload_data2[1]
	NEW_PASS2=re.sub('[^A-Za-z0-9]+', '', PASS2)#strip crap
	PASS3=payload_data2[2]
	NEW_PASS3=re.sub('[^A-Za-z0-9]+', '', PASS3)#strip crap

	
	if NEW_PASS1 == SECRET_PASS:
		UDPSock.sendto(b1,addr)
		print("TX PASS_ACCEPT Packet")
	elif NEW_PASS2 == SECRET_PASS:
		UDPSock.sendto(b1,addr)
		print("TX PASS_ACCEPT Packet")
	elif NEW_PASS3 == SECRET_PASS:
		UDPSock.sendto(b1,addr)
		print("TX PASS_ACCEPT Packet")
	else:
		UDPSock.sendto(b2,addr)
		print("ABORT..Wrong Password")
		print ()
		UDPSock.sendto(TERM,addr) #packet to reject password attempt
		print ("TX TERMINATE Packet")
		exit()
		
	print ()
	#print ("Client Sent Password of:", payload_data) 
	#clean_data= payload_data.spilt(",")
	#print ("client sent password new:", clean_data)
	print ()
	INPUTFILE1= open(str(sys.argv[3]), "r")
	line= INPUTFILE1.read()
	
	print("Reading TXT File...")
	print()
	if line:
		bytes1 = bytes(line, 'utf-8')
		#print("Data Read:", bytes1, end='')
		
		UDPSock.sendto(bytes1,addr)
		hash_file = hashlib.sha1(bytes1)
		hex_dig = hash_file.hexdigest()
		hex_dig1=hex_dig.encode()
		UDPSock.sendto(hex_dig1,addr)
		print ("TXT File Data Sent to Client Succesfully!")
		print()
		print("File_Hash:",hex_dig)
	else:
		break
	break

print()
print("OK!")
print("Goodbye. Now Exitng..")
UDPSock.sendto(TERM,addr)
UDPSock.close()