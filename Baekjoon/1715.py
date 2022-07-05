#카드 정렬하기
import heapq
n=int(input())
card=[]
for i in range(n):
    heapq.heappush(card,int(input()))

result=0
while len(card)!=1:
    n1=heapq.heappop(card)
    result+=n1
    n2=heapq.heappop(card)
    result+=n2
    heapq.heappush(card,n1+n2)
print(result)
