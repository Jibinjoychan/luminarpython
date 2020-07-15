class parent:
    def phone(self):
        print("iphone")
class child(parent):
    def phone2(self):
        print("asus")
obj=child()
obj.phone2()
obj.phone()