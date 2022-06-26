from collections import deque

#DFS 메서드 정의
'''
def dfs(graph,v,visited):
    visited[v]=True
    print(v,end='')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited=[False]*9

dfs(graph,1,visited)
'''
#BFS 메서드 정의
'''
def bfs(graph,start,visited):
    queue=deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited=[False]*9

bfs(graph,1,visited)
'''
#음료수 얼려 먹기
'''
n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(y,x):
    if y<=-1 or y>=n or x<=-1 or x>=m:
        return False
    if graph[y][x]==0:
        graph[y][x]=1
        dfs(y-1,x)
        dfs(y,x-1)
        dfs(y+1,x)
        dfs(y,x+1)
        return True
    return False

result=0

for i in range(n):
    for j in range(m):
        if(dfs(i,j)==True):
            result+=1
print(result)
'''
#미로 탈출
'''
n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(y,x):
    queue=deque()
    queue.append((y,x))
    while queue:
        y,x=queue.popleft()
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if ny <= -1 or ny >= n or nx <= -1 or nx >= m:
                continue
            if graph[ny][nx]==0:
                continue
            if graph[ny][nx]==1:
                graph[ny][nx]+=graph[y][x]
                queue.append([ny,nx])
    return graph[n-1][m-1]
print(bfs(0,0))
'''