#python3

def orangecap(d):
    maxs=0
    nd={}
    a=list(d.keys())
    for i in range(len(a)):
        b=list(d[a[i]].keys())
        for j in range(len(b)):
            maxp=b[j]
            maxs=d[a[i]][b[j]]
            if maxp in nd:
                nd[maxp]+=maxs
            else:
                nd[maxp]=maxs
    maxc=0
    for i in nd:
        if(nd[i]>maxc):
            maxc=nd[i]
            maxp=i
    return(maxp,maxc)
