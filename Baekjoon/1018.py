import sys
input=sys.stdin.readline

r,c=map(int,input().split())

map=[]
count=[]
for i in range(r):
    map.append(list(input().rstrip()))

def search_square(row,col):
    white=0
    black=0
    for i in range(row,row+8):
        for j in range(col,col+8):
            if (i+j)%2==0:
                if map[i][j]!='W':
                    white+=1
                if map[i][j]!='B':
                    black+=1
            else:
                if map[i][j]!='B':
                    white+=1
                if map[i][j]!='W':
                    black+=1
    count.append(min(white,black))

                

def solve(row,col):
    for i in range(row-7):
        for j in range(col-7):
            search_square(i,j)


solve(r,c)
print(min(count))
