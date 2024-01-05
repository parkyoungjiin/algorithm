import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque()
for _ in range(n):
    command = input().rstrip()
    if "push" in command:
        command, number = command.split()
        queue.append(int(number))
        print(number)
    elif command == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            number = int(queue.popleft())
            print(number)
        
    elif command == "size":
        print(len(queue))
    elif command == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif command == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif command == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
        