lst=[1,5,8,3,4,7]
lst.sort()
upper=len(lst)
low=0
element=int(input("enter number to be search")
while(low<upper):
    mid=(low+upper)//2
    if(element>lst[mid]):
        low=mid+1
    elif (element=lst[mid]):
        print("present")
    elif(element<lst[mid]):
        upper=mid-1

