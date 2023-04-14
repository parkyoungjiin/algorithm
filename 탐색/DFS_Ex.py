# 음료수 얼려먹기 예제
# dfs를 사용하여 특정 노드를 방문
def dfs(x, y):
    # 범위를 벗어나는 경우 즉시 종료
    if x >= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 0일 때는 얼릴 수 있는 공간
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x -1, y)
        dfs(x, y-1)
        dfs(x + 1, y)
        dfs(x, y+1)
        return True
    return False



# 1.  N * M 크기로 이뤄진 얼음 틀

n, m = map(int, input().split())

# 2. 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    # graph에 입력한 값들을 하나씩 리스트에 넣음.
    graph.append(list(map(int,input())))

# 모든 노드에 대해 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(n,m) == True:
            result += 1
print(result)