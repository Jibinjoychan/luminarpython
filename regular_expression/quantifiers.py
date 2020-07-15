#check the number of quantity
import re
#x='a+' #it will check the single a and combination of a
#x='a*' #check occurence of a and also check a illatha position
#x='a?' oro postion ilum a undo enn check cheyyum.illengium position print cheyyum
#x='a{2}' #check for 2 number of a
#x='a{2,3}' minimum 2 number of a and max 3 number of a


matcher=re.finditer(x,"aaaaabbbbbaaaabbbaaa")
#count=0
for match in matcher:
    print(match.start())
    print(match.group())
    #count+=1
#print(count)