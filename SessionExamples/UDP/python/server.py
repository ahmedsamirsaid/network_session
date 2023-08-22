import socket as sk
import os


# SERVER_IP = input('Enter server IP address: ')
# SERVER_PORT = int(input('Enter Server port: '))

sock = sk.socket(sk.AF_INET,  sk.SOCK_DGRAM)
sock.bind((sk.gethostname(), 12345))

duration = 1  # seconds
print(f"Server listening...{sk.gethostbyname(sk.gethostname())}")
# sock.listen(5)
try:
    while True:
        data, addr = sock.recvfrom(1024) 
        print(data)  
        print(addr)
        number= min(800,data[0]*256+data[1])
        print(number)
except KeyboardInterrupt:
    print('Closing Server...')
    sock.close()


    