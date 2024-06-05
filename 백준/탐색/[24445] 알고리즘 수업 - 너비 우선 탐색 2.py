import sys
from collections import deque

input = sys.stdin.readline

def bfs(s):
    global cnt
    q = deque([s])
    while q:
        node = q.popleft()
        for i in sorted(graph[node], reverse=True):# 내림차순 정렬
            if visited[i] == 0:
                cnt += 1
                visited[i] = cnt
                q.append(i)


n, m, s = map(int,input().split())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
visited[s] = 1
cnt = 1
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


bfs(s)
for i in visited[1:]:
    print(i)







