import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# cost = [[0] for i in range(n+1)]
# print(cost)
cost = []
for i in range(n):
    cost.append(int(input()))

start, end = min(cost), sum(cost)

while start <= end:
    cnt = 1
    mid = (start + end) // 2
    money = mid # 인출 금액
    for c in cost:
        # 인출 금액이 음수가 되면 추가로 인출해야 하기에 기존 금액은 무시하고, mid 값으로 갱신.
        if money - c < 0:
            money = mid
            cnt += 1
        # 가진 돈 차감
        money -= c
    # 인출 횟수가 m보다 큰 경우, 인출금액이 최대금액보다 작은 경우 더 큰 값으로 갱신.
    if cnt > m or mid < max(cost):
        start = mid + 1
    else:
        end = mid -1
        ans = mid

print(ans)





    
