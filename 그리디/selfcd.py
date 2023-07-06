"""
# 거스름돈 (그리디)
n = int(input())
coin_type = [500, 100, 50, 10]
cnt = 0
# 타입별로 나누고 몫은 개수로, 나머지는 또 나누기.
for i in coin_type:
    # 코인 개수
    cnt += n // i

    # 나머지 금액
    n %= i

print(cnt)
"""


# 큰 수의 법칙

n,m,k = map(int,input().split())
result = 0
# m 은 총 더하는 횟수, k는 연속 횟수
numlist = list(map(int, input().split()))
numlist.sort()
while m > 0:
    for i in range(k):
        if m == 0:
            break
        result += numlist[-1]
        m -= 1
    if m == 0:
        break
    result += numlist[-2]
    m -= 1

print(result)






