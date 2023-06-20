"""
문자열 my_str과 n이 매개변수로 주어질 때, my_str을 길이 n씩 잘라서 저장한 배열을 return하도록 solution 함수를 완성해주세요.

"""

def solution(my_str, n):
    answer = []
    
    for i in range(0, len(my_str), n):
        answer.append(my_str[i:i+n])

    
    return answer


solution("abc1Addfggg4556b", 6)