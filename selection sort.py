#python3
import random
def func1(a):
    for i in range(len(a)-1):
        mini=i
        for j in range(i+1,len(a)):
            if(a[j]<a[mini]):
                mini=j
        temp=a[i]
        a[i]=a[mini]
        a[mini]=temp
    print(a)

arr=[]
for i in range(10000):
    arr.append(random.randint(0,300))

print(arr)
print('\n')
func1(arr)

        
