#python3.7
from itertools import combinations

T = int(input())
blist=[]

for i in range(T):
    N = int(input())
    a=[]
    a1=[]
    b=[]
    count=0
    for j in range(N):
        a.append(input())
    b = list(combinations(range(1,N+1),2))
    for j in b:
        tempDir={'a':0,'e':0,'i':0,'o':0,'u':0}
        tempStr = a[j[0]-1]+a[j[1]-1]
        for m in tempStr:
            if(m in tempDir):
                tempDir[m]+=1
        if(tempDir['a']>0 and tempDir['e']>0 and tempDir['i']>0 and tempDir['o']>0 and tempDir['u']>0):
            count+=1
    blist.append(count)

for i in blist:
    print(i)
