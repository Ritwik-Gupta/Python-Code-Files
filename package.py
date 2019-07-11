#python3

t = int(input())
cakes=[]

for i in range(t):
    x=int(input())
    cakes.append(x)

package=[]
for i in range(len(cakes)):
    y = int(cakes[i]/2) + 1
    package.append(y)

for i in range(len(package)):
    print(package[i])
