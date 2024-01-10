import heapq
# heapq는 최소 힙 자료구조(부모<= 자식)
# 즉, 루트 노드는 heapq에서 가장 작은 값.
heap_list = []
heapq.heappush(heap_list, 4)
heapq.heappush(heap_list, 6)
heapq.heappush(heap_list, 3)
heapq.heappush(heap_list, 1)
heapq.heappush(heap_list, 2)

print(heap_list)