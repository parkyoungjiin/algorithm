import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [[False]*m for _ in range(n)]

def bfs(a, b):
    q = deque()
    q.append((a, b))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    result[nx][ny] = 0
                elif graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    result[nx][ny] = result[x][y] + 1
                    q.append((nx,ny))
            
graph = []
result = [[0]*m for _ in range(n)]

for _ in range(m):
    graph.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start_x, start_y = i,j

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

 
bfs(start_x, start_y)
print(result)
            
    

