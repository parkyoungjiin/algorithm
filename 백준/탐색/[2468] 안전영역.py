"""
물에 잠기지 않는 안전한 영역이라 함은 물에 잠기지 않는 지점들이 위, 아래, 오른쪽 혹은 왼쪽으로 인접해 있으며 그 크기가 최대인 영역을 말한다. 
위의 경우에서 물에 잠기지 않는 안전한 영역은 5개가 된다(꼭짓점으로만 붙어 있는 두 지점은 인접하지 않는다고 취급한다).
-> 문장이 이해가지 않음.
"""

N = int(input())
area = []
max_h = 0
# 영역 2차원 배열 입력 받기
for _ in range(N):
    low = list(map(int,input().split()))
    area.append(low)
    # 큰 값 판별
    for j in low:
        if j > max_h:
            max_h = j
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 깊이 탐색
def dfs(x, y, i):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 벗어나지 않고, 방문하지 않은 경우
        if 0<=nx<N and 0<=ny<N and visited[nx][ny] == False:
            # i보다 큰 경우(잠기지 않는 경우) -> 다시 dfs 돌려서 재귀
            visited[nx][ny] == True
            dfs(nx, ny, i)



# 높이(1<=h<=100) max_h 만큼만 반복
for i in range(max_h):
    # 안전지대 count 변수
    count = 0
    # visited?
    visited = [[False] * N for _ in range(N)]
    # dfs
    for x in range(N):
        for y in range(N):
            # i보다 area원소가 큰 경우는 안전지대.
            if area[x][y] > i and visited[x][y] == False: 
                count += 1
                visited[x][y] = 1
                dfs(x, y,i) 
    result = max(result, count)
                
print(result)
    
