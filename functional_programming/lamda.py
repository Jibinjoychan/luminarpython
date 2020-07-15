#it is an anonymous function
#def add(num1,num2)
#    return(num+num2)  it is normal function

#lambda function
#lambda arguments:expression

f1=lambda num1,num2:(num1+num2)
f2=lambda num1,num2:(num1*num2)
f3=lambda num1,num2:(num1-num2)
print(f1(10,15))
print(f2(10,5))
print(f3(10,10))

sq=lambda num:num**2
print(sq(10))
