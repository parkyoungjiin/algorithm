def solution(array, commands):
    answer = []
    for i,j,k in commands:
        answer.append(sorted(array[i-1:j])[k-1])
        # print(i,j,k)
    return answer


solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])