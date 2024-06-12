import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    
    q = []
    heapq.heappush(q, (0,start))

    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue

        for i in graph[now]:
            #i[0] 길/지름길 도착지점
            #i[1] 길/지름길 길이
            cost = dist + i[1] #현재 지점에서 길/지름길을 더함 

            #해당 노드로 가는데 계산된 비용이 최단거리테이블보다 작으면 업데이트
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
n, d = map(int,input().split())

INF = int(1e9)

distance = [INF]*(d+1)
graph = [[] for _ in range(d+1)]

for i in range(d):
    graph[i].append((i+1,1))

for _ in range(n):
    start, end , length = map(int, input().split())
    
    if end > d: 
        continue
    
    #지름길 정보 입력
    graph[start].append((end, length))

dijkstra(0)
print(distance[d])


# import sys
# input = sys.stdin.readline

# n, d = map(int, input().split())


# shortcut = []
# for _ in range(n):
#     shortcut.append(list(map(int,input().split())))

# shortcut.sort()

# dp = [i for i in range(d+1)] # 거리 저장 DP (1차원) -> 기본 거리를 저장.

# k = 0 # k -> shortcut index

# for i in range(d+1):
#     # 기본 도로 갱신
#     dp[i] = min(dp[i-1]+1, dp[i])

#     # 지름길 갱신
#     while k < n: # n = len(shortcut)
#         if shortcut[k][0] == i: # start == i
#             if shortcut[k][1] <= d:
#                 dp[shortcut[k][1]] = min(dp[i] + shortcut[k][2], dp[shortcut[k][1]])
#             k+=1 # k++
#         else:
#             break
    
# print(dp[d])






