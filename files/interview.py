'''f=open("person.txt","r")
#100,jibin,23,developer,10000
emp={100:{"name":"jibin","age":23,"des":"developer","salary":1000}}
print(emp[100]["salary"])'''
f=open("person.txt","r")
emp={}
for data in f:
    values=data.rstrip("\n").split(",")
    id=values[0]
    name=values[1]
    age=values[2]
    desig=values[3]
    exp=values[4]
    salary=values[5]
    if(id not in emp):
        emp[id]={"id":id,"name":name,"age":age,"desig":desig,"exp":exp,"salary":salary}
    else:
        pass
for k,v in emp.items():
    print(k,"\t",v)

'''def printEmployee(**kwargs):
    for k,v in kwargs.items():
        id=v
        if(id in emp):
            print(emp[id]["name"])
        else:
            print("ther is no employee id with",id)
printEmployee(id="100")'''

'''def printEmployee(**kwargs):
    prop=kwargs["property"]
    id=kwargs["id"]
    print(emp[id]["name"])
    print(emp[id][prop])

printEmployee(id="101",property="salary")'''

def printEmployee(**kwargs):
    if "id" in kwargs:
        id = kwargs["id"]
        if id in emp:
            print(emp[id]["name"])
        else:
            print("no emp")
    if "property" in kwargs:
        prop = kwargs["property"]
        print(emp[id][prop])
printEmployee(id="100",property="salary")



