import re

#eg:jib@gmail.com

x='[a-zA-Z]\w*@gmail[.]com'
vname=input("enter variable name")
match=re.fullmatch(x,vname)
if(match!=None):
    print("valid")
else:
    print("invalid variable name")