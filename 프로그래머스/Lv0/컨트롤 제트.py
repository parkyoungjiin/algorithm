"""
숫자와 "Z"가 공백으로 구분되어 담긴 문자열이 주어집니다. 
문자열에 있는 숫자를 차례대로 더하려고 합니다. 이 때 "Z"가 나오면 바로 전에 더했던 숫자를 뺀다는 뜻입니다.
 숫자와 "Z"로 이루어진 문자열 s가 주어질 때, 머쓱이가 구한 값을 return 하도록 solution 함수를 완성해보세요.
"""
def solution(s):
    answer = 0
    # 공백 기준 문자열 분리
    s = s.split()
    # enumerate를 사용하여 인덱스로 접근한 뒤 answer를 계산.
    for i, val in enumerate(s):
        if val == 'Z':
            answer -= int(s[i-1])
        else:
            val = int(val)
            answer += val
            
    
    return answer
    
    
    
solution("1 2 Z 3")
solution("10 20 30 40")
solution("-1 -2 -3 Z")

# 다른 사람들 풀이
# 1. append와 pop 을 사용한 뒤 마지막에 sum()함수를 통해 배열에 있는 모든 값을 합쳤음.