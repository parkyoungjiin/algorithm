"""
문자열 my_string이 매개변수로 주어집니다.
my_string은 소문자, 대문자, 자연수로만 구성되어있습니다. my_string안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.
"""

"""

def solution(my_string):
    for i in my_string:
        if i.isalpha():
            my_string = my_string.replace(i, " ")
    my_string = my_string.split()
    return sum(list(map(int,my_string)))
"""


# 이 풀이는 숫자인경우 문자열결합을 통해 숫자를 붙여준다.
# 숫자가 아닌 경우는 answer에 더하고, "0"으로 초기화함.
"""
def solution(my_string):
    intch = "0"
    answer = 0
    for ch in my_string:
        if ch.isdigit():
            intch += ch
        else:
            print(intch)
            answer += int(intch)
            intch = "0"
    answer += int(intch)
    return print(answer)
"""
solution("aAb1B2cC34oOp")