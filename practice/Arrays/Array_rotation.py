#python3.7

N = int(input("N:"))

arr = [int(N) for N in input("arr:").split()]

def rotate(arr,d,n):
    barr=[]
    if(d>n):
        d=d%n
        barr=arr[d:]
    else:
        barr=arr[d:]
    return(barr+arr[:d])

d = int(input("How many rotations:"))

print("The rotated array is:",rotate(arr,d,N))
