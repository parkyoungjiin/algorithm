import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

area = [list(map(int,input().split())) for _ in range(n)]

#최대 높이
max_height = max(map(max, area))
# 상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, height):
    queue = deque()
    queue.append((x,y))
    # 방문처리
    safe_area[x][y] = 1

    while queue:
        x,y = queue.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 방문했거나, 잠긴 곳인 경우
            if safe_area[nx][ny] == 1 or area[nx][ny] <= height:
                continue

            queue.append((nx,ny))
            safe_area[nx][ny] = 1
result = 0

for i in range(max_height):
    count = 0
    safe_area=[[0] * n for _ in range(n)]
    for a in range(n):
        for b in range(n):
            # i(높이) 가 더 크거나 같은 경우 -> 잠김(안전영역X)
            if area[a][b] > i and safe_area[a][b] == 0:
                bfs(a, b, i)
                count += 1
    result = max(result, count)
print(result)
    
    




    