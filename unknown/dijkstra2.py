import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)
n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
distance=[INF]*(n+1)
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

start=1
dijkstra(start)

max_node=0

max_distance=0

result=[]

for i in range(1,n+1):
    if max_distance<distance[i]:
        max_distance=distance[i]
        max_node=i
        result=[max_node]
    elif max_distance == distance[i]:
        result.append(i)


print(min(result),max_distance,len(result))
