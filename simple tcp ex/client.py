import socket as sk



server_ip='192.168.1.7'
server_port=12345
sock=sk.socket(sk.AF_INET,sk.SOCK_STREAM)
sock.connect((server_ip,server_port))

while True:
    msg=input('Enter massage')
    sock.send(msg.encode('utf-8'))
    data=sock.recv(1024)
    print(data.decode('utf-8'))
    if msg=='exit':
        print("exiting")
        break
sock.close()










# import socket

# SERVER_HOST = '192.168.1.7'  # Change this to the server's IP address or hostname
# SERVER_PORT = 12345       # Change this to the server's port

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.connect((SERVER_HOST, SERVER_PORT))

# message = "Hello, server!"
# client_socket.send(message.encode())

# data = client_socket.recv(1024)
# print(f"Received from server: {data.decode()}")

# client_socket.close()
