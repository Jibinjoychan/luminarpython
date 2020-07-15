num=int(input("enter a number"))
flag=0
for i in range(2,num):
    if(num%i==0):
        flag=1
        break
    else:
        print("")
if(flag>0):
    print("not prime")
else:
    print("prime")