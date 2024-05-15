import sys
from collections import deque

n, m = map(int, input().split())

find_num = list(map(int, input().split()))

num_list = [i for i in range(1, n+1)]

q = deque(num_list)
result = 0
for i in find_num:
    mid = len(q) // 2
    
    while True:
        # 맨 앞에 위치할 경우 제거.
        if i == q[0]:
            q.popleft()
            break
        # 다른 위치에 있는 경우 왼 / 오 선택
        if q.index(i) <= mid: # 왼 이동
            q.rotate(-1)
            result += 1
        else:
            q.rotate(1)
            result += 1

print(result)
        
    

    