import sys
from collections import deque
input = sys.stdin.readline

# 섬 구하는 함수
def find_island(i, j):
    global cnt
    q = deque()
    q.append((i,j))
    visited[i][j] = 0
    map[i][j] = cnt

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and map[nx][ny] == 1 and visited[nx][ny] == -1:
                visited[nx][ny] = 0
                map[nx][ny] = cnt
                q.append([nx,ny])

# 가장 짧은 거리 구하는 함수
def bfs(c):
    global answer
    dist = [[-1] * n for _ in range(n)] # 거리 저장 배열
    q = deque()

    for i in range(n):
        for j in range(n):
            if map[i][j] == c:
                q.append([i,j])
                dist[i][j] = 0
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >=n:
                continue
            # 다른 땅을 만나면 기존 답과 비교하여 짧은 거리를 선택.
            if map[nx][ny] > 0 and map[nx][ny] != c:
                answer = min(answer, dist[x][y])
                return
            # 바다를 만나면 dist를 1씩 늘린다.
            if map[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append([nx,ny])



n = int(input())

map = [list(map(int, input().split()))for _ in range(n)]

# 방문 여부 -1: 방문 X, 0: 방문O
visited = [[-1] * n for _ in range(n)]

answer = sys.maxsize
# 동서남북 좌표
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 섬 구별 Cnt
cnt = 1

# 섬 구별 시작(bfs 돌 때 마다 cnt + 1 된 상태로 변경함.)
for i in range(n):
    for j in range(n):
        if visited[i][j] == -1 and map[i][j] == 1:
            find_island(i,j)
            cnt += 1

# 짧은 거리 구하기
for i in range(1, cnt):
    bfs(i)

print(answer)




