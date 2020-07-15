f=open("C:/Users/JITTO JOYCHAN/PycharmProjects/luminarproject/files/movies.csv","r")
dict={}
i=0
for lines in f:
    words=lines.rstrip("\n").split("\t")
    #print(words)
    year=words[2]
    if(year not in dict):
        dict[year]=1
    else:
        dict[year]+=1
    i+=1
    if(i==50):
        break
sortedyears=sorted(dict.items(),key=lambda x:x[1],reverse = True)
#print(dict)
print(sortedyears)
print(sortedyears[0][0])