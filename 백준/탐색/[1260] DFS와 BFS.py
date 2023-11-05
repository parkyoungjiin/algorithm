# 정점, 간선의 개수, 시작 번호
from collections import deque


N, M, V = map(int,input().split())

# 그래프 연결 정보
graph = [[] for _ in range(N+1)]
# 방문 여부
visited = [[False] * N+1 for _ in range(N)]
for m in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

# dfs
def dfs(graph, V, visited):
    # 현재 노드 방문 처리
    visited[V] = True
    print(V, end = '')

    # 현재 노드와 연결된 다른 노드를 False인 경우 재귀적으로 방문 처리.
    for j in graph[V]:
        if visited[j] == False:
            dfs(graph, j, visited)

# bfs
    









