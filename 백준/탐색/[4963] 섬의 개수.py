import sys
from collections import deque
input = sys.stdin.readline


def bfs(i, j):
    dx = [1, -1 ,0 , 0, 1, -1, 1, -1]
    dy = [0, 0, 1, -1, 1, -1, -1, 1]
    q = deque()
    q.append((i, j))
    #방문 처리
    graph[i][j] = 0
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            # h, w 실수함
            if 0<=nx<h and 0<=ny<w and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx,ny))

while True:
    count = 0
    w, h = map(int,input().split())

    if w == 0 and h == 0:
        break
    graph = []
    # visited = [[False] * h for _ in range(w)]
    
    # 입력받기
    for _ in range(h):
        graph.append(list(map(int,input().split())))

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i, j)
                count += 1

    print(count)