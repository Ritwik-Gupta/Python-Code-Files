#python3

t = int(input())
alist=[]

for i in range(t):
    x = int(input())
    alist.append(x)

    
div=alist[0]
count=0
leng=0

for i in range(len(alist)):
    if(alist[i]%div==0):
        div=alist[i]
        leng+=1
print(leng)

        
