"""
군 전략가 머쓱이는 전쟁 중 적군이 다음과 같은 암호 체계를 사용한다는 것을 알아냈습니다.

암호화된 문자열 cipher를 주고받습니다.
그 문자열에서 code의 배수 번째 글자만 진짜 암호입니다.
문자열 cipher와 정수 code가 매개변수로 주어질 때 해독된 암호 문자열을 return하도록 solution 함수를 완성해주세요.
"""

def solution(cipher, code):
    answer = ''
    # 인덱스 접근을 위해 list로 변경
    cipher = list(cipher)
    # code 배수 번째 글자만 추출하여 answer에 넣기.(range 사용)
    for i in range(code-1,len(cipher),code):
        answer += cipher[i]
    return answer

# 다른 풀이(슬라이싱 사용, 문자열로 바로 처리 가능함.)
def solution2(cipher, code):
   answer = cipher[code-1::code]
   return print(answer)

solution2("dfjardstddetckdaccccdegk",4)
solution2("pfqallllabwaoclk", 2)