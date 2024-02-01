import sys
from collections import deque

m, n, k = map(int, input().split())

graph = [[0] * n for _ in range(m)]
# print(graph)


for _ in range(k):
    sc, sr, ec, er = map(int, input().split())
    
    # 시작 ~ 끝점까지 모두 1로 변경
    # 행 -> sr ~ er
    # 열 -> sc ~ ec
    for i in range(sr,er):
        for j in range(sc, ec):
            graph[i][j] = 1

def bfs(a,b):
    dr=[-1, 1, 0, 0]
    dc=[0, 0, -1, 1]
    cnt = 1
    graph[a][b] = 1
    queue = deque()
    queue.append((a,b))

    while queue:
        r,c = queue.popleft()
        for i in range(4):
            mr = r + dr[i]
            mc = c + dc[i]
            if 0 <= mr < m and 0 <= mc < n and graph[mr][mc] == 0:
                # 방문처리
                graph[mr][mc] = 1
                queue.append((mr,mc))
                cnt += 1
                
    result.append(cnt)

result = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            bfs(i,j)

result.sort()
print(len(result))
print(*result)     






