#python 3.7

T = int(input())
alist=[]

for i in range(T):
    N = int(input())
    S = [int(N) for N in input().split()]
    S.reverse()
    blist=[]
    for j in range(N-1,-1,-1):
        for k in range(N):
            val = S[k]-S[j]
            if(val<0):
                blist.append(j-k)
                break
            elif(val==0 and j!=k):
                blist.append(j-k-1)
                break
            elif(j==k):
                blist.append(0)
                break
            else:
                continue
    alist.append(blist)

for i in alist:
    print(" ".join(str(x) for x in i))
