#python3.7

T = int(input())
alist=[]

def fun(x,y):
    return(x+y+(x*y))

for i in range(T):
    N = int(input())
    val=0
    while(N>=0):
        if(val==0):
            val = fun(N,N-1)
            N-=2
        else:
            val = fun(N,val)
            N-=1
    alist.append(val)

for i in alist:
    print(i)
