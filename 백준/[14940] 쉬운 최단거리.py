import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j):
    visited = [[0] * m for _ in range(n)]
    dist = [[0] * m for _ in range(n)]
    q = deque()
    q.append((i, j))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and graph[nx][ny] == 1:
                    visited[nx][ny] = 1
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx,ny))

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and dist[i][j] == 0:
                print(-1, end=' ')
            else:
                print(dist[i][j], end=' ')
        print()   

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            bfs(i, j)

    

