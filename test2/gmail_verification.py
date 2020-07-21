import re
f=open("emp","r")
empl={}
for data in f:
    values=data.rstrip("\n").split(",")
    id=values[0]
    name=values[1]
    desig=values[2]
    mailid=values[3]
    salary=values[4]
    if(id not in empl):
        empl[id]={"id":id,"name":name,"desig":desig,"mailid":mailid,"salary":salary}
    else:
        pass
for k,v in empl.items():
    print(k,"\t",v)


#eg:jib@gmail.com

x='[a-zA-Z]\w*@gmail[.]com'
mailid=values[3]
match=re.fullmatch(x,mailid)
if(match!=None):
    print("valid")
else:
    print("invalid variable name")
