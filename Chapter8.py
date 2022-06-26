#1로만들기
'''
n=int(input())
dp=[0]*30001

for i in range(2,n+1):
    dp[i]=dp[i-1]+1
    if i%5==0:
        dp[i]=min(dp[i//5]+1,dp[i])
    if i%3==0:
        dp[i]=min(dp[i//3]+1,dp[i])
    if i%2==0:
        dp[i]=min(dp[i//2]+1,dp[i])
print(dp[n])
'''
#개미 전사
'''
n=int(input())
arr=list(map(int,input().split()))
dp=[0]*101
dp[0]=arr[0]
dp[1]=arr[1]
#1. dp[i]=dp[i-2]+arr[i]
#2. dp[i]=dp[i-3]+arr[i]
for i in range(3,n):
    print(i)
for i in range(3,n):
    dp[i]=arr[i]+max(dp[i-2],dp[i-3])
print(dp[n-1])
'''
#바닥 공사
'''
n=int(input())
dp=[0]*1001
dp[0]=1
dp[1]=3

for i in range(2,n+1):
    dp[i]=(dp[n-2]+2+dp[n-1])%796796

print(dp[n-1])
'''
#효율적인 화폐 구성
'''
n,m=map(int,input().split())
INF=10001
dp=[INF]*10001
coin=[]
dp[0]=0
for i in range(n):
    coin.append(int(input()))

for i in range(n):
    for j in range(coin[i],m+1):
        if dp[j-coin[i]]!=10001:
            dp[j]=min(dp[j],dp[j-coin[i]]+1)
if dp[m]==10001:
    print('-1')
else:
    print(dp[m])
'''
