import sys
import heapq

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    k = int(input())
    file = list(map(int, input().split()))
    heapq.heapify(file)
    for _ in range(k-1):
        print("pop:",heapq.heappop(file))
        print("pop2:",heapq.heappop(file))
    print(file)