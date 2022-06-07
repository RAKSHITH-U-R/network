#client
import socket

ID = '1001100010011001'
R = '0'
DF = '0'

HOST = 'localhost'
PORT = 12345

psize = int(input('packetSize: '))
rno = int(input('no of routers: '))
mtu = list()
for i in range(rno):
    mtu.append(input('mtu for router'+str(i+1)+': '))
    
packet = ID+'-'+R+'-'+DF+'-0-0-'+str(psize-20)
print('datagram structure: [ID-R-DF-M-OFFSET-DATALENGTH]')
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as c:
    c.connect((HOST, PORT))
    c.send((packet + ' ' + str(rno) +' ' + ' '.join(mtu)).encode())
    datagrams = c.recv(8192).decode().split(',')
    for i in datagrams:
        print(i)
        
