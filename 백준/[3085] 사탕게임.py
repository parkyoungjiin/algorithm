import sys
input = sys.stdin.readline

def check(graph):
    max_cnt = 1
    for i in range(n):
        # 가로 확인
        cnt = 1 #기본 1개
        for j in range(1, n):
            if graph[i][j] == graph[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(cnt, max_cnt)
        # 세로 확인
        cnt = 1
        for j in range(1, n):
            if graph[j][i] == graph[j-1][i]:
                cnt += 1
            else:
                cnt += 1
            max_cnt = max(cnt, max_cnt)

    return max_cnt

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(input()))

answer = 0
for i in range(n):
    for j in range(n-1):
        # 오른쪽
        if j + 1 < n and graph[i][j] != graph[i][j+1]:
            # 오른쪽 요소와 교환
            graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]
            # 변경 후 사탕 개수 계산.
            temp_cnt = check(graph)
            answer = max(answer, temp_cnt)
            # 교환 복구
            graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]
        # 아래
        if i + 1 < n and graph[i][j] != graph[i+1][j]:
            # 아래 요소와 교환
            graph[i][j], graph[i+1][j] = graph[i+1][j], graph[i][j]
            # 변경 후 사탕 개수 계산.
            temp_cnt = check(graph)
            answer = max(answer, temp_cnt)
            # 교환 복구
            graph[i][j], graph[i+1][j] = graph[i+1][j], graph[i][j]
print(answer)

