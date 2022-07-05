#경쟁적 전염 bfs
import sys
input = sys.stdin.readline
from collections import deque
n,k=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))
target_time,target_x,target_y=map(int,input().split())

queue=[]

for i in range(n):
    for j in range(n):
        if graph[i][j]!=0:
            queue.append((graph[i][j],i,j,0))
queue.sort()
queue=deque(queue)

dx=[-1,0,1,0]
dy=[0,1,0,-1]

while queue:
    position,x,y,time=queue.popleft()
    if time==target_time:
        break
    for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y
        if  0<= nx < n and 0 <= ny < n :
            if graph[nx][ny]==0:
                graph[nx][ny]=position
                queue.append((position,nx,ny,time+1))
print(graph[target_x-1][target_y-1])
