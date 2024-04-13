while True:
    a = input()
    stack = []

    if a == ".":
        break

    for i in a:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                # 스택의 마지막번지 값이 대괄호가 아닌 경우 ] 값을 넣는다.
                stack.append(i)
                break
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                # 스택의 마지막번지 값이 중괄호가 아닌 경우 ) 값을 넣는다.
                stack.append(i)
                break
    
    if len(stack) == 0:
        print('yes')
    # 스택에 남아 있으면 짝이 맞지 않은 괄호가 있었다는 뜻이기에 NO
    else:
        print('no')
        