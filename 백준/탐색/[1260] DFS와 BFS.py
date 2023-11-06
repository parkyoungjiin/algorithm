# 정점, 간선의 개수, 시작 번호
from collections import deque


N, M, v = map(int,input().split())

# 그래프 연결 정보
graph = [[] for _ in range(N+1)]
# => [[2,3,4], [1], [2,3], []]
# 방문 여부
visited = [[False] * (N+1) for _ in range(N)]
# => [[False],[Fasle]]

for m in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()


# dfs
def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end = '')

    # 현재 노드와 연결된 다른 노드를 False인 경우 재귀적으로 방문 처리.
    for j in graph[v]:
        if visited[j] == False:
            dfs(graph, j, visited)

# bfs
def bfs(graph, v, visited):
    queue = deque([v])
    # 방문 처리
    visited[v] = True 

    # 큐가 빌 때까지
    while queue:
        v = queue.popleft()
        print(v, end =' ')
        for i in graph[v]:
            # 방문하지 않은 노드를 큐에 삽입 + 방문 처리
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
        
    
bfs(graph, v, visited)








