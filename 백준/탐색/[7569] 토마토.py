from collections import deque
import sys
M, N, H = map(int, input().split())
tomato = []
# 3차원 배열로 생성(토마토)
for i in range(H):
    tmp = []
    for i in range(N):
        tmp.append(list(map(int,input().split())))
    tomato.append(tmp)
# 6방향 설정(상하좌우위아래)
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,1,-1]

# 익은 토마토 위치 저장
queue = deque()
for z in range(H):
        for i in range(N):
            for j in range(M):
                 if tomato[z][i][j] == 1:
                    queue.append((z,i,j))

# bfs 처리
while queue:
    z,i,j = queue.popleft()
    for idx in range(6):
        nz = z + dz[idx]
        nx = i + dx[idx]
        ny = j + dy[idx]
        if 0<=nz<H and 0<=nx<N and 0<=ny<M:
            if tomato[nz][nx][ny] == 0:
                    queue.append((nz,nx,ny))
                    tomato[nz][nx][ny] = tomato[z][i][j] + 1
# print(tomato)
# 일자 출력하기
day = 0
for i in tomato:
     for j in i:
          for k in j:
               # 0이 하나라도 있으면 익지 못하기에 -1 출력
               if k == 0:
                    print(-1)
                    exit()
          day = max(day, max(j))
        #   print(day)
print(day -1 )
                



    
