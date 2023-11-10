N, M = map(int, input().split())
miro = [[]]
# 입력받기(그래프 완성)
for _ in range(N):
    miro.append(list(map(int,input())))
print(miro)
# print(miro[2][1])
# 상하좌우
nx = [-1, 1, 0, 0]
ny = [0,0,-1,1]
x, y = 1,1
cnt = 0

def dfs(x,y):
    global cnt
    miro[x][y] = 0
    if x == N and y == M:
        return cnt
    for i in range(4):
        dx = x + nx[i]
        dy = y + ny[i]
        # print('dx:',dx,'dy:',dy)
        # print(miro[dx][dy])
        if 0<dx<=N and 0<dy<=M and miro[dx][dy-1] == 1:
            cnt += 1
            dfs(dx, dy)
dfs(x,y)