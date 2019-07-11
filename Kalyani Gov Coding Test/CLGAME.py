#python3.7

T = int(input())

for i in range(T):
    N,K = [int(x) for x in input().split()]
    A = [int(N) for N in input().split()]
    X = [int(K) for K in input().split()]
    cscore=0
    gscore=0
    flag=0
    X.sort(reverse=True)
    while(len(A)>0):
        if(flag==0):         #Chef's turn
            for j in X:
                if(len(A)>=j):
                    for k in range(j):
                        cscore+=2**A[k]
                    for k in range(j):
                        del(A[k])
            flag=1
        else:
            for j in X:
                if(len(A)>=j):
                    for k in range(j):
                        gscore+=2**A[k]
                    for k in range(j):
                        del(A[k])
            flag=0
