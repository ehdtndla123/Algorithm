
import sys
input=sys.stdin.readline


N=int(input())
rgb=[]
#빨 초 파 
for i in range(N):
    rgb.append(list(map(int,input().split())))

dp=[[0]*3  for i in range(N)]

dp[0][0]=rgb[0][0]
dp[0][1]=rgb[0][1]
dp[0][2]=rgb[0][2]

for i in range(1,N):
    dp[i][0]=rgb[i][0]+min(dp[i-1][1],dp[i-1][2])
    dp[i][1]=rgb[i][1]+min(dp[i-1][0],dp[i-1][2])
    dp[i][2]=rgb[i][2]+min(dp[i-1][1],dp[i-1][0])
print(min(dp[N-1]))
