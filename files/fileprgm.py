lst=[]
fin=open("C:/Users/JITTO JOYCHAN/PycharmProjects/luminarproject/files/file1","r")
for name in fin:
    print(name)
    lst.append(name.rstrip("\n")) #rstrip is using to remove \n
print(lst)
#to upper case
for name in lst:
    print(name.upper())

