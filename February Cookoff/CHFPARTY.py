#python3.7

T = int(input())
blist=[]

for i in range(T):
    N = int(input())
    A = [int(N) for N in input().split()]
    A.sort()
    count=0
    for j in range(len(A)):
        if(count>=A[j]):
            count+=1
        else:
            blist.append(count)
            break
    if(count==N):
        blist.append(count)

for i in blist:
    print(i)
