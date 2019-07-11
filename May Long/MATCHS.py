#python3.7

T = int(input())
alist=[]

for i in range(T):
    N,M = [int(x) for x in input().split()]
    ctr=0                # 0 represents Ari's turn & 1 represents Rich's turn
    count=0
    while(N!=0 and M!=0):
        if(N>M):
            N = N%M
        elif(M>N):
            M = M%N
        else:
            N = N%M
        ctr=not(ctr)
    alist.append(ctr)
        
for i in alist:
    if(i==1):
        print("Ari")
    else:
        print("Rich")
