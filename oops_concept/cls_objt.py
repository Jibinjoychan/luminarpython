class demo:
    def fun(self,name,age):
        self.name=name
        self.age=age
    def prnt(self):
        print(self.age,'',self.name)
ob=demo()
ob.fun("jibin",14)
ob.prnt()
