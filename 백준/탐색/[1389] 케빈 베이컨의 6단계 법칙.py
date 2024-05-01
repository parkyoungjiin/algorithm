import sys
from collections import deque

input = sys.stdin.readline

def bfs(s):
    #graph[1] = [3,4]
    q = deque(graph[s])
    visited[s] = 1

    while q:
        next_val = q.popleft()

        for i in graph[next_val]:
            if not visited[i]: # 0
                visited[i] = visited[next_val] + 1 
                q.append(i)


n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
# print(graph)

result = []

for i in range(1,n+1):
    visited = [0] * (n + 1)
    bfs(i)
    result.append(sum(visited))

print(result.index(min(result)) + 1)
