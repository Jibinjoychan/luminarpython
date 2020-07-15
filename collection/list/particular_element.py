lst=[1,2,7,4,5,6]
num=int(input("enter a number"))
flag=0
count=0
for i in lst:
    count=count+1
    if(i==num):
        flag=1
        break
    else:
        pass
if(flag>0):
    print("present in",count)
else:
    print("not present")