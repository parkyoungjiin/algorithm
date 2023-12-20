import sys
input = sys.stdin.readline
n = int(input())
spoil = sorted(list(map(int, input().split())))
result = []
sum_value = sys.maxsize #maxsize = 최대 정수
# n-2는 3개의 합을 구해야 하기 때문.
for i in range(n-2):
    start, end = i+1, n-1
    while start < end:
        temp_sum = spoil[i] + spoil[start] + spoil[end]
        # 값이 작을 수록 0에 가까운 수, 업데이트
        if abs(temp_sum) < sum_value:
            result = [spoil[i], spoil[start], spoil[end]]
            sum_value = abs(temp_sum)
        
        if temp_sum < 0:
            start += 1
        elif temp_sum > 0:
            end -= 1
        else:
            break
print(*result)

    