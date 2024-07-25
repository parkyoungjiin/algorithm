import sys
input = sys.stdin.readline

n = int(input())

meetting = []
for _ in range(n):
    meetting.append(list(map(int, input().split())))

meetting = sorted(meetting)

s, e = meetting[0][0], meetting[n-1][1]

print(s, e)
