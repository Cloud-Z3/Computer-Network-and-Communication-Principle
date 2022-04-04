#Server
from phy_channel import*
from socket import*
from time import*
from random import*

serversocket=socket(AF_INET,SOCK_STREAM)
host='localhost'
port=8088
serversocket.bind((host,port))
serversocket.listen(5)
t_start=time()
print("Waiting for connect....\n")
clientsocket,address=serversocket.accept()

print("Connected successfully.\n")
#print("Address:"+str(address))
#print(address)
tstart=time()
storedata=[]

recvdata=clientsocket.recv(1000).decode('utf-8')
recvdata=phy_channel(recvdata)
storedata.append(recvdata)

    
print(storedata)



    
