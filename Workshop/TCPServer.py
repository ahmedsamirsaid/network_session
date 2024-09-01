import socket as sk
import threading

closeThreads = False
numberOfConnections = 0
connectionThreads = []
server_ip = sk.gethostbyname(sk.gethostname())
server_port = 12345

def manageClient(clientSocket: sk.socket, addr):
    global numberOfConnections
    while not closeThreads:
        data = clientSocket.recv(1024)
        if not data:
            break
        
        data = data.decode()
        print(f'[{addr[0]}:{addr[1]}]: {data}')
        
        if data.startswith("GET") or data.startswith("POST"):  # Handle HTTP requests from a browser
            response = """\
HTTP/1.1 200 OK

<html>
<head><title>Server Response</title></head>
<body><h1>Received your message!</h1></body>
</html>
"""
            clientSocket.sendall(response.encode('UTF-8'))
        else:  # Handle other device connections
            message = f'I received from you this message: \"{data}\"'
            clientSocket.sendall(message.encode('UTF-8'))
    
    print(f'Closing Connection to client: {addr[0]}:{addr[1]}')
    clientSocket.close()
    numberOfConnections -= 1

server_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
server_socket.bind((server_ip, server_port))

server_socket.listen(5)
print(f'Listening on IP: {server_ip} and Port: {server_port}...')
try:
    while True:
        print(f'Number of connections= {numberOfConnections}')
        client_sock, client_addr = server_socket.accept()
        print(f"Connected to {client_addr}")
        thread = threading.Thread(target=manageClient, args=(client_sock, client_addr,))
        numberOfConnections += 1
        thread.start()
        connectionThreads.append(thread)
except:
    server_socket.close()
    closeThreads = True
