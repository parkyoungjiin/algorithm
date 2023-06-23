"""
한 개 이상의 항의 합으로 이루어진 식을 다항식이라고 합니다.
 다항식을 계산할 때는 동류항끼리 계산해 정리합니다. 
 덧셈으로 이루어진 다항식 polynomial이 매개변수로 주어질 때,
   동류항끼리 더한 결괏값을 문자열로 return 하도록 solution 함수를 완성해보세요. 
   같은 식이라면 가장 짧은 수식을 return 합니다.


"""

def solution(polynomial):
    polynomial = polynomial.split(" + ")
    answer = ""
    x, num =0, 0
    for i in polynomial:
        # x가 들어있으면 앞의 숫자를 더하고 상수일 경우 num에 값을 추가함.
        if 'x' in i:
            # 길이가 1이면 인자값이 없기에 1을 더한다.
            if len(i) == 1:
                x += 1
            else:
                # x += int(i[0]) -> 이 코드는 x의 인자가 1자리인 경우만 고려한 코드임.
                x += int(i[:-1])
            
        else:
            num += int(i)
    # print("x:", x, "num:", num)

    # 1. 처음 풀이

    # if x > 1 and num > 0:
    #     answer = str(x) + "x + " + str(num)
    # elif x > 1 and num == 0:
    #     answer = str(x) + "x"
    # elif x == 1 and num == 0:
    #     answer = 'x'
    # elif x == 0 and num > 0:
    #     answer = str(num)
    # elif x == 1 and num > 0:
    #     answer = 'x + ' +str(num)
    # elif x == 0 and num == 0:
    #     answer = '0'
    

    #------------------
    # 2번째 풀이(if문을 간소화하였음)
    # 1. x 가 0일 때, num이 0일경우, 1보다 클경우
    if x == 0:
        return '0' if num == 0 else str(num)
    # 2. x 가 1일 때
    elif x == 1:
        return 'x' if num == 0 else 'x + ' + str(num)
    # 3. x가 1 이상일 때
    elif x > 1:
        return str(x) + "x" if num == 0 else str(x) + "x + " + str(num)



    

solution("3x + 7 + x")
solution("10x + 7 + x")
solution("x + x + x")
solution("x")
solution("x + 7")
solution("7 + 5")
solution("1 + 1")