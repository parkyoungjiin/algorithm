# --- bfs(pypy 통과 코드)---
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a) # 역방향 그래프 설정


def bfs(s):
    q = deque()
    q.append(s)
    cnt = 0

    visited=[False] * (n+1)
    visited[s] = True

    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                cnt += 1
    return cnt


answer = []
for i in range(1, len(graph)):
    answer.append(bfs(i))

max_value = max(answer)
# print(answer)
for i in range(len(answer)):
    if max_value == answer[i]:
        print(i+1, end=' ')




# --- dfs (시간초과)
# import sys
# sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline

# def dfs(s):
#     global cnt
#     cnt += 1
#     for i in graph[s]:
#         dfs(i)


# n, m = map(int, input().split())

# graph = [[] for _ in range(n+1)]
# answer = [0 for _ in range(n+1)]
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[b].append(a)

# for i in range(1, n+1):
#     cnt = 0
#     dfs(i)
#     answer[i] = cnt
# max_value = max(answer)
# for i in range(1, n+1):
#     if max_value == answer[i]:
#         print(i, end=' ')


