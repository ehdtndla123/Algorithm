import sys
from collections import deque
from tabnanny import check
input=sys.stdin.readline

#N값
n=int(input())

queen_list=[]
queen_list=deque(queen_list)

def check(x,y):
    for qx,qy in queen_list:
        if qy==y:
            return False
        if abs(qx-x)==abs(qy-y):
            return False
    return True

count=0
def queen3(x,y):
    #다 돌았을경우
    if x==n:
        global count
        count=count+1
        return
    for j in range(n):
        if check(x,j):
            queen_list.append((x,j))
            queen3(x+1,j)
            queen_list.pop()

queen3(0,0)

print(count)
