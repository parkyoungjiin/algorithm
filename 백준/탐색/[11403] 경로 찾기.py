import sys
input = sys.stdin.readline
n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

def dfs(num):
    for i in range(n):
        if visited[i] == 0 and graph[num][i] == 1:
            visited[i] = 1
            dfs(i)



for i in range(n):
    visited=[0 for _ in range(n)]
    dfs(i)
    print(*visited)

