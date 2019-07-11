#python3

t = int(input())
flist=[]

for i in range(t):
    text = input()
    alist = list(text)
    for j in range(len(alist)-1):
        test = alist[j]
        atest = ord(test)
        for k in range(j+1, len(alist)):
            btest = ord(alist[k])
            diff = abs(atest-btest)
            if(diff==32):
                flist.append((test,))
