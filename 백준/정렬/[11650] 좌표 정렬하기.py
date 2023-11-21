import sys
input = sys.stdin.readline

N = int(input())

location = []
for i in range(N):
    x, y = map(int,input().split())
    location.append([x, y])
location.sort()

for x, y in location:
    print(x, y)

