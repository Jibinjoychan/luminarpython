class EMP:
    def __init__(self,id,name,desig,salary,exp):
        self.id=id
        self.name=name
        self.desig=desig
        self.salary=salary
        self.exp=exp
    def printdetails(self):
        print(self.id,",",self.name,",",self.desig,",",self.salary,",",self.exp)
f=open("emp")
lst=[]
for data in f:
    print(data)
    employee=data.rstrip("\n").split(",")
    id=employee[0]
    name=employee[1]
    desig=employee[2]
    salary=int(employee[3])
    exp=int(employee[4])
    obj=EMP(id,name,desig,salary,exp)
    obj.printdetails()
    lst.append(obj)

namecaps=list(map(lambda EMP:EMP.name.upper(),lst))
print(namecaps)

designation=list(filter(lambda EMP:EMP.desig=="developer",lst))
for values in designation:
    print(values.name)

highsalary=list(filter(lambda EMP:EMP.salary>15000,lst))
for values in highsalary:
    print(values.name)

increment=list(filter(lambda EMP:EMP.exp>=2,lst))
for values in increment:
    print(values.name,":",values.salary)
    sal=values.salary+5000
    print("updated salary",sal)



