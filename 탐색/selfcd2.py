# 미로 탈출
# 함수 정의 (bfs)
from collections import deque

# 이동횟수, 현재 정점, 방문여부
def bfs(x,y):
    # 큐 선언
    queue = deque()
    # 현재 정점을 큐에 넣고 인접한 노드에 0이 있는 지 판별
    queue.append(x,y)
    
    # 큐가 빌때까지 반복
    while queue:
        x,y = queue.popleft()
        # 현 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 범위 내에 있는 지 확인
            if nx < 0 or nx <=n or ny < 0 or ny <= m:
                continue
            # 벽 인경우에 무시
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    



# 이동 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 미로 크기 입력받기
n,m = map(int,input().split())
graph = []
start, end = 1,1

# 미로 정보 입력받기
for i in range(n):
    graph.append(input())

# 최소 이동 횟수 입력받기
int(input())

