import sys
input = sys.stdin.readline

n, m = map(int, input().split())

for i in range(n, m+1):
    if i == 1:
        continue
    # 2~i의 제곱근까지 판별을 해도 됨.
    for j in range(2, int(i**0.5)+1):
        # 소수 판별
        if i % j == 0:
            break
    else:
        print(i)
