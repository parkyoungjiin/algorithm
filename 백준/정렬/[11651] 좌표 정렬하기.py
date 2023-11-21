import sys
input = sys.stdin.readline

N = int(input())

# y좌표 기준 오름차순 정렬 , y가 같으면 x좌표 오름차순
li = []
for i in range(N):
    x, y = map(int,input().split())
    li.append([x,y])

li.sort(key=lambda x:(x[1], x[0]))

for i,j in li:
    print(i,j)