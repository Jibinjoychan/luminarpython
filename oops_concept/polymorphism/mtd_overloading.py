class meth:
    def add(self):
        print("one")
    def add(self,n1):
        print("two")
    def add(self,n1,n2):
        print("three")
obj=meth()
obj.add(1,2)