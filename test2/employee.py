import functools
import re
class EMP:
    def __init__(self,id,name,desig,mailid,salary):
        self.id=id
        self.name=name
        self.desig=desig
        self.mailid=mailid
        self.salary=salary
    def printdetails(self):
        print(self.id,",",self.name,",",self.desig,",",self.mailid,",",self.salary)
f=open("emp")
lst=[]
for data in f:
    #print(data)
    employee=data.rstrip("\n").split(",")
    id=employee[0]
    name=employee[1]
    desig=employee[2]
    mailid=employee[3]
    salary=int(employee[4])
    obj=EMP(id,name,desig,mailid,salary)
    obj.printdetails()
    lst.append(obj)


salarylst=list(map(lambda object1:object1.salary,lst))
high=functools.reduce(lambda object1,object2:object1 if object1>object2 else object2,salarylst)
print(high)

emaillist=list(map(lambda obj1:obj1.mailid,lst))
print(emaillist)

x='[a-zA-Z]\w*@gmail[.]com'
valid=lambda emailid:re.fullmatch(x,emailid)
validlst=list(filter(valid,emaillist))
print(validlst)

fwrite=open("valid_mails","w")
for i in validlst:
    fwrite.write(i+"\n")