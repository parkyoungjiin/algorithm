from collections import deque


def solution(ingredient):
    answer = 0
    temp = []
    for i in ingredient:
        # 임시 배열에 넣기
        temp.append(i)

    for i in range(len(temp)):
        if ingredient[i:i+4] == [1,2,3,1]:
            answer += 1
            # pop
            for i in range(i, i+4):
                temp.pop(i)
                ingredient = temp
        
    return print(answer)


solution([2, 1, 1, 2, 3, 1, 2, 3, 1])

