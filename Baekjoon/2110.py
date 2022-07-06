#공유기 설치
import sys
input=sys.stdin.readline


n,c=map(int,input().split())
num_list=[]
for i in range(n):
    num_list.append(int(input()))

num_list.sort()
left=1
right=num_list[-1]-num_list[0]
result=[]
while left<=right:
    mid=(left+right)//2

    count=1
    gong=min(num_list)+mid

    for i in range(1,n):
        if gong<=num_list[i]:
            count+=1
            gong=num_list[i]+mid

    if count>=c:
        left=mid+1
        result.append(mid)
    else:
        right=mid-1


print(max(result))
