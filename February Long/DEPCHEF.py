#python3.7

T = int(input())
blist=[]

for i in range(T):
    N = int(input())
    a = [int(N) for N in input().split()]
    d = [int(N) for N in input().split()]
    slist=[]
    result=[]
    for j in range(len(a)):
        if(j==len(a)-1):        #Exception for last element
            slist.append(d[j]-a[0]-a[j-1])
        else:
            slist.append(d[j]-a[j+1]-a[j-1])
    count=0
    for k in range(len(slist)):
        if(slist[k]>0):
            count+=1
    if(count==0):
        blist.append(-1)
    else:
        for k in range(len(slist)):
            if(slist[k]>0):
                result.append(d[k])
        blist.append(max(result))

for i in blist:
    print(i)
