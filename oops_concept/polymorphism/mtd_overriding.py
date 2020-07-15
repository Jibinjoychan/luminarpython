class parent:
    def phone(self):
        print("iphone")
class child(parent):
    def phone(self):
        print("asus")

obj=child()
obj.phone()