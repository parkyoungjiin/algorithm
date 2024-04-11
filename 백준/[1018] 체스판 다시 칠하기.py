import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(input().rstrip())

# 결과값 저장
result = []

# 8 * 8 배열 (시작점 i 는 행의 시작점, j는 열의 시작점)
for i in range(n-7):
    for j in range(m-7):
        white_draw = 0
        black_draw = 0

        # 시작점 ~ 시작점 + 8까지 탐색
        for x in range(i, i+8):
            for y in range(j, j+8):
                # 짝수일 때는 같아야 함.
                if (x+y) % 2 == 0:
                    if graph[x][y] != 'W':
                        white_draw += 1
                    if graph[x][y] != 'B':
                        black_draw += 1
                # 홀수 일 때는 달라야 함.
                if (x+y) % 2 == 1:
                    if graph[x][y] != 'B':
                        white_draw += 1
                    if graph[x][y] != 'W':
                        black_draw += 1
                
        result.append(min(black_draw, white_draw))

print(result)
print(min(result))



