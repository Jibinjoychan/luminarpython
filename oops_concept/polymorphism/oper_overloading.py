class book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return (self.pages+other.pages)
    def __mul__(self,other1):
        return (self.pages*other1.pages)
    def __sub__(self,other3):
        return (self.pages-other3.pages)

    def __str__(self):
        return str(self.pages)
b=book(100)
b1=book(200)
print(b+b1)
print(b*b1)
print(b1-b)