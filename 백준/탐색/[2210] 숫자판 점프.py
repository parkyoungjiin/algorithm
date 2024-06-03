def dfs(x, y, number):
    # 6자리 되면 종료
    if len(number) == 6:
        if number not in result:
            result.append(number)
        return

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < 5 and 0 <= ny < 5: #범위 내 dfs
            dfs(nx, ny, number +graph[nx][ny])


graph = []
for i in range(5):
    graph.append(list(map(str, input().split())))

result = []
for i in range(5):
    for j in range(5):
        dfs(i, j, graph[i][j])

print(len(result))