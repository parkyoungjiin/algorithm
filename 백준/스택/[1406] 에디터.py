import sys
from collections import deque
input = sys.stdin.readline

left_lst = deque(list(input().rstrip()))
right_lst = deque()

n = int(input())

for _ in range(n):
    command = input().split()
    
    if command[0] == 'L' and len(left_lst) != 0:
        t = left_lst.pop()
        right_lst.appendleft(t)
    elif command[0] == 'D' and len(right_lst) != 0:
        t = right_lst.popleft()
        left_lst.append(t)
    elif command[0] == 'B' and len(left_lst) != 0:
        left_lst.pop()
    elif command[0] == 'P':
        left_lst.append(command[1])

print("".join(list(left_lst)+list(right_lst)))