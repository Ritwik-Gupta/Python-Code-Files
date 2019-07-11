#python3
import random
x, y = [int(x) for x in input().split()]

result = x-y
a=[]
f=0

while(result>0):
    rem=result%10
    result=int(result/10)
    a.append(rem)
a.reverse()

for i in range(len(a)):
    n=random.randint(1,9)
    if(f==0):
        if(a[i]!=n):
            a[i]=n
            f=1
    else:
        continue

num=0
for i in range(len(a)):
    c=len(a)-(i+1)
    num = num + a[i]*(10**c)

print(num)
        
