import heapq
import sys

input = sys.stdin.readline

V,E=map(int,input().split())

graph=[[] for _ in range(V+1)]
visited=[False]*(V+1)
result=[]

for i in range(E):
    A,B,C=map(int,input().split())
    graph[A].append((B,C))
    graph[B].append((A,C))

def mst(start):
    queue=[(0,start)]

    while queue:
        dist,vertax=heapq.heappop(queue)
        if not visited[vertax]:
            visited[vertax]=True
            result.append(dist)

            for i in graph[vertax]:
                if not visited[i[0]]:
                    heapq.heappush(queue,(i[1],i[0]))


mst(1)
print(sum(result))
