import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())

tree_lst = [[] for _ in range(n+1)]
visited = [0] * (n+1) # 방문 & 부모 노드 저장 변수
visited[1] = 1

def dfs(vertex, visited):
    for i in tree_lst[vertex]:
        if not visited[i]:
            visited[i] = vertex
            dfs(i, visited)

for i in range(n-1):
    a, b = map(int, input().split())
    tree_lst[a].append(b)
    tree_lst[b].append(a)


dfs(1, visited)

for i in range(2, n+1):
    print(visited[i])


