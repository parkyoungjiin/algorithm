N, M = map(int,input().split())

r,c,d = map(int,input().split())
space = []
for _ in range(N):
    space.append(list(map(int,input().split())))
visited = [[0 for _ in range(M)] for _ in range(N)]
# print(space)
# 북동남서(시계방향) -> 반시계방향
dr = [-1,0,1,0]
dc = [0,1,0,-1]
cnt = 0
def bfs(r,c,d):
    global cnt
    # 방문처리
    space[r][c] = 1
    for i in range(4):
        # 반시계?
        nx = r + dr[i]
        ny = r + dc[i]
        # 청소해야 할 공간인 경우
        if 0<=nx<N and 0<=ny<M and space[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
