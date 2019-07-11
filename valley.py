#python3

def valley(a):
    l=len(a)
    if(l==0 or l==1 or l==2):
        return False
    else:
        for i in range(len(a)-1):
            if(a[i]>a[i+1]):
                continue
            else:
                v=i
                break
        flag=0
        for j in range(v,len(a)-1):
            if(a[j]<a[j+1]):
                flag=flag+1
            else:
                continue
        if(flag==j-v+1):
            return True
        else:
            return False

print(valley([2]))
