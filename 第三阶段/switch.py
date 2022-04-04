def readcontent(filename):
    f = open(filename,encoding='utf-8')
    addresslist=[]
    while True:
        line = f.readline()
        if line:
            index=line.find('\n')
            listline=list(line)
            del(listline[index:index+2])
            addresslist.append(''.join(listline))
        else:
            break
    f.close()
    listnew=[]
    for i in range(len(addresslist)):
        segm=[]
        segm1=[]
        for j in range(len(addresslist[i])):
            if addresslist[i][j]==' ':
                segm1.append(segm)
                segm=[]
                continue
            segm.append(addresslist[i][j])
        segm1.append(segm)
        listnew.append(segm1)
    return listnew

def findroute(startpoint,endpoint):
    self_list=readcontent(startpoint+'.txt')
    print(self_list)
    if len(self_list)==1:
        return ''
    for i in (1,len(self_list)):
        if self_list[i][0][0]==endpoint:
            route=self_list[0][0][0]
        else:
            route=findroute(self_list[i][0][0],endpoint)
    return startpoint+route



print('ABCDFGH')
