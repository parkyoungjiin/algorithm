# 첫째 줄에 F, S, G, U, D가 주어진다. (1 ≤ S, G ≤ F ≤ 1000000, 0 ≤ U, D ≤ 1000000) 건물은 1층부터 시작하고, 가장 높은 층은 F층이다.
# F = 총 층, S = 현 위치, G = 목적지, U = 위, D = 아래
from collections import deque
F, S, G, U, D = map(int,input().split())
# 방문처리 + 갯수 세는 변수
visited = [0] * (F+1)
def bfs(start):
    # 방문 처리
    
    queue = deque()
    queue.append(start)
    # visited[start] = 1
    while queue:
        q = queue.popleft()
        # print(q)
        if q == G:
            # print("종료")
            return visited[q]
        else:
            for i in (q+U, q-D): # U, D 0, 3
                if (0<i<=F) and visited[i] == 0:
                    visited[i] = visited[q] + 1
                    queue.append(i)
# visited[1] = 1 -> visited[3] =2
    return "use the stairs"




print(bfs(S))