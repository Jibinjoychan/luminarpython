def num(p1):
    for i in range(2,p1):
        flag=0
        if(p1%i==0):
            flag=1
            break
        else:
            pass
    if(flag>0):
        print("not prime")
    else:
        print("prime")
num(16)