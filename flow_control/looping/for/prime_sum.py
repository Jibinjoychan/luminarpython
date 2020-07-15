lower=int(input("enter lower limit"))
upper=int(input("enter upper limit"))
for i in range(lower,upper+1):
    flag=0
    aa=0
    for j in range(2,i):
        if(i%j==0):

            flag=1
        else:
            pass
    if(flag>0):
        pass
    else:
        print(i,"prime")
