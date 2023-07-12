"""
문자열 my_string이 매개변수로 주어집니다.
 my_string에서 중복된 문자를 제거하고 하나의 문자만 남긴 문자열을 return하도록 solution 함수를 완성해주세요.
"""

def solution(my_string):
    answer = ''
    
    for i in my_string:
        if i not in answer:
            # 문자열 증감해도 문자가 결합된다..
            # 나는 배열에다가 넣은 뒤에 ''.join으로 풀이했음.
            answer += i
        
    return print(answer)

solution("people")
solution("We are the world")