n = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
answer = [0] * (n+1)

def dfs(s):
    visited[s] = True
    # 연결된 노드들을 하나씩 꺼낸다.
    for i in graph[s]:
        if not visited[i]:
            # 자식노드로 가기 전 부모노드를 저장.(s가 부모노드)
            answer[i] = s
            dfs(i)

dfs(1)

for i in range(2, n+1):
    print(answer[i])
