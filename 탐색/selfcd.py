# 음료수 얼려먹기 dfs, bfs 판별 -> bfs?
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False   
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 상하좌우 재귀 호출
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)

        return True
    return False


# 1. 얼음 틀 크기 입력받기
n, m = map(int, input().split())
# 2. 틀 내용물 입력받기 (2차원 리스트))
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))
# 3. 틀에 음료수 채우기
count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1


