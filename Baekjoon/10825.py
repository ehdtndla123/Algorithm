#국영수

n=int(input())
people=[]
for i in range(n):
    people.append(input().split())
people=sorted(people,key=lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for i in range(n):
    print(people[i][0])
