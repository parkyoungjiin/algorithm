import sys
input = sys.stdin.readline
sys.setrecursionlimit(150000)

def dfs(start):
    global cnt
    visited[start] = cnt
    # 오름차순으로 방문하기에 정렬.
    graph[start].sort()
    for i in graph[start]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)
    
n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)] # 초기값 0으로 설정한 후에 방문 순서를 저장함.

# 방문하는 순서 계산 변수
cnt = 1

for _ in range(m):
    # 양방향으로 저장.
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(r)

for i in range(1, n+1):
    print(visited[i])
