"""
문자열 my_string이 매개변수로 주어집니다. 
my_string안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.


1. 자연수인지 아닌 지 판별하기
-  정수로 변환했을 떄 가능하면 더하고, 아니면 빼기.

2. 자연수인 경우만 더하기.

"""

# isdigit 활용
def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isdigit():
            answer += int(i)
    
    return answer

# try except 활용

def solution2(my_string):
    answer = 0
    for i in my_string:
        try:
            answer = answer + int(i)
        except:
            pass
    return print(answer)


solution("aAb1B2cC34oOp")
solution("1a2b3c4d123")
solution2("aAb1B2cC34oOp")
solution2("1a2b3c4d123")