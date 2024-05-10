import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

result = 0
c = cost[0] # 첫 번째 도시 비용으로 초기값 설정.
for i in range(n-1):
    if c > cost[i]: # 해당 도시 비용이 더 작을 경우 갱신.
        c = cost[i]
    result += c * dist[i]

print(result)
