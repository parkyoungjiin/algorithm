import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
arr = []
answer = 0
for i in range(n):
    deadline, cup = map(int,input().split())
    #heappush(list, (값1, 값2)) -> 값1을 우선순위로 잡고 heappush
    # heapq.heappush(heap,(-cup, deadline))
    arr.append((deadline, cup))
arr.sort()
print(arr)

for i in arr:
    heapq.heappush(heap, i[1])
    # 데드라인 = i[0] 보다 길이가 더 큰 경우
    # 같은 데드라인을 가지는 튜플이 있다는 이야기이므로 pop
    if i[0] < len(heap):
        heapq.heappop(heap)
    

print(heap)
    
        
            
        
    
        

    




