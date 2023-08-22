import socket as sk
import threading

closeThreads=False
numberOfConnections = 0
connectionThreads= []
server_ip=sk.gethostbyname(sk.gethostname()) #set server ip to the ip of the machine 
server_port= 12345

def manageClient(clientSocket:sk.socket, addr): #function to manage client connection by receiving and sending data
    global numberOfConnections
    while not closeThreads:
        data = clientSocket.recv(1024)
        if not data:
            break
        data=data.decode()
        print(f'[{addr[0]}:{addr[1]}]:{data}')
        message= f'I received from you this message : \"{data}\"'
        clientSocket.sendall(message.encode('UTF-8'))
    print(f'Closing Connection to client: {addr[0]}:{addr[1]}')
    clientSocket.close()
    numberOfConnections-=1


server_socket= sk.socket(sk.AF_INET, sk.SOCK_STREAM) #open socket for TCP "SOCK_STREAM" connection and IPv4 "AF_INET" address family
server_socket.bind((server_ip,server_port)) #bind socket to server ip and port

server_socket.listen(5) #listen for connections with maximum of 5 connections in queue
print(f'Listening on IP: {server_port}  and Port: {server_port}...') 
try:
    while True:
        print(f'Number of connections= {numberOfConnections}')
        client_sock, client_addr= server_socket.accept() #accept connection from client and return socket and address
        print(f"Connected to {client_addr}")
        thread= threading.Thread(target=manageClient, args=(client_sock,client_addr,)) #create thread to manage client connection
        numberOfConnections+=1
        thread.start() #start thread 
        connectionThreads.append(thread) 
except:
    server_socket.close() #close server socket
    closeThreads= True