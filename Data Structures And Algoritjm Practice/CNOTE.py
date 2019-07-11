#python3.7

t = int(input())
blist=[]

for i in range(t):
    X,Y,K,N = input().split(" ")
    X = int(X)
    Y = int(Y)
    K = int(K)
    N = int(N)
    flag=0
    for j in range(N):
        P,C = input().split(" ")
        P = int(P)
        C = int(C)
        if(P+Y>=X and C<=K):
            blist.append("LuckyChef")
            flag=1
            break
        else:
            continue
    if(j==N-1 and flag==0):
        blist.append("UnluckyChef")

for i in blist:
    print(i)

