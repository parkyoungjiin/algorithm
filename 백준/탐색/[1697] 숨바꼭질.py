from collections import deque
N, K = map(int,input().split())
max_value = 100000
visited = [0] * (max_value + 1)
# print(visited[N])
# v는 초.
def bfs(N):
    for v in range(len(visited)):
        second = v + 1
        queue = deque()
        queue.append(N)
        while queue:
            x = queue.popleft()
            # 꺼낸 큐를 방문처리
            visited[x] == 1
            if x == K:
                print(second)
                break
            for j in (x-1, x+1, x*2):
                if 0 <= j <= max_value and not visited[j]:
                    visited[j] = 1
                    queue.append(j)

bfs(N)








