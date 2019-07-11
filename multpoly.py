#python3

def multpoly(p1,p2):
    d={}
    a=[]
    for i in range(len(p1)):
        for j in range(len(p2)):
            c=p1[i][0]*p2[j][0]
            e=p1[i][1]+p2[j][1]
            if e not in list(d.keys()):
                d[e]=c
            else:
                d[e] = d[e] + c
    p1=list(d.keys())
    for i in p1:
        if(d[i]!=0):
            a.append((d[i],i))
    print(a)
