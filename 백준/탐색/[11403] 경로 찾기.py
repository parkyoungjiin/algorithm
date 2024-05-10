import sys
input = sys.stdin.readline
n = int(input())

graph = []

def dfs(num):
    for i in range(n):
        if graph[num][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)
            


for _ in range(n):
    graph.append(list(map(int, input().split())))

# 행
for i in range(n):
    visited = [0 for i in range(n)]
    dfs(i)
    print(*visited)
    


