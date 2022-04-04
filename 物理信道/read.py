# 使用readline()读文件
f = open("a.txt",encoding='utf-8')
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
print(listnew)
