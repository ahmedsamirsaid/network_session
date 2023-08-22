import socket as sk
import os


SERVER_IP = input('Enter server IP address: ')
SERVER_PORT = int(input('Enter Server port: '))
sock= sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

number=0
while True:
    data= [0,0]
    data[0]= 170
    data[1]= 201
    print(f'Sent {data[0]}&&{data[1]}')
    address= (SERVER_IP,SERVER_PORT)
    sock.sendto(bytearray(data), address)
    # data,addr=sock.recvfrom(1024)
    # print(data)

    