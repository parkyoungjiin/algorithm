from collections import deque
M, N = map(int,input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

print(graph)
start, end = 0, 0
# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
queue = deque()
for i in range(N):
    for j in range(M):
        # print(j, i)
        # print(graph[j][i])
        if graph[i][j] == 1:
            queue.append((i,j))
print(queue)
    
while queue:
    s, e = queue.popleft()
    for i in range(4):
        nx = s + dx[i]
        ny = e + dy[i]
        # print(nx, ny)
        if 0<=nx<N and 0<=ny<M:
            if graph[nx][ny] == 0:
                queue.append([nx,ny])
                graph[nx][ny] = graph[s][e] + 1

        
print(graph)
# 2차원 행렬에서 최대값 원소 찾기
print(max(map(max,graph))-1)




