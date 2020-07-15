#i used to abc ile athelum letter athil undenno enn nokkum
import re
x='[abc]'
matcher=re.finditer(x,"ab7k9z")
count=0
for match in matcher:
    print(match.start())
    print(match.group())
    count+=1
print(count)