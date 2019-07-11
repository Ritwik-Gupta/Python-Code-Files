#python3
import random

x, y = [int(x) for x in input().split()]

p = x-y
a=[]

while(p>0):
    d=p%10
    p=int(p/10)
    a.append(d)

a.reverse()
print(a)

a2=[]
a2.append(random.randint(1,9))

for i in range(1,len(a)):
    a2.append(a[i])

print(a2)
