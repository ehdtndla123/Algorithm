
import sys
input=sys.stdin.readline

N=int(input())

number=list(map(int,input().split()))

dp=[0]*(N+1)
dp[0]=number[0]
present=number[0]

for i in range(1,N):
    if present<=0:
        present=0
    present+=number[i]
    dp[i]=max(dp[i-1],present)

print(dp[N-1])
