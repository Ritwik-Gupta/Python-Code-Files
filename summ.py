#python3

t = int(input())
in_val=[]

for i in range(t):
    x=int(input())
    in_val.append(x)
    
op_val=[]
for i in range(t):
    summ=0
    p=in_val[i]
    while(p>0):
        y=p%10
        p=int(p/10)
        summ = summ + y
    op_val.append(summ)

for i in range(t):
    print("%d" %op_val[i])
