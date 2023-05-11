"""
i팩토리얼 (i!)은 1부터 i까지 정수의 곱을 의미합니다. 
예를들어 5! = 5 * 4 * 3 * 2 * 1 = 120 입니다. 
정수 n이 주어질 때 다음 조건을 만족하는 가장 큰 정수 i를 return 하도록 solution 함수를 완성해주세요.
"""

from math import factorial


def solution(n):
    answer = 0
    # 반복문을 통해서 팩토리얼이 n을 안넘는 최대의 값을 찾으면 된다.
    for i in range(1,n+1):
        if n < factorial(i):
            break
        else:
            answer = i
    k = 10
    
    return answer

solution(3628800)
# 재귀함수를 이용한 팩토리얼
def solution2(n):
    #1팩토리얼은 1이기에 1보다 큰 경우로 조건절을 작성함.
    if (n>1):
        return n * factorial(n-1)
    else:
        return 1
    
a = int(input("팩토리얼 숫자 입력하시오 : "))
print(solution2(a))