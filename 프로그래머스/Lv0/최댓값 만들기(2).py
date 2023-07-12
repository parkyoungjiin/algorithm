"""
정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.


"""

def solution(numbers):
    answer = 0
    
    answer1 = sorted(numbers)[0] * sorted(numbers)[1]
    answer2 = sorted(numbers)[-1] * sorted(numbers)[-2]
    
    # max 함수가 떠오르지 않아서, if로 분기함.
    """
    if(answer1 > answer2):
        answer = answer1        
    else:
        answer = answer2
    """
        
    # max 사용 후
    answer = max(answer1, answer2)
    return answer


solution([1, 2, -3, 4, -5])
solution([0, -31, 24, 10, 1, 9])