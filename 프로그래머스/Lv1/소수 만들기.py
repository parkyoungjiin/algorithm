from itertools import combinations


def solution(nums):
    # 3개씩 더했을 때 소수가 되는 경우의 수를 리턴하라.
    answer = 0

    sum_num = 0

    for i in combinations(nums, 3):
        sum_num = sum(i)
        chk = True
        for j in range(2, sum_num):
            # 0으로 나눠지면 소수가 아님.
            if sum_num % j == 0:
                chk = False
                break
        if chk:
            answer += 1

    return print(answer)

solution([1,2,3,4])