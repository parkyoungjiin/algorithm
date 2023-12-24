# 첫째 줄은 DFS, 다음 줄은 BFS 결과 출력
# V부터 방문된 점을 순서대로 출력.

import sys
from collections import deque
input = sys.stdin.readline
N, M, V = map(int,input().split())
# 행렬 만들기.(graph : 2차원 배열)
graph = [[False] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

print("graph:", graph)
print("visited:",visited)
# 2. dfs
def dfs(v):
    global visited
    visited[v] = True
    print(v, end = ' ')
    for next in range(1, N + 1):
        # 방문 하지 않았고(=> visited에서 False), 연결된 노드(=> graph에서 True)인 경우에 호출
        if not visited[next] and graph[v][next]:
            dfs(next)

# 3. bfs
def bfs(v):
    global visited, q
    # q에 요소가 있을 때 까지 반복.
    while q:
        cur = q.pop(0)
        print(cur, end = ' ')
        # 방문하지 않은 경우 v를 큐에 삽입한다.
        for next in range(1, N+1):
            if not visited[v] and graph[cur][next]:
                q.append(ㅜㄷㅌㅅ                visited[v] = True




dfs(V)
print() # dfs 후 bfs출력
visited = [False] * (N+1)
# v는 시작 노드이기에 방문 처리 하고 시작. + 큐에 v를 먼저 넣고 시작.(재방문 방지)
q = [V]
visited[V] = True

bfs()

