#python3

t = int(input())
ans=[]

for i in range(t):
    n = int(input())
    vals = [int(n) for n in input().split()]
    mini = abs(vals[1]-vals[0])
    for j in range(len(vals)-1):
        for k in range(j+1, len(vals)):
            dif=abs(vals[j]-vals[k])
            if(dif<mini):
                mini=dif
            else:
                continue
    ans.append(mini)

for i in ans:
    print(i)
