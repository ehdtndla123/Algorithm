
n,m=map(int,input().split())
numList=list(map(int,input().split()))

dp=[]
index=0
for i in range(n):
    dp.append(numList[index:index+m])
    index+=m

for j in range(1,m):
    up=0
    down=0
    zicsun=0
    for i in range(n):
        if i==0:
            up=0
        else:
            up=dp[i-1][j-1]
        if i==n-1:
            down=0
        else:
            donw=dp[i+1][j-1]
        zicsun=dp[i][j-1]

        dp[i][j]=dp[i][j]+max(up,down,zicsun)

result=0
for i in range(n):
    result=max(result,dp[i][m-1])

print(result)
