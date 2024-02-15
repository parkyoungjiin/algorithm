from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())
tomato = []
for _ in range(h):
    tomato.append([list(map(int, input().split())) for _ in range(n)])

# 좌표 (6방향)
dr = [1, 0, -1, 0, 0, 0]
dc = [0, 1, 0, -1, 0, 0]
# 위, 아래에 대한 좌표
dx = [0, 0, 0, 0, 1, -1]

q = deque()
# 익은 토마토 위치 확인
for x in range(h):
    for i in range(n):
        for j in range(m):
            if tomato[x][i][j] == 1:
                q.append([x,i,j])
print(q)
while q:
    x,r,c = q.popleft()
    
    for i in range(6):
        nx = x + dx[i]
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nx < h and 0 <= nr < n and 0 <= nc < m:
            if tomato[nx][nr][nc] == 0:
                q.append([nx,nr,nc])
                tomato[nx][nr][nc] = tomato[x][r][c] + 1




