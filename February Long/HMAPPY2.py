#python3.7

T = int(input())
blist=[]
  
for i in range(T):
    N,A,B,K = [int(x) for x in input().split()]
    cA = int(N/A)
    cB = int(N/B)
    cAB = int(N/(A*B))
    if(A>=B):
        if(A%B==0):
            c1=0
            c2=cB-cA
        else:
            c1=cA-cAB
            c2=cB-cAB
    else:
        if(B%A==0):
            c1=cA-cB
            c2=0
        else:
            c1=cA-cAB
            c2=cB-cAB
    if(c1+c2>=K):
        blist.append('Win')
    else:
        blist.append('Lose')

for i in blist:
    print(i)
