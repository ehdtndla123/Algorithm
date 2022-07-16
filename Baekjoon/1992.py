import sys
input=sys.stdin.readline

N=int(input())
map=[]
for i in range(N):
    map.append(input().rstrip())

str=""
def devide(x,y,n):
    global str
    check=map[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if map[i][j]!=check:
                check=2
    n=n//2
    if check==2:
        str+="("
        devide(x,y,n)
        devide(x,y+n,n)
        devide(x+n,y,n)
        devide(x+n,y+n,n)
        str+=")"
    else:
        str+=check
devide(0,0,N)
print(str)
