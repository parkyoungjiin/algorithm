"""
머쓱이는 행운의 숫자 7을 가장 좋아합니다. 
정수 배열 array가 매개변수로 주어질 때, 7이 총 몇 개 있는지 return 하도록 solution 함수를 완성해보세요.
"""

def solution(array):
    answer = 0
    # 내가 작성한 코드 : 인덱스 번지에 접근하여 Count를 사용.
    # for i in range(len(array)):
    #     answer += str(array[i]).count('7')

    # ---------풀이---------
    # answer += array.count('7') # 리스트의 경우는 count가 동작 하지 않기에 문자열로 변환!

    answer += str(array).count('7')
    return answer

solution([7, 77, 17])