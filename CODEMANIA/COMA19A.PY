#python3.7

N,Q = [int(x) for x in input().split()]
count=0

for i in range(Q):
    t = int(input())
    if(N-t>=0):
        N=N-t
        count+=1

print(count)
