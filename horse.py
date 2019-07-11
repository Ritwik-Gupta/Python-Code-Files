#python3
import re

t = int(input())
a=[]
b=[]

for i in range(t):
    s=int(input())
    p = input()
    testReg = re.compile(r'\d+')
    a = testReg.findall(p)
    for i in range(len(a)):
        a[i] = int(a[i])
    mini=abs(a[0]-a[1])
    for k in range(len(a)-1):
        for j in range(k+1, len(a)):
            if(abs(a[k]-a[j])<mini):
                mini = abs(a[k]-a[j])
    b.append(mini)

for i in b:
    print(i)
