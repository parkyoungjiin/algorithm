import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

# graph = [[False] * (m+1) for _ in range(n+1)]
graph = [list(map(int,input().split())) for _ in range(n)]
print(graph)
visited = [False] * (n+1)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# bfs
def bfs(graph, a, b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0
    count = 1
    # queue가 빌때까지
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 이동하려는 좌표가 범위를 벗어난 경우 밑의 if를 거치지 않음.
            if nx < 0 or nx >= n or ny < 0 or ny >=m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count

paint = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            paint.append(bfs(graph, i, j))
        
if len(paint) == 0:
    print(len(paint))
    print(0)
else:
    print(len(paint))
    print(max(paint))




    