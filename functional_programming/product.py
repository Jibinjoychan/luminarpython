class product:
    def __init__(self,id,name,category,price):
        self.id=id
        self.name=name
        self.category=category
        self.price=price
    def __str__(self):
        return self.name

lst=[]
ob=lst.append(product(100,"lux","soap",50))
ob=lst.append(product(101,"celtux","pen",10))
ob=lst.append(product(102,"phone","sony",1000))

namelst=list(map(lambda product:product.name.upper(),lst))
print(namelst)

price=list(filter(lambda product:product.price>55,lst))
for value in price:
    print(value)