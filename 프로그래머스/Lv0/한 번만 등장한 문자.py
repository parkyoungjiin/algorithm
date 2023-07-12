"""
문자열 s가 매개변수로 주어집니다. 
s에서 한 번만 등장하는 문자를 사전 순으로 정렬한 문자열을 return 하도록 
count를 사용.
solution 함수를 완성해보세요. 한 번만 등장하는 문자가 없을 경우 빈 문자열을 return 합니다.

제한사항
- 0 < s의 길이 < 1,000
- s는 소문자로만 이루어져 있습니다.
"""

def solution(s):
    s = list(s)
    temp = []
    answer = ''
    for i in s:
        # 한 번만 등장하는 문자를 answer에 담고, 2번 이상 등장하는 경우는 필요없음. 
        if s.count(i) >=2 :
            continue
        else:
            answer += i

    return ''.join(sorted(answer))


# 다른 사람 풀이 (애초에 알파벳별로 정렬하여 sort, join을 사용하지 않음.)

def solution2(s):
    answer = ''
    for c in 'abcdefghijklmnopqrstuvwxyz':
        if s.count(c) == 1:
            answer += c
    return answer
solution("abcabcadc")
solution("abdc")