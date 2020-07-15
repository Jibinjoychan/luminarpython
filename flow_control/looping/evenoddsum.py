l1=int(input("enter lower limit"))
l2=int(input("enter upper limit"))
o=0
e=0
while(l1<=l2):
    if(l1%2==0):
        e=e+l1
    else:
        o=o+l1
    l1+=1
print("total odd",o)
print("total even",e)