#python3

t = int(input())
t1=t
t2=t
t3=t
c1=0
c2=0
c3=0

while(t1>=0):
    if(t1%5==0):
        c1=t1/5
        break
    else:
        t1=t1-1
c1=int(c1/2)
        

while(t2>0):
    if(t2%10==0):
        c2=t2/10
        break
    else:
        t2=t2-1

while(t3>0):
    if(t3%25==0):
        c3=t3/25
        break
    else:
        t3=t3-1

        

total = c1+c2+c3

print(int(total))
