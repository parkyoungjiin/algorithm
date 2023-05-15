"""
정수 배열 array와 정수 n이 매개변수로 주어질 때,
array에 들어있는 정수 중 n과 가장 가까운 수를 return 하도록 solution 함수를 완성해주세요.

가장 가까운 수가 여러 개일 경우 더 작은 수를 return 합니다.
"""

# array 요소 하나씩 n과 - 연산 후 저장된 값을 배열에 저장한다. 이후 절대값(abs)으로 가장 적은 값을 return
def solution(array, n):
    array.sort()
    box = []
    
    answer = []
    for i in array:
        box.append(abs(n-i))
    print(box)

    # box에서의 절대값이 가장 작은 번지에 접근한 값을 answer에 넣기 
    answer = [array[box.index(min(box))]]
    if len(answer) > 1:
        return print(min(answer))
    else:
        return print(answer[0])
    

    

solution([12, 10, 28], 20)
solution([10, 11, 12], 13)

"""
test_arr = []
array.sort()
print(array)
for i in array:
    test_arr.append(abs(n-i))
print(test_arr)
    index_val = box.index(answer)

    answer = array[index_val]
"""

# 정렬 미사용 시 같은 값이 2개일 경우 풀이가 어렵네
    