"""
어떤 세균은 1시간에 두배만큼 증식한다고 합니다. 
처음 세균의 마리수 n과 경과한 시간 t가 매개변수로 주어질 때 t시간 후 세균의 수를 return하도록 solution 함수를 완성해주세요.
"""

# 2마리가 10시간 지났을 때 몇마리인가 여기서 1시간이 지날 때 마다 2배 증가.


def solution(n, t):
    answer = 2**t * n  
    return print(answer)

solution(2,10)
solution(7,15)