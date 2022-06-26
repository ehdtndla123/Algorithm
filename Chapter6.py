
#선택정렬
'''
array=[7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index=i
    for j in range(i+1,len(array)):
        if array[min_index]>array[j]:
            min_index=j
    array[min_index],array[i]=array[i],array[min_index]
print(array)
'''
#삽입정렬
'''
array=[7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j]<array[j-1]:
            array[j],array[j-1]=array[j-1],array[j]
        else:
            break
print(array)
'''
#퀵 정렬
'''
array=[7,5,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):
    if start>=end:
        return
    pivot=start
    left=start+1
    right=end
    while left<=right:
        while left <= end and array[left]<=array[pivot]:
            left+=1
        while right>start and array[right]>array[pivot]:
            right-=1
        if left>right:
            array[right],array[pivot]=array[pivot],array[right]
        else:
            array[left], array[right] = array[right],array[left]
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)
print(array)
'''
#계수 정렬
'''
array=[7,5,9,0,3,1,6,2,4,8]
count=[0]*(max(array)+1)

for i in range(len(array)):
    count[array[i]]+=1
for i in range(len(count)):
    for j in range(count[i]):
        print(i,end=' ')
'''
#위에서 아래로
'''
n=int(input())
array=[]
for i in range(n):
    array.append(int(input()))
array=sorted(array,reverse=True)

for i in array:
    print(i,end=' ')
'''
#성적이 낮은 순서로 학생 출력하기
'''
n=int(input())
array=[]
for i in range(n):
    input_data=input().split()
    array.append((input_data[0],int(input_data[1])))

array=sorted(array,key=lambda x: x[1])
for i in array:
    print(i[0],end=' ')
'''
#두 배열의 원소 교체
'''
n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a=sorted(a)
b=sorted(b,reverse=True)
cnt=0
for i in range(n):
    if cnt==k:
        break
    if a[i]<b[i]:
        cnt+=1
        a[i]=b[i]
print(sum(a))
'''

