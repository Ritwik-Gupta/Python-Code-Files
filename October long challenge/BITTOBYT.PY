#python3.7

t = int(input())
b=[]

for i in range(t):
    n = int(input())
    a=[1,0,0]
    c=1
    while(True):
        if(n-2>0):
            n=n-2
            a[1]=a[1]+a[0]
            a[0]=0
        else:
            b.append(a)
            break
        if(n-8>0):
            n=n-8
            a[2]=a[2]+a[1]
            a[1]=0
        else:
            b.append(a)
            break
        if(n-16>0):
            n=n-16
            a[0]=a[0]+2*a[2]
            a[2]=0
        else:
            b.append(a)
            break

for i in b:
    print(' '.join(map(str, i)))

        
        
    
