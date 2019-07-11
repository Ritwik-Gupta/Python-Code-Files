#python3.7

T = int(input())

alist=[]

for i in range(T):
    G = int(input())
    for j in range(G):
        I,N,Q = [int(x) for x in input().split()]
        arr=[]
        for p in range(N):
            if(I==1):
                arr.append(1)
            else:
                arr.append(2)
        for p in range(N):
            l=N+1-p
            if(p%2!=0):
                pass
            else:
                if(arr[p]==1):
                    arr[p]=2
                else:
                    arr[p]=1
        #print('arr',arr)
        hcount=0
        tcount=0
        for p in arr:
            if(p==1):
                hcount+=1
            else:
                tcount+=1
        #print("hcount",hcount)
        #print("tcount",tcount)
        if(Q==1):
            alist.append(hcount)
        else:
            alist.append(tcount)

for i in alist:
    print(i)
