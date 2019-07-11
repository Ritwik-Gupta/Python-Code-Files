#python3.7

T = int(input())
blist=[]

for i in range(T):
    N, B = [int(x) for x in input().split()]
    area=[]
    count=0
    for j in range(N):
        W,H,P = [int(x) for x in input().split()]
        if(B>=P):
            area.append(W*H)
        else:
            count+=1
    if(count==N):
        blist.append("no tablet")
    else:
        blist.append(max(area))

for i in blist:
    print(i)
