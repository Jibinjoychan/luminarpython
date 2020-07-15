import re
#1st char should be a-k
#econd should be digit and divisible by 3
#any number of char
#eg:a9kkth

x='[a-k][369][a-z]*'
vname=input("enter variable name")
match=re.fullmatch(x,vname)
if(match!=None):
    print("valid")
else:
    print("invalid variable name")
