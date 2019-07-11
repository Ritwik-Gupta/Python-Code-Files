#python3.7

"""
def countZero(S):
    for n in S
        a=''
        oc=0
        ec=0
        while(n!=0):
            a+=str(n%2)
            n=int(n/2)
            if(a=='1'):
                oc+=1
        if(oc%2==0):
            ec+=1
        else:
            oc+=1
    return((ec,oc))

def countZero(S):
    ocount=0
    ecount=0
    for n in S:
        oc=0
        while(n!=0):
            a=n%2
            n=int(n/2)
            if(a==1):
                oc+=1
        if(oc%2==0):
            ecount+=1
        else:
            ocount+=1
    return((ecount,ocount))
"""

T = int(input())
S=[]

for i in range(T):
    N = int(input())
    for m in range(N):
        k=int(input())
        S.append(k)
        for j in range(len(S)-1):
            S.append(k^S[j])
        tupVal = countZero(S)
        alist.append(tupVal)
