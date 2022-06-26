#특정 거리의 도시 찾기
n,m,k,x=map(int,input().split())
graph=[[] for i in range(n+1)]
visited=[False]*(n+1)
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)

result=[]
def dfs(graph,v,visited,cnt):
    visited[v]=True
    if cnt==x:
        result.append(v)
    for i in graph[v]:
        if not visited[i]:
            cnt+=1
            dfs(graph,i,visited,cnt)

