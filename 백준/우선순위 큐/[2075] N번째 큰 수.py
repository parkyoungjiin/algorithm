import sys
import heapq
input = sys.stdin.readline
# https://naroforme.tistory.com/entry/%EB%B0%B1%EC%A4%80-2075%EB%B2%88-N%EB%B2%88%EC%A7%B8-%EC%88%98-%ED%8C%8C%EC%9D%B4%EC%8D%AC

n = int(input())
num_list=[]
for _ in range(n):
    temp = map(int,input().split())
    for t in temp:
        if len(num_list) < n:
            heapq.heappush(num_list, t)
        else:
            if num_list[0] < t:
                heapq.heappop(num_list)
                heapq.heappush(num_list, t)
print(num_list[0])



        
    
