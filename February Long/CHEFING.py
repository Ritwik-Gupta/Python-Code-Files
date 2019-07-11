#python3.7

T = int(input())
blist=[]

for i in range(T):
    N = int(input())
    count = 0
    flist=[]
    for j in range(N):
        text = input()
        ulist=[]
        if(j==0):
            first=text
        else:
