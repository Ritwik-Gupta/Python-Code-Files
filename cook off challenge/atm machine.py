#python3

t = int(input())
c=[]

for i in range(t):
    n, k = [int(k) for k in input().split()]
    a = [int(n) for n in input().split()]
    b=[]
    for j in range(n):
        if(k-a[j]>=0):
            b.append('1')
            k=k-a[j]
        else:
            b.append('0')
    f=('').join(b)
    c.append(f)

for i in range(len(c)):
    print((c[i]))
