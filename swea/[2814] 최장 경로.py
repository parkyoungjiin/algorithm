def dfs(v, count):
    global max_count

    # 방문 처리
    visited[v] = True

    for i in graph[v]:
        # 방문하지 않은 경우 방문(count+1)
        if visited[i] == False:
            dfs(i, count + 1)

    # 다시 방문할 수 있기에 False처리
    visited[v] = False
    # max_count 갱신
    if count > max_count:
        max_count = count



tc = int(input())
for t in range(1, tc+1):
    n, m = map(int, input().split())
    # 경로 저장 배열
    graph = [[] * i for i in range(n+1)]
    # 방문 처리 배열
    visited = [False] * (n+1)

    result = 0
    
    for i in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    count, max_count = 0, 0

    for i in range(1, n+1):
        dfs(i, 1)
    
    print("#{} {}".format(t, max_count))

