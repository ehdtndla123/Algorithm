#고정점 찾기

n=int(input())
number=list(map(int,input().split()))

print(type(number[0]))
def binary_search(number,first,last):
    if(first>last):
        return None
    mid=(first+last)//2

    if(number[mid]==mid):
        return mid
    elif number[mid]<mid:
        return binary_search(number,mid+1,last)
    else:
        return binary_search(number,first,mid-1)
    return -1;

if(binary_search(number,0,n)==None):
    print('-1')
else:
    print(binary_search(number,0,n))
