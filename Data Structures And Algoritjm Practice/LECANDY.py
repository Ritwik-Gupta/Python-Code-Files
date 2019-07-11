#python3.7

t = int(input())
blist=[]

for i in range(t):
    n,c = [int(x) for x in input().split()]
    A = [int(n) for n in input().split()]
    flag=0
    for i in range(n):
        if(c-A[i]>=0):
            c=c-A[i]
        else:
            blist.append("No")
            flag=1
            break
    if(i==n-1 and flag==0):
        blist.append("Yes")

for i in blist:
    print(i)
