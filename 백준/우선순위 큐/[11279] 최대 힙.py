import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    val = int(input())
    if val != 0:
        heapq.heappush(heap, (-val, val))
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])

    
        


    