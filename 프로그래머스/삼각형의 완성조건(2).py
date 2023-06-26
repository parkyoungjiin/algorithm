"""
선분 세 개로 삼각형을 만들기 위해서는 다음과 같은 조건을 만족해야 합니다.

가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.
삼각형의 두 변의 길이가 담긴 배열 sides이 매개변수로 주어집니다. 
나머지 한 변이 될 수 있는 정수의 개수를 return하도록 solution 함수를 완성해주세요.

조건1. sides의 max값이 가장 긴 경우 / 조건2. 다른 c의 값이 가장 긴 경우

"""


def solution(sides):
    answer = 0
    sides = sorted(sides)
    sum_val = sum(sides)
    min_val = min(sides)
    max_val = max(sides)
    print(sum_val, min_val, max_val)
    # sides의 max값이 가장 긴 경우 max_val은 min_val + x 보다 작아야함.
    for i in range((max_val - min_val)+1, max_val):
        # print(i)
        answer += 1

    # x의 값이 가장 긴경우 = 두 길이보다 작고, 두 변보다는 길어야 함.
    for i in range(max_val, sum_val):
        # print(i)
        answer += 1
    return print('answer:',answer)


solution([1, 2])
solution([11, 7])