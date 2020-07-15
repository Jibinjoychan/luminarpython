lst=[1,2,3,4,5,6]
elst=[]
olst=[]
for item in lst:
    if(item%2==0):
        elst.append(item)
    else:
        olst.append(item)

print("even list",elst)
print("odd list",olst)