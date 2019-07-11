#python3.7

T = int(input())
blist=[]

for i in range(T):
    X, Y = [int(x) for x in input().split()]
    mwon=2
    mdraw=1
    for j in range(0,Y+1):
        tpoint=mdraw*(Y-j)+mwon*j
        if(tpoint>=X):
            blist.append(j)
            break

for i in blist:
    print(i)
