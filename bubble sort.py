#python3
import random

def func1(a):
    x=len(a)
    y=len(a)
    for j in range(x):
        for i in range(y-1):
            if(a[i]>a[i+1]):
                (a[i],a[i+1])=(a[i+1],a[i])
        y-=1
    print(a)

b=[]
for i in range(10):
    b.append(random.randint(1,20))

print(b)
func1(b)
