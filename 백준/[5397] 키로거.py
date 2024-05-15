import sys
input = sys.stdin.readline

l = int(input())

for _ in range(l):
    password = list(input().strip())
    left, right = [], []

    for i in password:
        if i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())

        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)
    
    left.extend(reversed(right))
    
    print(''.join(left))

    