#서로소 집합 알고리즘
'''
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]
def union(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v,e=map(int,input().split())
parent=[0]*(v+1)

for i in range(1,v+1):
    parent[i]=i

for i in range(e):
    a,b=map(int,input().split())
    union(parent,a,b)

print('각 원소가 속한 집합:',end=' ')
for i in range(1,v+1):
    print(find_parent(parent,i),end=' ')

print()

print('부모 테이블: ',end=' ')
for i in range(1,v+1):
    print(parent[i],end=' ')
'''
#서로소 집합을 활용한 사이클 판별 소스코드
'''
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]
def union(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v,e=map(int,input().split())
parent=[0]*(v+1)

for i in range(1,v+1):
    parent[i]=i

cycle=False

for i in range(e):
    a,b=map(int,input().split())
    if find_parent(parent,a)==find_parent(parent,b):
        cycle=True
        break
    else:
        union(parent,a,b)
if cycle:
    print("사이클이 발생했습니다")
else:
    print("사이클이 발생하지 않았습니다")
'''
#크루스칼 알고리즘
'''
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]
def union(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v,e=map(int,input().split())
parent=[0]*(v+1)

edges=[]
result=0

for i in range(1,v+1):
    parent[i]=i

for _ in range(e):
    a,b,cost=map(int,input().split())
    edges.append((cost,a,b))

edges.sort()

for edge in edges:
    cost,a,b=edge

    if find_parent(parent,a)!=find_parent(parent,b):
        union(parent,a,b)
        result+=cost

print(result)
'''
#위상 정렬
'''
from collections import deque

v,e=map(int,input().split())

indegree=[0]*(v+1)

graph=[[] for i in range(v+1)]

for _ in range(e):
    a,b=map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1

def toplogy_sort():
    result=[]
    q=deque()

    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)

    while q:
        now=q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
    for i in result:
        print(i,end=' ')
toplogy_sort()
'''
#팀 결성
'''
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]
def union(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

n,m=map(int,input().split())
parent=[0]*(n+1)

for i in range(1,n+1):
    parent[i]=i

for i in range(m):
    number,a,b=map(int,input().split())
    if number==0:
        union(parent,a,b)
    else:
        if find_parent(parent,a)==find_parent(parent,b):
            print('YES')
        else:
            print('NO')
'''
#도시 분할 계획
'''
from collections import deque
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]
def union(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
n,m=map(int,input().split())

parent=[0]*(n+1)
for i in range(1,n+1):
    parent[i]=i

edges=[]
for i in range(m):
    a,b,c=map(int,input().split())
    edges.append((c,a,b))

edges.sort()
result=0
last=0
for edge in edges:
    c,a,b=edge

    if find_parent(parent,a)!=find_parent(parent,b):
        union(parent,a,b)
        result+=c
        last=c
result-=last
print(result)
'''
#커리큘럼
from collections import deque
n=int(input())
indigree=[0]*(n+1)
graph=[[] for i in range(n+1)]
time=[0]*(n+1)
for i in range(1,n+1):
    data=list(map(int,input().split()))
    time[i]=data[0]
    if len(data)!=2:
        for j in range(1,len(data)-1):
            graph[i].append(data[j])
            indigree[data[j]]+=1

result=[0]*(n+1)
def topology_sort():

    q=deque()


    for i in range(1,n+1):
         if indigree[i]==0:
             q.append(i)

    while q:
        now=q.popleft()

        for i in graph[now]:
            indigree[i]-=1
            if indigree[i]==0:
                q.append(i)


topology_sort()
for i in range(1,n+1):
    print(result[i])





