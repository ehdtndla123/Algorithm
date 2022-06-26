
#부품 찾기
n=int(input())

'''
def binary_serch(array,target,start,end):
    while start<=end:
        mid = (start + end) // 2
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
        return None
arr=list(map(int,input().split()))
arr.sort()
m=int(input())
arr2=list(map(int,input().split()))
for a in arr2:
    result=binary_serch(arr,a,0,n-1)
    if result!=None:
        print('yes')
    else:
        print('no')
'''
#떡볶이 떡 만들기
'''
n,m=map(int,input().split())
arr=list(map(int,input().split()))

arr.sort()
start=0
end=max(arr)
max=0
while start<=end:
    mid=(start+end)//2
    sum=0
    for a in arr:
        if a>mid:
            sum+=a-mid
    if sum>=m:
        start=mid+1
        if mid>=max:
            max=mid
    else:
         end=mid-1
print(max)
'''
