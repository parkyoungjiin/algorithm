import sys
from collections import deque
input = sys.stdin.readline

    

def bfs(a,b):
    queue = deque([])
    queue.append((a, b))
    # 방문처리
    field[a][b] == 0
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 범위 내, 방문 X 
            if 0 <= nr < n and 0 <= nc < m and field[nr][nc] == 1:
                queue.append((nr, nc))
                # 방문처리 -> 0으로
                field[nr][nc] = 0
                

t = int(input())
for _ in range(t):
    cnt = 0
    m, n, k = map(int, input().split())
    # 그래프
    field = [[0] * m for _ in range(n)]
    # 방문 여부
    # visited = [[False] * m for _ in range(n)]
    # 상하좌우 좌표
    
    # 배추 위치 저장
    for _ in range(k):
        r, c = map(int,input().split())
        field[c][r] = 1
    

    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                bfs(i, j)
                cnt += 1

    print(cnt)
    
    
