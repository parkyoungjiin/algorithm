from collections import deque
# 지도 크기
N = int(input())

# 지도 정보
map_info = []
for _ in range(N):
    map_info.append(list(map(int,input())))

# print(map_info)
# 좌표 (상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs 안에서 단지 내 개수 출력.
def bfs(map_info, a, b):
    n = len(map_info)
    queue = deque()
    queue.append((a, b))
    map_info[a][b] = 0
    count = 1
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if map_info[nx][ny] == 1:
                map_info[nx][ny] = 0
                queue.append(nx, ny)
                count += 1
    return count
            
# 단지 개수
cnt = []
# 단지 내 집 개수
# 2차원 행렬
for i in N:
    for j in N:
        # 사는 집인 경우
        if map_info[i][j] == 1:
            cnt.append(bfs(map_info, i, j))

    
cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])