import sys
input = sys.stdin.readline

def dfs(i, val, depth):
    global n
    global first
    global result
    
    # 방문을 다 했을 때 min 계산
    if depth == n:
    
    # 모두 방문하지 않았을 때 재귀
    for nx, c in cost[i]:
        if not visited[i]:
            dfs(nx, val + c, depth + 1)
            visited[nx] = False
        
    

n = int(input())

cost = []
result = float('inf')


for _ in range(n):
    cost.append(list(map(int, input().split())))

# 출발 지점 미정 -> 0 ~ n-1까지 방문
for i in range(n):
    visited = [False] * n
    # 시작점, 깊이(1) 정하기
    first = i
    depth = 1
    dfs(i, 0, depth) # 
