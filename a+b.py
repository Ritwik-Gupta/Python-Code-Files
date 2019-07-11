#python3

t = int(input())
p1=[]
p2=[]

for i in range(t):
    x, y = [int(x) for x in input().split()]
    p1.append(x)
    p2.append(y)

win1=[]
win2=[]

for i in range(t):
    if(p1[i]>p2[i]):
        x = p1[i]-p2[i]
        win1.append(x)
    else:
        x = p2[i]-p1[i]
        win2.append(x)

res1=max(win1)
res2=max(win2)

if(res1>res2):
    print(1,"%d"%res1)
else:
    print(2,"%d"%res2)
