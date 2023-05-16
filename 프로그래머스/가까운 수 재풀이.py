# 가장 가까운 수가 여러 개일 경우 더 작은 수를 return 합니다.
def solution(array, n):
    answer = 0
    # 오름차순 정렬하여 작은 수를 먼저 앞으로 뺀다.
    array.sort()
    box =[]
    for i in array :
        box.append(abs(n - i))
    answer = array[box.index(min(box))]
    return answer

solution([12,10,28], 20)
solution([13,10,28], 20)