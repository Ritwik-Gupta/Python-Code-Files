#python3

t = int(input())
alist=[]

for i in range(t):
    n = int(input())
    songs = [int(n) for n in input().split()]
    upos = int(input())
    usong = songs[upos-1]
    songs.sort()
    for j in range(len(songs)):
        if(usong==songs[j]):
            alist.append(j+1)

for i in alist:
    print(i)
