#Client
from Datalink import*
from socket import*
from time import*
from random import*

clientsocket=socket(AF_INET,SOCK_STREAM)
host='localhost'
port=8088
clientsocket.connect((host,port))

data='1'*64
sendbitss=sendbits(data)
for i in range(len(sendbitss)):
    clientsocket.send(str(sendbitss[i]).encode('utf-8'))
    sleep(1)
clientsocket.close()
