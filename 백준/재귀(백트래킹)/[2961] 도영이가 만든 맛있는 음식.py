from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())

# 재료
ingredient = []

for _ in range(n):
    s, b = map(int, input().split())
    ingredient.append([s,b])

com = []
answer = 1000001
for i in range(1, n+1):
    com.append(combinations(ingredient,i))

for c in com:
    # combinations 내용물을 확인하려면 재출력.
    for comb in c:
        print(comb)
        sour = 1
        bitter = 0

        for e in comb:
            sour *= e[0]
            bitter += e[1]
        
        answer = min(abs(sour - bitter), answer)

print(answer)
# for i in range(n):
#     for j in range(i):
#         sour.append(ingredient[i][0] * ingredient[j][0])

# answer = 1000001
# for i in range(n):
#     for s in sour:
#         if ingredient[i][1] - s > 0:
#             answer = min(ingredient[i][1] - s, answer)

# print(answer)
