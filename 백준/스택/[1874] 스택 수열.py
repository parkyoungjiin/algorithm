import sys

input = sys.stdin.readline

n = int(input())
stack = []
count = 1
flag = 0

for _ in range(n):
    num = int(input())
    while count <= num:
        stack.append(count)
        count += 1
        print('+')

    if stack[-1] == num:
        stack.pop()
        print('-')
    else:
        print("NO")
        flag = 1
        break

if flag == 0:
    for i in stack:
        print(i)

    

    
    


stack = []
# for i in range(1, n+1):
#     stack.append(i)
#     idx = 0
#     if stack[0] == answer[idx]:
#         stack.pop()
        