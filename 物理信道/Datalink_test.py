from socket import*
from time import*
from random import*
class Daralink_test:
    #处理5个连续1的情况
    def five_1_pro(data):
        datapro=list(data)
        i=0
        length=len(datapro)
        while i<length:
            j=i
            if datapro[i]=='0':
                i+=1
                continue
            if datapro[i]=='1':
                count=0
                while j<length:
                    if count==5:
                        break
                    if datapro[j]=='0':
                        i=j
                        break
                    j+=1
                    count+=1
                if count==5:
                    datapro.insert(j,'0')
                    i=j
                    length+=1
                i+=1
        return ''.join(datapro)

    #帧定位字段添加
    def add_location(data):
        datapro=list(data)
        head='01111110'
        tail='01111110'
        datapro=''.join(datapro)
        return head+datapro+tail

    #帧定位
    def location(data):
        #datapro=list(data)
        head='01111110'
        tail='01111110'
        first=data.find(head)
        second=data.find(head,first+8)
        data=data[first+8:second]
        return data

    #处理5个连续1的情况
    def five_1zero_pro(data):
        index=data.find('111110')
        while index!=-1:
            datapro=list(data)
            del(datapro[index+5])
            data=''.join(datapro)
            index=data.find('111110',index+5)
        return data

    #添加校验码
    def D2odd_addcheck(data):
        length=len(data)
        matrix=[]
        for i in range(length):
            matrix.append(int(data[i]))
        if length!=64:
            for i in range(length,64):
                matrix.append(0)
        #row
        row=[]
        for i in range(8):
            sum=0
            for j in range(8):
                sum+=matrix[8*i+j]
            if sum%2==0:
                row.append(0)
            else:
                row.append(1)
        #column
        column=[]
        for j in range(8):
            sum=0
            for i in range(8):
                sum+=matrix[8*i+j]
            if sum%2==0:
                column.append(0)
            else:
                column.append(1)
        strrow=''.join([str(x) for x in row])
        strcolumn=''.join([str(x) for x in column])
        return ''.join([str(x) for x in matrix])+strrow+strcolumn

    #校验纠错
    def D2odd_check(data):
        row=list(data[64:72])
        row=[int(x) for x in row]
        column=list(data[72:80])
        column=[int(x) for x in column]
        matrix=list(data[0:64])
        matrix=[int(x) for x in matrix]
        rowerror=[]
        columnerror=[]
    #row
        for i in range(8):
            sum=0
            for j in range(8):
                sum+=matrix[8*i+j]
            sum+=row[i]
            if sum%2==0:
                continue
            else:
                rowerror.append(i)
    #column
        for j in range(8):
            sum=0
            for i in range(8):
                sum+=matrix[8*i+j]
            sum+=column[j]
            if sum%2==0:
                continue
            else:
                columnerror.append(j)
        if len(rowerror)!=0:
            print('error!')
            for i in range(len(rowerror)):
                print('第'+str(rowerror[i])+'行'+'第'+str(columnerror[i])+'列的数据出错了')
                if matrix[8*rowerror[i]+columnerror[i]]==0:
                    matrix[8*rowerror[i]+columnerror[i]]=1
                if matrix[8*rowerror[i]+columnerror[i]]==1:
                    matrix[8*rowerror[i]+columnerror[i]]=0 
        return ''.join([str(x) for x in matrix])

if __name__=='__main__':
    print("原始数据："+'11111111111111')
    newdata=five_1_pro('11111111111111')
    print("处理连续5个1的情况："+str(newdata))
    addcheck=D2odd_addcheck(newdata)
    print("加入校验码："+str(addcheck))
    datawithht=add_location(addcheck)
    print("加入帧头帧尾："+str(datawithht))
    print('''发送——物理层——接收''')
    receive=datawithht
    delht=location(receive)
    print("去掉帧头帧尾："+str(delht))
    checkcorrect=D2odd_check(delht)
    print("校验并纠错:"+str(checkcorrect))
    rawdata=five_1zero_pro(checkcorrect)      
    print("删去帧头帧尾，处理连续5个1的情况："+str(rawdata))


