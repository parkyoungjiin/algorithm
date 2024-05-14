import sys
input = sys.stdin.readline

l = int(input())

for _ in range(l):
    password = list(input().strip())
    cursor = 0
    answer = []

    for i in password:
        if i == '>' and cursor < len(answer):
            cursor += 1

        elif i == '<' and cursor > 0 :
            cursor -= 1

        elif i == '-' and cursor > 0:
            answer.pop(cursor-1)
            cursor -= 1
                
        elif  i != '>' and i != '<' and i != '-':
            answer.insert(cursor, i)
            cursor += 1

    for i in answer:
        print(i, end='')