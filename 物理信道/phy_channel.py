from random import*
def phy_channel(recvdata):
    storedata=list(recvdata)
    length=len(storedata)
    #误码率0.1%
    error_num=int(length/1000)
    if error_num!=0:
        for i in range(error_num):
           error_index=radint(length)
           if storedata[error_index]=='0':
               storedata[error_index]=='1'
           else:
               storedata[error_index]=='0'
    head_length=randint(0,12)
    tail_length=randint(0,12)
    for i in range(tail_length):
        storedata.append(str(randint(0,1)))
    for i in range(head_length):
        storedata.insert(i,str(randint(0,1)))
    return ''.join(storedata)
if __name__=='__main__':
    stdt=phy_channel('1010101')
    print(stdt)
