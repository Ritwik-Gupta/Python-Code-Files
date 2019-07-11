#python3

def addpoly(p1,p2):
    d={}
    a=[]
    for i in range(len(p1)):
        d[p1[i][1]] = p1[i][0]
    for j in range(len(p2)):
        if p2[j][1] in d:
            d[p2[j][1]] += p2[j][0]
        else:
            d[p2[j][1]] = p2[j][0]
    for i in list(d.keys()):
        if(d[i]!=0):
            a.append((d[i],i))
    a.sort()
    return(a)
