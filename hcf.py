#python3

x, y = [int(x) for x in input().split()]
facx=[]
facy=[]

for i in range(1,x):
    if(x%i==0):
        facx.append(i)

for j in range(1,y):
    if(y%i==0):
        facy.append(j)

facx.sort(reverse=True)
facy.sort(reverse=True)
print(facx)
print(facy)

for i in range(len(facx)):
    for j in range(len(facy)):
        if(facx[i]==facy[j]):
            print(fac[i])
            break

        


