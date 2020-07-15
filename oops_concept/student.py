class Student:
    def __init__(self,id,name,batch,score):
        self.id=id
        self.name=name
        self.batch=batch
        self.score=score
    def printstd(self):
        print(self.id,",",self.name,",",self,batch,",",self.score)
f=open("std")
stdlst=[]
namelst=[]
name2lst=[]
for data in f:
    print(data)
    students=data.rstrip("\n").split(",")
    id=students[0]
    name=students[1]
    batch=students[2]
    score=int(students[3])
    ob=Student(id,name,batch,score)
    stdlst.append(ob)
    #ob.printstd()
for students in stdlst:
    print("score above 150")
    if(students.score>150):
        print(students.name)
print("names in upper case")
for students in stdlst:
    name=students.name
    print(name.upper())
print("mca students are")
for students in stdlst:
    if(students.batch =="mca"):
        namelst.append(students.name)
print(namelst[0:])
print("bca students are")
for students in stdlst:
    if(students.batch =="bca"):
        name2lst.append(students.name)
print(name2lst[0:])

