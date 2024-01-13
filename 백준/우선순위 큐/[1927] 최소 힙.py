import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap_list = []

for _ in range(n):
    temp = int(input())
    if temp != 0:
        heapq.heappush(heap_list, temp)
    else:
        if len(heap_list) != 0:
            print(heapq.heappop(heap_list))
        else:
            print(0)