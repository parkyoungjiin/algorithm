import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    #간선 정보
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

# dfs
def dfs(v):
    for i in graph[v]:
        if visited[i] == False:
            visited[i] = True
            dfs(i)

cnt = 0

for i in range(1, n+1):
    if visited[i] == False:
        cnt += 1
        dfs(i)
    
print(cnt)

