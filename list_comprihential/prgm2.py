lst1=[1,2]
lst2=[3,4]
for i in lst1:
    for j in lst2:
        print((i,j))

pairs=[(i,j)for i in lst1 for j in lst2]
print(pairs)