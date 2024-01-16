import sys
import heapq
input = sys.stdin.readline

card = []
n = int(input())
total_val = 0
answer = []
for _ in range(n):
    c = int(input())
    heapq.heappush(card, c)

while len(card) > 1:
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    sum_val = a + b
    total_val += sum_val

    heapq.heappush(card, sum_val)
print(total_val)



