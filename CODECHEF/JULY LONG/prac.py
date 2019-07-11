#python3.7

T = int(input())
alist=[]

for i in range(T):
    N = input()
    if(len(N)==10):
        alist.append('true')
    elif(len(N)==11):
        if(N[0]=='0'):
            alist.append('true')
        else:
            alist.append('false')
    elif(len(N)==13):
        if(N[0:3]=='+91'):
            alist.append('true')
        else:
            alist.append('false')
    elif(len(N)==3 or len(N)==4):
        alist.append('true')
    else:
        alist.append('false')

for i in alist:
    print(i)
