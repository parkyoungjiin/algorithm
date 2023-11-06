
"""
첫째 줄에는 컴퓨터의 수가 주어진다. 
컴퓨터의 수는 100 이하인 양의 정수이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다.
 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 
 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.
"""

# 컴퓨터 수(0< n <=100)
n = int(input())

# 컴퓨터 쌍 수
m = int(input())

# 컴퓨터 연결 정보
network = [[] for _ in range(n+1)]
# print(network)
# 방문 여부
visited = [False] * (n+1)
# print(visited)
# 연결 정보 추가
for i in range(m):
    a,b = map(int,input().split())
    network[a].append(b)
    network[b].append(a)
# print(network)
virus = 0
v = 1

# dfs
def dfs(v):
    global virus
    # 방문 처리
    visited[v] = True
    
    for n in network[v]:
        if visited[n] == False:
            dfs(int(n))
            virus += 1

dfs(v)
print(virus)


