#안테나

n=int(input())
an_list=list(map(int,input().split()))

an_list.sort()

# n이 짝수면 N//2 list[2] 0,1,2,3 list[n//2] or list[n//2 -1 ]
# n이 홀수면 N//2 list[1] 0,1,2 list[n//2]

def solve(index):
    target=an_list[index]
    sum=0
    for dis in an_list:
        if target<dis:
            sum+=(dis-target)
        else:
            sum+=(target-dis)
    return sum



result_index=0
if n%2==0:
    print(an_list[n//2]) if solve(n//2)<solve(n//2 -1) else print(an_list[n//2 - 1])
else:
    print(an_list[n//2])
