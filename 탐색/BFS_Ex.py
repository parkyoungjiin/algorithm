# 미로 탈출
# 현재 위치를 기준으로 상하좌우(근접한 노드)에 괴물이 있는 지 없는 지 판별하여 없는 부분(1)으로 움직
# 탈출을 위해 움직여야 하는 최소 칸의 개수 (이동할 때 마다 칸 수를 count 증가)
# 칸을 셀 때는 시작, 마지막 칸 모두 포함

# 공백 구분을 통해 입력받기
from collections import deque


N, M = map(int, input().split())
# 입력된 값을 하나씩 리스트에 집어넣음(미로)
miro = []
for i in range(N):
    miro.append(list(map(int,input())))

# 이동할 방향 정의 (상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 함수 정의
def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시 (N, X 보다 크면 안되고 음수가 되서는 안된다.)
            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue
            # 벽인 경우 무시
            if miro[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리를 기록한다.
            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[nx][ny] + 1
                queue.append((nx,ny))

    return miro[N -1][M -1]  