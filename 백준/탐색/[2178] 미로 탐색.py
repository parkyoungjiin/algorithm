from collections import deque

N, M = map(int, input().split())
miro = []
# 입력받기(그래프 완성)
for _ in range(N):
    miro.append(list(map(int,input())))
print(miro)
# print(miro[2][1])
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0,0,-1,1]
# x, y = 0,0


queue = deque()
queue.append([0,0])
# print(queue.popleft())
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M:
            if miro[nx][ny] == 1:
                queue.append((nx,ny))
                miro[nx][ny] = miro[x][y] + 1
print(miro)
print(miro[N-1][M-1])
    


# def dfs(x,y):
#     global cnt
#     # 방문처리
    
#     for i in range(4):
#         dx = x + nx[i]
#         dy = y + ny[i]
     
#         if 0<=dx<N and 0<=dy<M:
#             if miro[dx][dy] != 0:
#                 miro[x][y] = 0
#                 cnt+=1
#                 dfs(dx, dy)
                

#     print(cnt)
# dfs(x,y)