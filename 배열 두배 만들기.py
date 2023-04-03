"""
정수 배열 numbers가 매개변수로 주어집니다. 
numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.
"""

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        answer.append(numbers[i] * 2)
    
    return print(answer)

solution([1,2,5,6,7,8]);

numbers = [1,2,3]

# 리스트 요소를 하나씩 뽑아낼 때 사용
for n in numbers:
    print(n)