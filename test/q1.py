f=open("C:/Users/JITTO JOYCHAN/PycharmProjects/luminarproject/test/data.txt","r")
dict={}
for i in f:
    values= i.rstrip("\n").split(",")
    print(values)
    district=values[0]
    temp=int(values[1])
    if district not in dict:
        dict[district]=temp
    else:
        if(temp>dict[district]):
            dict[district]=temp
        else:
            pass
print(dict)


