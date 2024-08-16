data = input()

stack = []
ans = ''
check = False # 괄호안 여부 체크 변수
for d in data:
    # 스택에 존재하는 값을 역으로 추가
    if d == '<':
        check = True
        for _ in range(len(stack)):
            ans += stack.pop()

    stack.append(d)
    # 스택에 존재하는 값은 괄호안의 값이기에 순차적으로 추가
    if d == '>':
        check = False
        for _ in range(len(stack)):
            ans += stack.pop(0)
    # 스택에 존재하는 값을 역으로 추가
    if d == ' ' and check == False:
        for i in range(len(stack)):
            if i == 0:
                stack.pop()
                continue
            ans += stack.pop()
        ans += ' '
# 이미 존재하는 경우 역으로 추가
if stack:
    for _ in range(len(stack)):
        ans += stack.pop()

print(ans)