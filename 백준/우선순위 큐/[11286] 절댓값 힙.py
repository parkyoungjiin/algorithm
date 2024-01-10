import heapq
import sys
input = sys.stdin.readline
n = int(input())
heap_list = []

for _ in range(n):
    command = int(input())
    if command != 0:
        # 튜플(절대값, 원래수)
        # -> (우선순위, 기존값)
        heapq.heappush(heap_list,(abs(command), command))
        # heapq.heappush(heap_list, command)
    else:
        if len(heap_list) == 0:
            print(0)
        else:
            # heappop할 때 우선순위 중 가장 작은 값부터 출력(command)
            print(heapq.heappop(heap_list))