"""
이진수를 의미하는 두 개의 문자열 bin1과 bin2가 매개변수로 주어질 때, 
두 이진수의 합을 return하도록 solution 함수를 완성해주세요.

1. 2진수 -> 10진수 변환 후 10진수를 2진수로


"""

def solution(bin1, bin2):
    answer = ''
    bin1 = int(bin1, 2)
    bin2 = int(bin2, 2)
    result = bin(bin1 + bin2)
    answer = result[2:]
    return print(answer)


solution("10", "11")
solution("1001", "1111")