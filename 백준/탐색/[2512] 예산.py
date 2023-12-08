import sys
input = sys.stdin.readline


N = int(input())
budget = sorted(list(map(int,input().split())))
M = int(input())

# 시작점 =0, 끝점 = 가장 큰 값.
start, end = 0, max(budget)

# 상한액 찾기.
while start <= end:
    mid = (start + end) // 2
    sum_budget = 0
    for b in budget:         
        if b > mid:
            sum_budget += mid
        else:
            sum_budget += b
    # 상한 기준으로 총 금액이 예산보다 큰 경우
    # -> end = mid-1
    if sum_budget > M:
        end = mid -1
    else:
        start = mid + 1
    print(end)
    # print(sum_budget)
    
