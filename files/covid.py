f=open("C:/Users/JITTO JOYCHAN/PycharmProjects/luminarproject/files/complete.csv","r")
dict={}
i=0
for lines in f:
    report=lines.rstrip("\n").split("\t")
    print(report)
    state=report[1]
    cases=int(report[4])
    if(state not in dict):
        dict[state]=cases
    else:
        dict[state]=cases
print(dict)

caseslist=[]
for k,v in dict.items():
    caseslist.append(v)
print(sum(caseslist))
srtlst=[]
for k,v in dict.items():
    srtlst.append((v,k))
print(srtlst)
sorteddata=sorted(srtlst,reverse=True)
print(sorteddata[:3])

#sortedvalue=sorted(dict.items(),key=lambda x:x[1],reverse=True)
#print(sortedvalue[0])