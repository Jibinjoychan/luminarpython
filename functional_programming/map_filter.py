'''lst=[10,20,30]
def square(num1):
    return(num1*num1)

sqlist=list(map(square,lst))
print(sqlist)'''


lst=[10,20,30]
#map(function,iterables
sq=list(map(lambda num1:num1**2,lst))
print(sq)