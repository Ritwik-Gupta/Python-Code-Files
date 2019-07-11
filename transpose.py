#python3

def transpose(m):
    rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    a=[]
    for row in rez:
        a.append(row)
    print(a)

transpose([[1,2],[3,4],[5,6]])
