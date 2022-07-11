import sys
input=sys.stdin.readline
import bisect
n=int(input())
number=list(map(int,input().split()))
dp=[number[0]]

for i in range(n):
    if number[i]>dp[-1]:
        dp.append(number[i])
    else:
        idx=bisect.bisect_left(dp,number[i])
        dp[idx]=number[i]
print(len(dp))
