#python3.7

t = int(input())
a=[]

for i in range(t):
    count=0
    n = int(input())
    while(n>0):
        if(int(n%10)==4):
            count+=1
        n=int(n/10)
    a.append(count)

for i in a:
    print(i)
