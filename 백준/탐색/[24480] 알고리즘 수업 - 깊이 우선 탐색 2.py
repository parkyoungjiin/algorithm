import sys
input = sys.stdin.readline

sys.setrecursionlimit(150000)

n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)] # 0번지 포함

for _ in range(m):
    x, y= map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (n+1)

cnt = 0

def dfs(v):
    global cnt
    cnt += 1
    visited[v] = cnt

    graph[v].sort(reverse=True) # 내림차순 정렬

    for i in graph[v]:
        if not visited[i]:
            dfs(i)
    

dfs(r)
for i in visited[1:]:
    print(i)


