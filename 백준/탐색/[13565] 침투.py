import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
m, n = map(int, input().split())


def dfs(x, y):
    # visited[x][y] = True
    graph[x][y] = '2'
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0<=nx<m and 0<=ny<n and graph[nx][ny] == '0':
            dfs(nx,ny)
            



graph = []
# visited = [[False] * n for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(m):
    graph.append(list(input().rstrip()))

for i in range(n):
    if graph[0][i] == '0': # outer line에서 0인 경우만 출발.
        dfs(0, i)

print(graph)
if '2' in graph[-1]:
    print('YES')
else:
    print('NO')

