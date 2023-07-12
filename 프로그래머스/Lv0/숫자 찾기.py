"""
정수 num과 k가 매개변수로 주어질 때, 
num을 이루는 숫자 중에 k가 있으면 num의 그 숫자가 있는 자리 수를 return하고 없으면 -1을 return 하도록 solution 함수를 완성해보세요.
"""

def solution(num, k):
    
    answer = 0
    # 1. 리스트로 변환하여 사용한 풀이
    """
    num = list(str(num))
    if str(k) in num:
        answer = num.index(str(k))+1
    else:
        answer = -1
    return answer
    """

    # 2. enumerate 사용한 풀이
    # i에는 인덱스번호, j에는 원소값이 들어감.
    for i, j in enumerate(str(num)):
        if str(k) == j:
            return i + 1
         
    return -1

solution(29183, 1)
solution(123456, 7)