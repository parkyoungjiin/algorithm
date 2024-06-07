import sys
input = sys.stdin.readline


N = int(input())
budget = sorted(list(map(int,input().split())))
M = int(input())

budget = sorted(budget)
start, end = 0, max(budget)
# 지방 예산 합이 총 예산보다 작거나 같은 경우 
# => 모두 배정 가능하기에 최대 값 출력.
if sum(budget) <= M:
    print(max(budget))
    
# 이분탐색 시작.
else:
    while start <= end:
        total_budget = 0
        mid = (start + end) // 2
        for i in budget:
            total_budget += min(mid, i) # mid, 예산의 최소값을 지방 전체예산에 더한다.

        # 지방 전체예산 > 총 예산
        # -> 끝 = 중간 - 1
        if total_budget > M:
            end = mid - 1
        # 지방 전체예산 <= 총 예산
        # -> 시작 = 중간 + 1
        else:
            start = mid + 1
            
    print(end)

        
        




