#python3

t = int(input())
plist=[]

for i in range(t):
    n, m = [int(n) for n in input().split()]
    d_jobs = [int(m) for m in input().split()]
    l_jobs=[]
    cwork=[]
    awork=[]
    for j in range(1,n+1):
        if(j not in d_jobs):
            l_jobs.append(j)
        else:
            continue
    check=0
    for k in l_jobs:
        if(check==0):
            cwork.append(k)
            check=1
        elif(check==1):
            awork.append(k)
            check=0
    #print(' '.join(map(str, cwork)))
    #print(' '.join(map(str, awork)))
    plist.append((cwork,awork))

for i in plist:
    print(' '.join(map(str, i[0])))
    print(' '.join(map(str, i[1])))
    
