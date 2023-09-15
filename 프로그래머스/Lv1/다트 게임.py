def solution(dartResult):
    stack = []
    start_idx = 0
    bonus_dict = {'S': 1, 'D':2, 'T': 3}
    # 숫자를 제외한 작업 처리
    for i in range(len(dartResult)):
        op = dartResult[i]
        if op in bonus_dict:
            stack.append(int(dartResult[start_idx:i]) ** bonus_dict[op])
        # 스타상 = 직전 점수, 해당 점수 각각 2배.
        elif op == '*':
            stack[-2:] = [x * 2 for x in stack[-2:]]
        # 아차상 = 해당 점수가 마이너스 된다. (음수로 변경)
        elif op == '#':
            stack[-1] = -stack[-1]

        # 인덱스 처리
        if not op.isnumeric():
            start_idx = i + 1       
            

    return sum(stack)

solution("1S2D*3T")
# solution("1D2S#10S")
# solution("1D2S0T")