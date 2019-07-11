#python3.8

T = int(input())
alist=[]

for i in range(T):
    N = int(input())
    arr = [int(N) for N in input().split()]
    mean=float(sum(arr)/N)
    count=0
    for p,j in enumerate(arr):
        if(j==mean):
            x=p+1
            break
        else:
            pass
    if(p==len(arr)-1):
        alist.append('Impossible')
    else:
        alist.append(x)

for i in alist:
    print(i)
