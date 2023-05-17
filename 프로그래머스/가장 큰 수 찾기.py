"""
정수 배열 array가 매개변수로 주어질 때, 
가장 큰 수와 그 수의 인덱스를 담은 배열을 return 하도록 solution 함수를 완성해보세요.
"""

def solution(array):
    answer = []

    answer.append(max(array))
    answer.append(array.index(max(array)))
    
    return print(answer)

solution([1, 8, 3])
solution([9, 10, 11, 8])