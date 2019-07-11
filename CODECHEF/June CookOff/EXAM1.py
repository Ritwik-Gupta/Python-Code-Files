#python3.7

T = int(input())
alist=[]

for i in range(T):
    N = int(input())
    S = input()
    U = input()
    point=0
    prev=0
    for j in range(N):
        if(prev==0):
            if(U[j]==S[j]):
                point+=1
                prev=0
            elif(U[j]=='N'):
                prev=0
            else:
                prev=1
        else:
            prev=0
    alist.append(point)

for i in alist:
    print(i)
