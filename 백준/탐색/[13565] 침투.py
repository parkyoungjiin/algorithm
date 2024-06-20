import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
m, n = map(int, input().split())

def dfs(x, y):
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0<=nx<m and 0<=ny<n and graph[nx][ny] == '0':
            graph[nx][ny] = '2'
            dfs(nx, ny)

graph = []

for i in range(m):
    graph.append(list(input().rstrip()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    if graph[0][i] == '0':
        graph[0][i] = '2'
        dfs(0, i)

if '2' in graph[-1]:
    print("YES")
else:
    print("NO")