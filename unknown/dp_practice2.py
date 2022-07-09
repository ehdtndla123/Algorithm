n=int(input())
dp=[]
for i in range(n):
    dp.append(list(map(int,input().split())))

for i in range(1,n):
    dp[i][0]+=dp[i-1][0]
    dp[i][i]+=dp[i-1][i-1]

if n>2:
    for i in range(2,n):
        for j in range(1,i):
            dp[i][j]=dp[i][j]+max(dp[i-1][j-1],dp[i-1][j])

result=0
for i in range(n):
    result=max(result,dp[n-1][i])

print(result)
