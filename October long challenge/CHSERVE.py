#python3

t = int(input())        #1 is chef and 2 is cook
alist=[]

for i in range(t):
    p1, p2, k = [int(x) for x in input().split()]
    if((int((p1+p2)/k))%2==0):
        alist.append("CHEF")
    else:
        alist.append("COOK")

for i in alist:
    print(i)
