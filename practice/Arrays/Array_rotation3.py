#python3.7
import math

N = int(input("N:"))

arr = [int(N) for N in input("arr:").split()]

d = int(input("How many rotations:"))
g = math.gcd(N,d)

def rotate(arr,n,g):
    for i in range(g):
        temp=arr[i]
        k=i
        while(k+d<=n):
            arr[k]=arr[k+d]
            k+=d
        arr[k]=arr[i]
        print(arr)
    return(arr)        

"""
def rotate(arr,d,n):
    barr=[]
    if(d>n):
        d=d%n
        barr=arr[d:]
    else:
        barr=arr[d:]
    return(barr+arr[:d])
"""

print("The rotated array is:",rotate(arr,N,g))

