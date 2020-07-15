age=int(input("enter age"))
if(age<18):
    raise Exception("invalid age")
else:
    print("u can vote")

#raise used to custamize the exception