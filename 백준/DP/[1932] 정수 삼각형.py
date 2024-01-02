import sys
input = sys.stdin.readline

n = int(input())
circle = []
for _ in range(n):
    circle.append(list(map(int,input().split())))

# 점화식
# 행
for i in range(1, n):
    for j in range(0,i+1):
        if j == 0:
            circle[i][0] += circle[i-1][0]
        elif j == i:
            circle[i][j] += circle[i-1][j-1]
        else:
            circle[i][j] += max(circle[i-1][j-1], circle[i-1][j])

print(max(circle[n-1]))
