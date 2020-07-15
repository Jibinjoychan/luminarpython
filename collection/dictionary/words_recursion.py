text="helloworld"
word=list(text)
print(word)
dict={}
for ltr in word:
    if(ltr not in dict):
        dict[ltr]=1
    else:
        print("recurssing", ltr)
        break