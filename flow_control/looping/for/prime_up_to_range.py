num1=int(input("enter lower limit"))
num2=int(input("enter upper limit"))
for num in range(num1,num2+1):
    if(num>1):
        for i in range(2,num):
            if(num%1==0):
                break
        else:
            print(num)

