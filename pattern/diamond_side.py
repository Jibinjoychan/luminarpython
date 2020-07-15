n=int(input("enter the limit"))
for i in range(0,n):
    for j in range(0,(i+1)):
        print("*",end="")
    print("\n")

for ii in range(n-1,0,-1):
    for jj in range(1,(ii+1)):
        print("*",end="")
    print("\n")
