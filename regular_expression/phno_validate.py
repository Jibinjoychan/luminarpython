import re

#eg:10 numbers

x='\d{10}'
vname=input("enter variable name")
match=re.fullmatch(x,vname)
if(match!=None):
    print("valid")
else:
    print("invalid variable name")