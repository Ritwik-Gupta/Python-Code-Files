#python3.7

t = int(input())
ans=[]

for i in range(t):
    n = int(input())
    size=0
    a=n
    b=n
    revNum=0
    while(a>0):
        a=int(a/10)
        size+=1
    while(b>0):
        ld = int(b%10)
        revNum = revNum + ld*(10**(size-1))
        size-=1
        b=int(b/10)
    ans.append(revNum)
       
        
for i in ans:
    print(i)
    
