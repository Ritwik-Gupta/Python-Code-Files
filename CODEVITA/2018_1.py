#python3.7

from itertools import product, starmap, islice

def findNeighbors(grid, x, y):
    xi = (0, -1, 1) if 0 < x < len(grid) - 1 else ((0, -1) if x > 0 else (0, 1))
    yi = (0, -1, 1) if 0 < y < len(grid[0]) - 1 else ((0, -1) if y > 0 else (0, 1))
    return islice(starmap((lambda a, b: grid[x + a][y + b]), product(xi, yi)), 1, None)

N, M = [int(x) for x in input().split()]

alist=[]

for i in range(N):
    blist = [int(M) for M in input().split()]
    alist.append(blist)


bDir={}

for i in range(len(alist)):  # i--> N
    for j in range(len(alist[i])):  # j--> M
        if(i!=0 or j!=0):
            if((alist[i][j]==1)):
                n = list(findNeighbors(alist, i, j))
                bDir[(i,j)]=sum(n)            
                

