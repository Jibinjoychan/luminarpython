class Student:
    def __init__(self,id,name,batch,score):
        self.id=id
        self.name=name
        self.batch=batch
        self.score=score
    def printstd(self):
        print(self.id,",",self.name,",",self.batch,",",self.score)
obj=Student(10,"jibin","mca",120)
