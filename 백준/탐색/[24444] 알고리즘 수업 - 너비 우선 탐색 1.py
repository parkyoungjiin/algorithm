import sys
from collections import deque
input = sys.stdin.readline

n,m,r = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y= map(int, input().split())

    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (n+1)
visited[r] = 1 # 시작 노드 방문

queue = deque([r]) # 시작점 넣고 큐 생성

cnt = 1 # 방문순서 변수

while queue:
    node = queue.popleft()
    graph[node].sort() # 오름차순 정렬

    for i in graph[node]:
        if not visited[i]:
            queue.append(i)
            cnt += 1 # 방문순서 + 1
            visited[i] = cnt

for i in visited[1:]:
    print(i)



    
