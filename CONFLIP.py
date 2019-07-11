#python3

t = int(input())
flist=[]

for i in range(t):
    g = int(input())
    for j in range(g):
        i, n, q = [int(i) for i in input().split()]
        alist=[]
        nohs=0
        nots=0
        if(i==1):
            for p in range(n):
                alist.append(0)
        elif(i==2):
            for p in range(n):
                alist.append(1)
        #At the end of all rounds
        for k in range(n):
            v=n-k
            if(v%2==0):
                continue
            else:
                if(alist[k]==0):
                    alist[k]=1
                elif(alist[k]==1):
                    alist[k]=0
        for m in alist:
            if(m==0):
                nohs+=1
            elif(m==1):
                nots+=1
        if(q==1):
            flist.append(nohs)
        elif(q==2):
            flist.append(nots)

for i in flist:
    print(i)
