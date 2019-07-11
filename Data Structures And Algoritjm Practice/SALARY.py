#python3.7

t = int(input())
blist=[]

for i in range(t):
    N = int(input())
    W = [int(N) for N in input().split()]
    count=0
    while(W.count(max(W))!=len(W)):
        maxNum = max(W)
        maxInd = W.index(max(W))
        for i in range(len(W)):
            if(i != maxInd):
                W[i]+=1
        count+=1
    blist.append(count)

for i in blist:
    print(i)
