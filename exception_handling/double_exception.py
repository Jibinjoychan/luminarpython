num1 = int(input("no1"))
num2 = int(input("no2"))
lst=[10,20,21]
indx=int(input("enter index position"))
try:
    res = num1 / num2
    print("result", res)
    print(lst[indx])
except Exception as e:
    print(e.args)

finally:

print("new line")

#except Exception as e
#Exception is the class has nickname e
#e.args print which exception is occured