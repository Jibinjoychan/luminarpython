#for pattern matching
#first import 're' package
#start use to in which location matching is occured
#group is used to ethu pattern ayittanu match cheyyane ennu ullath
import re
matcher=re.finditer("ab","ababab")
count=0
for match in matcher:
    print(match.start())
    print(match.group())
    count+=1
print(count)
