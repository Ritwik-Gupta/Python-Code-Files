#python3.7

T = int(input())
blist=[]
  
for i in range(T):
    N = int(input())
    vals = [int(N) for N in input().split()]
    plist=[]
    nlist=[]
    for j in vals:
        if(j<0):
            nlist.append(j)
        else:
            plist.append(j)
    if(len(plist)>len(nlist)):
        A=len(plist)
        B=len(nlist)
        if(B==0):
            B=A
    else:
        A=len(nlist)
        B=len(plist)
        if(B==0):
            B=A
    blist.append([A,B])

for i in blist:
    print(" ".join(str(x) for x in i))
