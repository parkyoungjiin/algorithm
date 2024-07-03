import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    # 단방향이기에 한 쪽에만 넣어준다.
    graph[a].append(b)

distance = [-1] * (n+1) # ans -> 최단거리저장 배열
distance[x] = 0

q = deque([x]) # 시작점 
while q:
    current = q.popleft()
    
    for next_node in graph[current]:
        if distance[next_node] == -1: # 방문하지 않은 경우
            distance[next_node] = distance[current] + 1
            q.append(next_node)       

if k in distance:
    for a in range(len(distance)):
        if distance[a] == k:
            print(a)
else:
    print(-1)



    
    
        




    



