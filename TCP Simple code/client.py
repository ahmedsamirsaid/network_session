import socket as sk


server_ip='127.0.1.1'
server_port=12345
sock=sk.socket(sk.AF_INET,sk.SOCK_STREAM)
sock.connect((server_ip,server_port))
while True:
    msg=input("Enter message: ")
    sock.send(msg.encode('utf-8'))
    data=sock.recv(1024)
    print(data.decode('utf-8'))
    if msg=='exit':
        print("exiting")
        break
sock.close()


