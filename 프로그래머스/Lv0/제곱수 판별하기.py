"""
어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 합니다. 
정수 n이 매개변수로 주어질 때, n이 제곱수라면 1을 아니라면 2를 return하도록 solution 함수를 완성해주세요.
"""

import math


def solution(n):
    # math.sqrt(정수) : 제곱근 구해줌.
    sqrt_num = math.sqrt(n)
    print('sqrt_num:', sqrt_num)
    print('floatSqrt_num:', float(int(sqrt_num)))
    if(float(int(sqrt_num) == sqrt_num)):
        answer = 1
    else:
        answer = 2
    

    return print(answer)

solution(144)
solution(1440)