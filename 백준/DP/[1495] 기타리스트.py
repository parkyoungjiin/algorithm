import sys
input = sys.stdin.readline

n, s, m = map(int, input().split())

vol = list(map(int, input().split()))

ans = [[0] * (m+1) for i in range(n)]

for i in range(n):
    min_vol = s - vol[i]
    max_vol = s + vol[i]

    if min_vol >= 0:
        ans[i][min_vol] = 1
        s = min_vol
    if max_vol <= m:
        ans[i][max_vol] = 1
        s = max_vol
            

print(ans)