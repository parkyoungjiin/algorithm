import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    cloths = {}
    for _ in range(n):
        cloth, type = input().split()
        if type not in cloths.keys():
            cloths[type] = 1
        else:
            cloths[type] += 1
    answer = 1
    for i in cloths:
        answer *= (cloths[i] + 1)
    print(answer-1)