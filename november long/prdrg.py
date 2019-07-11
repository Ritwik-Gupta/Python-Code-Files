#python3.7

nlist = [n for n in input().split()]
alist=[]

t = int(nlist[0])
del(nlist[0])

for i in range(t):
    x = 2**int(nlist[i])
    alist.append('1')
    alist.append(str(x))

print((' ').join(alist))
