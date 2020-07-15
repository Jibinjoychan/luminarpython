f=open("C:/Users/JITTO JOYCHAN/PycharmProjects/luminarproject/files/complete.csv","r")
dict={}
i=0
for lines in f:
    report=lines.rstrip("\n").split("\t")
    print(report)
    state=report[1]
    curedcases=int(report[6])
    if(state not in dict):
        dict[state]=curedcases
    else:
        dict[state]=curedcases
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