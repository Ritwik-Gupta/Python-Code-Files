#python3

def descending(l):
    flag=0
    for i in range(len(l)-1):
        if(l[i]>=l[i+1]):
            flag=flag+1
        else:
            break
    if(len(l)==0):
        return True
    elif(flag==len(l)-1):
        return True
    else:
        return False
       
