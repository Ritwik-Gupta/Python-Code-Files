#python3.7

N = int(input("Enter length of array"))

arr=[]

for i in range(1,N+1):
    arr.append(i)

k = int(input("Enter element to search"))

def binarySearch(arr,l,r,x):
    if(r-l>=0):
        mid = l + int((r-l)/2)
        if(arr[mid]==x):
            return(mid)
        elif(arr[mid]>x):
            return(binarySearch(arr,l,mid-1,x))
        else:
            return(binarySearch(arr,mid+1,r,x))
    else:
        return(-1)

val = binarySearch(arr,0,len(arr)-1,k)

if(val!=-1):
    print("Element found at index ",val)
else:
    print("Element not Found!!")
