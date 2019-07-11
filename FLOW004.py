#python3.7

t = int(input())
a=[]

for i in range(t):
    count=0
    n = int(input())
    while(n>0):
        cd = n%10
        if(cd==4):
            count+=1
        n=n/10
    a.append(count)

for i in a:
    print(a)
