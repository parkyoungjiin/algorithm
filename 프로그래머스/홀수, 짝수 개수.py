"""
정수가 담긴 리스트 num_list가 주어질 때,
num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.
"""

# list를 반복문으로 하나씩 꺼내서 짝수 홀수인지 판별하여 짝수일 때 짝수변수 ++, 홀수일 때 홀수변수 ++
def solution(num_list):
    #짝수 변수, 홀수 변수 선언
    odd_num, even_num = 0,0
    for i in num_list:
        if i % 2 == 0:
            even_num += 1 
        else:
            odd_num += 1
    answer = [even_num, odd_num]
    return answer

solution([1, 3, 5, 7])