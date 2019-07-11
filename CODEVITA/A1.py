#python3.7

N = int(input())

inArr = input().split(" ")
outArr = []

myDir = {'A':'0','B':'1','C':'2','D':'3','E':'4','F':'5','G':'6','H':'7','I':'8','J':'9'}
val=0

for i in inArr:
    tStr=''
    flag=0
    for j in range(len(i)):
        if(flag==0):
            if(i[j]=='J' and j!=len(i)-1):
                if(i[j+1]=='A'):
                    tStr += '00'
                    flag=1
                else:
                    tStr += myDir[i[j]]
            elif(i[j]=='T' and j!=len(i)-1):
                if(i[j+1]=='A'):
                    tStr += '11'
                    flag=1
                else:
                    tStr += myDir[i[j]]
            elif(i[j]=='H' and j!=len(i)-1):
                if(i[j+1]=='A'):
                    tStr += '22'
                    flag=1
                else:
                    tStr += myDir[i[j]]
            elif(i[j]=='G' and j!=len(i)-1):
                if(i[j+1]=='A'):
                    tStr += '33'
                    flag=1
                else:
                    tStr += myDir[i[j]]
            elif(i[j]=='F' and j!=len(i)-1):
                if(i[j+1]=='A'):
                    tStr += '44'
                    flag=1
                else:
                    tSt += myDir[i[j]]
            else:
                tStr += myDir[i[j]]
        else:
            flag=0
    val += int(tStr)

P = int(input())

if(P<val):
    print("GREEDY")
else:
    print("INNOCENT")
