#특정 거리의 도시 찾기 bfs
from collections import deque
import sys
input=sys.stdin.readline
n,m,k,x=map(int,input().split())

graph=[[] for _ in range(n+1)]
queue=[]


for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)

queue=deque([x])
distance=[-1]*(n+1)
distance[x]=0

while queue:
    now=queue.popleft()

    for next in graph[now]:
        if distance[next]==-1:
            distance[next]=distance[now]+1
            queue.append(next)

flag=False

for i in range(1,n+1):
    if distance[i]==k:
        print(i)
        flag=True

if not flag:
    print(-1)
