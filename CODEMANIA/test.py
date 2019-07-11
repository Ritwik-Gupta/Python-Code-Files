#python3.7

N = int(input())

arr = [int(N) for N in input().split()]

dir1={}
count=0
for i in arr:
    if(i in dir1):
        dir1[i]+=1
    else:
        dir1[i]=1

for i in dir1:
    count+=int(dir1[i]/2)

