#python3.7

import random
alist=[]

for i in range(300):
    alist.append(random.randint(1,1000))

alist.sort()

mid = int(len(alist)/2)

print("enter number to search:")
x = int(input())

def binSearch(mid,alist):
    if(x==alist[mid]):
        return("Found at index", mid)
    elif(x>alist[mid]):
        binSearch(int(len(alist[mid:])/2),alist[mid:])
    elif(x<alist[mid]):
        binSearch(int(len(alist[:mid])/2),alist[:mid])
    else:
        return("Not Found")
    
binSearch(mid,alist)
