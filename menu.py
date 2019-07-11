#python3

menu=[]

i=1
while(i<=2048):
    menu.append(i)
    i=i*2

menu.sort(reverse=True)
t = int(input())

bill=[]
for i in range(t):
    x = int(input())
    bill.append(x)

items=[]
for i in range(len(bill)):
    total=0
    count=0
    for j in range(len(menu)):
        while(menu[j]<=bill[i] and total < bill[i]):
            total = total + menu[j]
            count = count + 1
    items.append(count)

for i in range(len(items)):
    print(items[i])
    
