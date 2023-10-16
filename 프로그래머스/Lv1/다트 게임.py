def solution(dartResult):
    answer = 0
    score_stack = []
    dart_dict = {'S':1, 'D':2, 'T':3}
    
    # for 반복문은 한 자리씩 처리하기에 10을 별도로 A라는 숫자로 변경해주자.
    dartResult = dartResult.replace("10","A")

    for dart in dartResult:
        if dart.isnumeric() or dart == 'A':
            if dart == 'A':
                score_stack.append(10)
            else:
                score_stack.append(int(dart))
        elif dart in dart_dict:
            # print("dart는 SDT:", dart)
            score = score_stack.pop()
            score_stack.append(int(score ** dart_dict[dart]))
        elif dart == "*":
            # print("dart는 스타상")
            # 1. 처음에 나온 경우는 해당 점수만 *2
            if len(score_stack) == 1:
                score = int(score_stack.pop()) * 2
                score_stack.append(score)
            # 2. 처음이 아니면 직전 점수 * 2와 해당 점수 *2를 처리함.
            else:
                score_stack[-1] = score_stack[-1] * 2
                score_stack[-2] = score_stack[-2] * 2
        else:
            # print("dart는 아차상")
            score = score_stack.pop()
            score_stack.append(score * -1)
    return sum(score_stack)

solution("1S2D*3T")
solution("1D2S#10S")
solution("1D2S0T")
