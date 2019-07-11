#python3.7

def leftRotateByOne(arr,n):
    temp=arr[0]
    for i in range(len(arr)-1):
        arr[i]=arr[i+1]
    arr[-1]=temp
    return(arr)

def leftrotate(arr,d,n):
    if(d>n):
        d=d%n
    for i in range(d):
        arr=leftRotateByOne(arr,n)
    print("The rotated array is:",arr)

N = int(input("N:"))

arr = [int(N) for N in input("arr:").split()]

d = int(input("How many rotations:"))

leftrotate(arr,d,N)
