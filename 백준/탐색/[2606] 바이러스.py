import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
k = int(input())
virus = [[] for _ in range(n+1)]
visited = [0] * (n+1)


for _ in range(k):
    a, b = map(int, input().split())
    # 연결 정보 넣기
    virus[a].append(b)
    virus[b].append(a)

# 1번부터 방문(고정)
visited[1] = 1

queue = deque([1])

while queue:
    c = queue.popleft()
    for x in virus[c]:
        # 방문하지 않은 경우
        if visited[x] == 0:
            queue.append(x)
            visited[x] = 1
        
print(sum(visited)-1)

        


    

