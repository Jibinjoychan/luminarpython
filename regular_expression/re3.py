import re
x='[a-z]'
#x='[0-9]'
#x='[a-zA-Z]'
#X='[^a-z]'  cap symbol used to except(ozike)
#x='\s' space check cheyyum
#x='\d' chck for digits
#x='\D' check for [^0-9]
#='\w' check words [a-zA-z0-9]
#='\w' except words

matcher=re.finditer(x,"ab7k9z")
count=0
for match in matcher:
    print(match.start())
    print(match.group())
    count+=1
print(count)