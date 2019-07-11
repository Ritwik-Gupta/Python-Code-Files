#python3

t = int(input())
a=[]

for i in range(t):
    p=int(input())
    c=5
    count=0
    while(p/c>=1):
        count+=int(p/c)
        c*=5
    a.append(count)

for i in range(len(a)):
    print(a[i])
