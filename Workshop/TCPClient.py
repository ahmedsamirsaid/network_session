import socket as sk 
serverIP= input("Enter Server IP address: ")
serverPort= int(input("Enter Server Port: "))
clientSocket= sk.socket(sk.AF_INET, sk.SOCK_STREAM)#open socket for TCP "SOCK_STREAM" connection and IPv4 "AF_INET" address family

clientSocket.connect((serverIP,serverPort))# connect to server with IP and Port 
while True:
    data= input("Enter Data or 0 to exit: ")
    if data =='0':
        break
    clientSocket.sendall(data.encode()) # send data to server  
    receivedData=clientSocket.recv(1024) # receive data from server
    print(f"Data received from server is \"{receivedData.decode()}\"")
clientSocket.close() # close connection with server