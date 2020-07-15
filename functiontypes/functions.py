'''def add(**kwargs):
    print(kwargs)
add(num1=10,num2=20,num3=30)

#kwargs acts like a dictionary
#it is a predefined function
#it will store datas'''

def add(**kwargs):
    total=0
    for k,v in kwargs.items():
        total+=v
    print(total)
add(num1=10,num2=20,num3=30)