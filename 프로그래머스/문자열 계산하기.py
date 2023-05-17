"""
my_string은 "3 + 5"처럼 문자열로 된 수식입니다. 
문자열 my_string이 매개변수로 주어질 때, 
수식을 계산한 값을 return 하는 solution 함수를 완성해주세요.
"""

def solution(my_string):
    answer = 0
    # 리스트에 담기
    
    # 1. 내가 푼 풀이 : 0,1,2번지만 있다는 가정하에 풀이 정답.
    # 연산이 더 많을 경우 풀어지지 않음.
    """
     # 리스트 변환(공백기준으로)
    my_string = my_string.split()

    if '+' in my_string:
        answer = int(my_string[0]) + int(my_string[2])
    elif '-' in my_string:
        answer = int(my_string[0]) - int(my_string[2])
    """
    # 2. 다른 사람 풀이(블로그)

    """
    # 리스트 변환(공백기준으로)
    my_string = my_string.split()
    # 증감 연산자 사용을 위해, 첫 번째 값은 변수에 저장하고 시작.
    answer = int(my_string[0])
    # 연산자의 경우 1번지를 기준으로 2칸 간격으로 리스트에 담기기에 +, - 판별하여 증감작업.
    for i in range(1,len(my_string), 2):
        if my_string[i] == '+':
            answer += int(my_string[i+1])
        else:
            answer -= int(my_string[i+1])
    """
    # 3. eval() 함수 사용
    # - 파라미터 : 문자열
    # - 문자열로 받은 수식을 계산ㅇ하여 결과 반환
    answer = eval(my_string)
     
    return print(answer)

solution("3 + 4")
solution("32 + 23 + 22")
solution("22 - 11")