from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    global cnt
    q.append((x, y))
    while q:
        qx, qy = q.popleft()
        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]

            if 0 <= nx < n and 0<= ny < m:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    cnt += 1
                    q.append((nx,ny))


n, m, k = map(int, input().split())
result = 0
graph = [[0] * (m) for _ in range(n)]
visited=[[False] * (m) for _ in range(n)]
q = deque()
for _ in range(k):
    r, c = map(int,input().split())
    graph[r-1][c-1] = 1


dx = [1, -1, 0, 0]
dy = [0 ,0, 1, -1]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt = 0
            bfs(i,j)
            result = max(result, cnt)

print(result)