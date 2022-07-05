#감시 피하기 bfs
from itertools import combinations
n=int(input())
graph=[]
teacher=[]
blank=[]

for i in range (n):
    graph.append(list(input().split()))
    for j in range(n):
        if graph[i][j]=="T":
            teacher.append((i,j))
        elif graph[i][j]=="X":
            blank.append((i,j))



def checked(x,y,direction):
    if direction==0:
        while y>=0:
            if graph[x][y]=='S':
                return True
            if graph[x][y]=='O':
                return False
            y-=1

    if direction==1:
        while y<n:
            if graph[x][y]=='S':
                return True
            if graph[x][y]=='O':
                return False
            y+=1

    if direction==2:
        while x>=0:
            if graph[x][y]=='S':
                return True
            if graph[x][y]=='O':
                return False
            x-=1

    if direction==3:
        while x<n:
            if graph[x][y]=='S':
                return True
            if graph[x][y]=='O':
                return False
            x+=1
    return False

def process():
    for x,y in teacher:
        for i in range(4):
            if(checked(x,y,i)):
                return True
    return False

find=False

for data in combinations(blank,3):

    for x,y in data:
        graph[x][y]='O'
    if not process():
        find=True
        break
    for x,y in data:
        graph[x][y]='X'

if find:
    print('YES')
else:
    print('NO')
