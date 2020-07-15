class p1:
    def m1(self):
        print("inside parent 1")
class p2(p1):
    def m2(self):
        print("inside parent 2")
class p3(p2):
    def m3(self):
        print("inside parent 3")

obj=p3()
obj.m1()
obj.m2()
obj.m3()