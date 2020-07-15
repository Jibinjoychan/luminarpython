import re

#eg:kl01mn1234

x='KL\d{2}[a-z]*\d*'
vname=input("enter variable name")
match=re.fullmatch(x,vname)
if(match!=None):
    print("valid")
else:
    print("invalid variable name")