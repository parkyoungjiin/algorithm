import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    vps = list(input())
    stack = []
    for i in range(len(vps)):
        if vps[i] == '(':
            stack.append(vps[i])
        elif vps[i] == ')':
            if len(stack) == 0:
                print('NO')
                break
            else:
                stack.pop()

    else:
        if not stack:
            print('YES')
        else:
            print('NO')

        
    


    