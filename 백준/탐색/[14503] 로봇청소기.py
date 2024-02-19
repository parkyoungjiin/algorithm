import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

r,c,d = map(int, input().split())

house = [list(map(int,input().split())) for _ in range(n)]
cnt = 0
print(house)
# 북 동 남 서 
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(r,c,d):
    global cnt
    flag = 0
    # house[r][c] = 2
    # cnt += 1
    q = deque()
    q.append((r,c))

    while q:
        r, c = q.popleft()
        if house[r][c] == 0:
            house[r][c] = 2
            cnt += 1

        for _ in range(4):
        # 반 시계 90도 회전
            d = (d+3) % 4
            nr, nc = r + dr[d], c + dc[d]
            # if 0 <= nr < n and 0 <= nc < m:
            # 청소되지 않은 칸이 있는 경우
            if house[nr][nc] == 0:
                # house[nr][nc] = 2
                q.append((nr,nc))
                # cnt += 1
                flag = 1
                break
    
        # 청소되지 않은 칸이 없는 경우
        if flag == 0:
            back = (d+2) % 4
            if house[r+dr[back]][c+dc[back]] == 1:
                return
            else:
                q.append((r+dr[back], c+dc[back]))
    
bfs(r, c, d)
print(cnt)