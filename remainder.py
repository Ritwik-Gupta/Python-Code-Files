#python3

t = int(input())
res=[]

for i in range(t):
    x, y = [int(x) for x in input().split()]
    r = x%y
    res.append(r)

for i in range(len(res)):
    print(res[i])
    
