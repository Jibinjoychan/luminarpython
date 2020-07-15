'''lst=[1,2,3,4,5]
def check(num1):
    return(num1%2==0)
even=list(filter(check,lst))
print(even)'''

lst=[1,2,3,4,5]
even=list(filter(lambda num1:num1%2==0,lst))
print(even)