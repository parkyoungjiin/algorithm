import sys
import heapq

input = sys.stdin.readline

n = int(input())

num_list = []
for _ in range(n):
    heapq.heappush(num_list,int(input()))
    num_list.sort() 
    print(num_list)


