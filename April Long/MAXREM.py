#python3.7

N = int(input())

arr = [int(N) for N in input().split()]

arr.sort()

res=0

for i in range(len(arr)-1,1,-1):
    if(arr[i]!=arr[i-1]):
        res=arr[i-1]%arr[i]
        break
    else:
        pass

print(res)
