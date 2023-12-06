import sys
input = sys.stdin.readline

M, N = map(int, input().split())
snack = list(map(int,input().split()))

start, end = 1, max(snack)
result = 0
while start <= end:
    mid = (start+end) // 2
    cnt = 0
    # snack을 하나씩 꺼내서 mid로 나눈다.
    for s in snack:
        cnt += s // mid
    # 조카 수보다 많이 나눠줄 수 있을 때는 시작점을 변경하고 최대 길이를 구하는 것이므로 max 사용.
    if cnt >= M:
        result = max(result, mid)
        start = mid + 1
    else:
        end = mid - 1
print(result)
