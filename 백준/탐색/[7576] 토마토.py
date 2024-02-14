from collections import deque
import sys

input = sys.stdin.readline
# 행, 열
m, n  = map(int, input().split())
tomato = []
for _ in range(n):
    tomato.append(list(map(int,input().split())))
# tomato = [list(map(int,input().split())) for _ in range(n)]

# 좌표
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
# 결과
res = 0
q = deque([])

for i in range(n):
    for j in range(m):
        # 익은 토마토 인 경우
        if tomato[i][j] == 1:
            q.append([i,j])
# bfs 탐색
while q:
    r, c = q.popleft()
    # 인접한 토마토 익음
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < m:
            if tomato[nr][nc] == 0:
                tomato[nr][nc] = tomato[r][c] + 1
                q.append((nr,nc))
# 토마토를 다 탐색하면서 0이 있다면 익지 않은 것이기에 -1를 출력하고 종료.
for t_list in tomato:
    for t in t_list:
        if t == 0:
            print(-1)
            exit()
    # 0 이 없는 경우 max 값 갱신
    res = max(res, max(t_list))
# 1로 시작하기에 1을 빼준다.(날짜)
print(res-1)

