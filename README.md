Cyber 550 Assignment 1

This is a project to demonstrate UDP socket client/server programming.

Three files needed to run assignment.

udp_client.py udp_server.py python.txt

Launch udp_server.py with the following arugments:
  udp_server.py <port number> <password> <input.txt>
  *port number must be a valid computer port 1-49151
  *password can be a random string created by you
  *input.txt can be any text file with text inside of it.
  
After launching your server please launch the client

Launch udp_client.py with the following arugments:
  udp_client.py <serverIP> <port> <password1> <password2> <password3> <outputfile.txt>
  *server IP should be entered as the loopback 127.0.0.1 since the udp_server.py is hard coded with that IP
  *port number should be the same port as you passed as an arugment when launching the server
  *password1-3 should be three passwords created by you. only one will match the server password. If 1 of 3 passwords authenticate with the server, then the server will send it's text file to the client. If not, it will termiante and tell you invalid password.
  *outputfile.txt can be named whatever you like. This is the output file that your client will use to write all data send from text file on udp_server.
