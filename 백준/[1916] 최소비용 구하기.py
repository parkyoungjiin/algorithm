import sys
from collections import deque
import heapq
input = sys.stdin.readline
# n 도시 개수
n = int(input())
# m 버스 개수
m = int(input())

# bus_cost = {}
bus_route = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, cost= map(int,input().split())
    # bus_cost[(start,end)] = cost
    bus_route[start].append((end,cost))

start_city, end_city = map(int, input().split())

def dijkstra(bus_route, start):
    distances = [int(1e9)] * (n+1)
    distances[start] = 0

    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        dist, node = heapq.heappop(queue) # 탐색할 노드, 거리
        
        if distances[node] < dist:
            continue
            
        for next_node, next_dist in bus_route[node]:
            distance = dist + next_dist
            if distance < distances[next_node]:
                distances[next_node] = distance
                heapq.heappush(queue, [distance, next_node])

    return distances

dis_start = dijkstra(bus_route, start_city)
print(dis_start)
print(dis_start[end_city])