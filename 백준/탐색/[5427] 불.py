import sys
from collections import deque

input = sys.stdin.readline

# 불은 1초마다 동서남북으로 다 번진다.
def burn():
    for _ in range(len(fire)):
        x, y = fire.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w:
                if building[nx][ny] != '#' and building != '*':
                    # 불 번짐
                    building[nx][ny] = '*' 
                    fire.append([nx,ny])


t = int(input())
w, h = map(int, input().split())

# 동서남북 좌표
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# main
for _ in range(t):
    building = []
    visited = [[0] * w for i in range(h)]

    fire = deque()
    start = deque()

    # 빌딩 좌표
    for _ in range(h):
        building.append(list(map(str, input().rstrip())))

    # 불, 상근 위치
    for i in range(h):
        for j in range(w):
            if building[i][j] == '@':
                start.append([i,j])

            if building[i][j] == '*':
                fire.append([i,j])
