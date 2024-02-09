# 첫째 줄에 F, S, G, U, D가 주어진다. (1 ≤ S, G ≤ F ≤ 1000000, 0 ≤ U, D ≤ 1000000) 건물은 1층부터 시작하고, 가장 높은 층은 F층이다.
# F = 총 층, S = 현 위치, G = 목적지, U = 위, D = 아래
from collections import deque
import sys
input = sys.stdin.readline

f,s,g,u,d = map(int, input().split())
visited= [0 for _ in range(f+1)]
q = deque([s])
visited[s] = 1

while q:
    # 방문노드
    x = q.popleft()
    visited[x] = 1
    if x == g:
        print(visited[x])
        break
    
    for i in (u, -d):
        next = x + i

        if 1 <= next <= f and not visited[next]:
            visited[next] = visited[x] + 1
            q.append(next)

else:
    print("use the stairs")
            
