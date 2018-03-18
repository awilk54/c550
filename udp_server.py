import socket
import sys
import time

PORT= sys.argv[1] #Port specified by arugment when running script
SERVER_PASSWORD= sys.argv[2] #Server password send when running script
INPUT_FILE= sys.argv[3] #Text file input when running script

UDP_SERVER_VER = "1.0"
UDP_SERVER_IP = "127.0.0.1"
UDP_BUFFER=4096
PASS= 'CYBER'

NEW_PORT=int(PORT) #Convert port to integer
addr2= (UDP_SERVER_IP, NEW_PORT)

	

print ()
print ("Server Version: ", UDP_SERVER_VER) #print server info
print ()
print ("Server IP: ", UDP_SERVER_IP, "Listenting on Port:", PORT) #Print Port and IP
print()

#Create socket
UDPSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print ('Socket Initialized')
UDPSock.bind((UDP_SERVER_IP, NEW_PORT)) #Bind the socket to IP/Port
print ()
password = UDPSock.recvfrom(UDP_BUFFER)
print ("Client Sent Password:", password)
print ()



	
#Keep socket running, recieve message from client and send data back
while True:
	
	data, addr = UDPSock.recvfrom(UDP_BUFFER)
	print ("Client connected from IP:", addr)
	print ()
	print ("Client Sent:", data.decode("utf-8"))	
	print ()
	
	INPUTFILE1= open(str(sys.argv[3]), "r")
	line= INPUTFILE1.read()
	print("Text File Contents:",line)
	if line:
		bytes1 = bytes(line, 'utf-8')
		print("Data Read:", bytes1, end='')
		UDPSock.sendto(bytes1,addr)
	else:
		break
		#sent= UDPSock.sendto(data, addr)
		#print (sent, addr)
	break
#==================================================================================		
print()
#method to recive .txt file from argumnet when launching script and then take file and send back to client
UDPSock.sendto(INPUT_FILE.encode('utf-8'),addr2)
#f=open(filename, "rb")
f=open(sys.argv[3], 'rb')
data1= f.read(UDP_BUFFER)
print ("Name of File Input:", INPUT_FILE)
#print ("File Contents:", data1)





print ("File sent to client...OK")
UDPSock.close()