import sys
input = sys.stdin.readline

n = int(input())

height = list(map(int, input().split()))
ans = [0] * n
for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == height[i] and ans[j] ==0:
            ans[j] = i + 1
        elif ans[j] == 0:
            cnt += 1


print(ans)
