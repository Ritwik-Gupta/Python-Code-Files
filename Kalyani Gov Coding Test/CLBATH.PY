#python3.7

T = int(input())
blist=[]

for i in range(T):
    v1,t1,v2,t2,v3,t3 = [int(x) for x in input().split()]
    t4 = (v1*t1+v2*t2)/(v1+v2)
    v4=v1+v2
    if(v1>=v3 and t1>=t3):
        blist.append("YES")
    elif(v2>=v3 and t2>=t3):
        blist.append("YES")
    elif(v4>=v3 and t4>=t3):
        blist.append("YES")
    else:
        blist.append("NO")

for i in blist:
    print(i)
    
