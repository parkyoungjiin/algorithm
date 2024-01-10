import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque()
for i in range(1, n+1):
    queue.append(i)

if len(queue) == 1:
    print(queue[0])

while len(queue) != 1:
    queue.popleft()
    
    if len(queue) == 1:
        print(queue[0])
    
    else:
        temp = queue.popleft()
        queue.append(temp)


