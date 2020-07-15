f=open("students.txt","r")
fw=open("passed.txt","r")
fww=open("failed.txt","w")
for name in f:
    if name not in fw:
        fww.write(name)
    else:
        pass