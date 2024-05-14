import sys
input = sys.stdin.readline

l = int(input())

for _ in range(l):
    password = list(input())
    cursor = 0
    answer = []

    for i in password:
        if i == '>' and len(answer) !=0 :
            if len(answer) < cursor + 1:
                continue

            cursor += 1
        elif i == '<' and len(answer) !=0 :
            if cursor == 0:
                continue

            cursor -= 1
        elif i == '-':
            answer.pop(cursor-1)
            if cursor != 0:
                cursor -= 1
                
        elif  i != '>' and i != '<' and i != '-':
            if cursor != 0:
                answer.insert(cursor, i)
                cursor += 1
            else:
                cursor += 1
                answer.append(i)

    for i in answer:
        print(i, end='')