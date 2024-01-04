import sys
input = sys.stdin.readline

n = int(input())

stack = []
# command_list = ["push", "pop", "size", "empty", "top"]
for _ in range(n):
    command = input().rstrip()
    if "push" in command:
        command, number = command.split()
        stack.append(int(number))
    elif command == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command == "pop":
        if len(stack) > 0:
            num = stack.pop()
            print(num)
        else:
            print(-1)




