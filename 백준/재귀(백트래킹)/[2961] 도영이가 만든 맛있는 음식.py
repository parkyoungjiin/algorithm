import sys
input = sys.stdin.readline

n = int(input())

def dfs(depth, start):
    global result
    # 개수 만큼 뽑은 경우
    if depth == lenght:
        # 신맛(곱)
        bitter = 1
        # 쓴맛(합)
        sour = 0
        for i in arr:
            bitter *= i[0]
            sour += i[1]
            if abs(bitter - sour) < result:
                result = abs(bitter - sour)
        return

    
    # 재귀
    for i in range(start, n):
        arr.append(ingredient[i])
        dfs(depth + 1, start + 1)
        arr.pop()
# 재료
ingredient = []

for _ in range(n):
    s, b = map(int, input().split())
    ingredient.append([s,b])

# 재료 임시 보관 배열
arr = []
result = float('inf')

for i in range(1, n+1):  # i = 1~n개 (뽑는 개수)
    lenght = i
    dfs(0, 0)

print(result)
# 재귀
