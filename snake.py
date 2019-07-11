#python3

t = int(input())

for i in range(t):
    p=int(input())
    s=input()
    a=[]
    c=0
    c1=0
    for j in s:
        if(j=='.'):
            c+=1
            continue
        elif(j=='H' or j=='T'):
            a.append(j)
            c+=1
    f=a[0]
    if(len(a)==0):
        print("valid")
    else:
        if(a[0]!='H' and a[-1]!='T'):
            print("Invalid")
        else:
            for k in range(1,len(a)):
                if(a[k]==f):
                    print("Invalid")
                    break
                else:
                    f=a[k]
                    c1+=1
        if(c1==len(a)-1):
            print("Valid")
