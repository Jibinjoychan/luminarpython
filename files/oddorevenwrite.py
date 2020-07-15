f=open("oddeven.txt","r")
fw=open("outeven.txt","w")
for data in f:
    num=int(data)
    if(num%2==0):
        fw.write(str(num))
