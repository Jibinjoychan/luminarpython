n=int(input("enter a number"))
rev=0
while(n>0):
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
print("reversed number is",rev)

# // used for remove floting point value (floting division)