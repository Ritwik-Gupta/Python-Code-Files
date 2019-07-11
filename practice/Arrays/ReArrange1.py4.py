#python3.7

N = int(input("N:"))

arr = [int(N) for N in input('arr:').split()]

for i,j in enumerate(arr):
    if(j==-1):
        pass
    elif(j==i):
        pass
    else:
        if(arr[j]==-1):
            arr[j]=j
        else:
            y=arr[j]
            arr[j]=j
            arr[y]=y

for i,j in enumerate(arr):
    if(arr[i]!=-1 and arr[i]!=i):
        arr[i]=-1

print(arr)

        
