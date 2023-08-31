"""
0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어집니다.
numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.
"""

def solution(numbers):
    answer = 0
    number_dict = {str(i):0 for i in range(10)}
    # print(number_dict)
    for i in numbers:
        if str(i) in number_dict:
            # print("i값 존재 : ", i)
            number_dict[str(i)] += 1

    # dict값이 0이면 그 키값을 int로 전환하여 더하기.
    for key, value in number_dict.items():
        if value == 0:
            answer += int(key)

    return answer


solution([1,2,3,4,6,7,8,0])
