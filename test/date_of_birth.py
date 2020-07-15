'''dob=input("enter dob")
d_o_b=dob.split("/")
current_year=input("current year")
age=int(current_year)-int(d_o_b[-1])
print(age)'''

crntdate=29
crntmnt=6
crntyer=2020
bd=int(input("enter date"))
bm=int(input("enter month"))
by=int(input("enter year"))
age=crntyer-by
if(bm>crntmnt):
    if(bd<crntdate):
        age=age-1;
print("age is",age)
