#python3.7

N = input()

alist = []

for i in N:
    alist.append(i)

flag=0

for i in range(len(alist)):
    if(flag==0):
        if(i!=len(alist)-1):
            if(alist[i+1]>=alist[i]):
                pass
            else:
                alist[i]=str(int(alist[i])-1)
                flag=1
    else:
        alist[i]='9'

nStr = ''

for i in alist:
    nStr+=i

nStr = int(nStr)

print(nStr)
