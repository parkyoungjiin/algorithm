"""
영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류합니다. 
문자열 my_string이 매개변수로 주어질 때 모음을 제거한 문자열을 return하도록 solution 함수를 완성해주세요.
# 1. 매개변수를 배열로 넣어서 해결하기
# 
"""

def solution(my_string):

    type = ['a','e','i','o','u']
        
    for i in type:
        # 모음이 존재할 경우 my-String에서 제거
        if i in my_string:
            #제거하기..
            my_string = my_string.replace(i,"")
    return my_string

solution("bus")
solution("nice to meet you")