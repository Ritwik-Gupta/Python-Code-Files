T = int(input())
blist=[]

for i in range(T):
    N, d = [int(x) for x in input().split()]
    flag=0
    while(flag==0):
        count=0
        alist=[]
        tempN = str(N*10 + d)
        for j in tempN:
            alist.append(j)
        for k in range(0,len(alist)-1):
            if(int(alist[k])>int(alist[k+1])):
                print(alist)
                del(alist[k])
                flag=0
                print(alist)
                break
            else:
                flag=1
                count+=1
                print("Count:",count)
        print("flag:",flag)
        N = int(('').join(alist))
        if(count==len(alist)-1):
            if(flag==0):
                blist.append(N)
                flag=1
            else:
                blist.append(int(('').join(alist[:-1])))
        print("while ran")
    
for i in blist:
    print(i)
