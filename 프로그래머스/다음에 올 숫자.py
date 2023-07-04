"""
등차수열 혹은 등비수열 common이 매개변수로 주어질 때,
 마지막 원소 다음으로 올 숫자를 return 하도록 solution 함수를 완성해보세요.

 
"""

def solution(common):
    answer = 0
    # 등차 수열
    if common[1]-common[0] == common[2] - common[1]:
        answer = common[-1]+(common[1]-common[0])
    # 등비 수열
    elif common[1]/common[0] == common[2]/common[1]:
        answer = common[-1]*(common[1]/common[0])
    return answer

solution([1, 2, 3, 4])
solution([2,4,8])