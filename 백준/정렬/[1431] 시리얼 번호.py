import sys
input = sys.stdin.readline
# N <= 50
N = int(input())

# 정렬 기준 3개
# 1. 길이가 짧은 것이 먼저
# 2. 자릿수 합 비교하여 작은 합이 먼저
# 3. 사전순 비교


def number_sum(x):
    res = 0
    for i in x:
        if i.isdigit():
            res += int(i)
    return res
        

serial = []

for _ in range(N):
    serial.append(input().strip())

serial.sort(key=lambda x:(len(x), number_sum(x) , x))

for s in serial:
    print(s)

