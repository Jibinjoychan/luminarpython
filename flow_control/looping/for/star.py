lim=int(input("enter limit"))
for i in range(1,lim+1):
    for j in range(1,i+1):
        print("*", end='')
    print("\r")