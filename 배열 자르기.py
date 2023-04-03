"""
정수 배열 numbers와 정수 num1, num2가 매개변수로 주어질 때,
numbers의 num1번 째 인덱스부터 num2번째 인덱스까지 자른 정수 배열을 return 하도록 solution 함수를 완성해보세요.
 1. 슬라이스 사용
 list[시작:끝]
 2. 내가 풀이한 방법(for 반복문으로 새로운 배열에 집어넣기)
"""

def solution(numbers, num1, num2):
    answer = []
    for i in range(num1, num2 + 1):
        answer.append(numbers[i])
    return answer

solution([1,2,3,4,5],1,3)