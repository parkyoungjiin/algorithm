def solution(dot):
    # 음수 카운트 변수, 양수 카운트 변수
    num = []
    # 결과 변수
    answer = 0
    
    for i in dot:
        if i > 0:
            print("양수입니다.")
            num.append(1)
        elif i <0:
            print("음수입니다.")
            num.append(-1)
    for i in num:
        answer += i
    if answer == 2:
        answer = 1
    elif answer == 0:
        # 0번지가 양수일 때는 제4사분면
        if num[0] > 0:
            answer = 4
        # 0번지가 음수일 때는 제2사분면
        else:
            answer = 2
    elif answer == -2:
        answer =3

    
    return answer

solution([2,4])
solution([-2,4])


# 코드 간소화

def solution2(dot):
    if dot[0] > 0 and dot[1] > 0:
        return 1
    elif dot[0] > 0 and dot[1] < 0 :
        return 4
    elif dot[0] < 0 and dot[1] > 0 :
        return 2
    else :
        return 3