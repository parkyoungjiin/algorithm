import sys

input = sys.stdin.readline

r, c = map(int, input().split())
island = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for _ in range(r):
    island.append(list(input().rstrip()))

cp_island = island.copy()
for x in range(r):
    for y in range(c):
        if island[x][y] == 'X':
            count = 0
            for z in range(4):
                nx = dx[z] + x
                ny = dy[z] + y
                # 범위가 벗어나면 바다로 간주-> count + 1
                if 0 > nx or nx >= r or 0 > ny or ny >= c:
                    count += 1
                
                # 바다인 경우 +1
                elif island[nx][ny] == '.':
                    count += 1
            if count == 3:
                cp_island[x][y] = '.'

x1 = 0
y1 = c-1
x2 = 0
y2 = 0
# 지도 범위 구하기
for i in range(0, r):
    if 'X' in cp_island[i]:
        x1 = i
        break
for i in range(r-1, -1, -1):
    if 'X' in cp_island[i]:
        x2 = i
        break

for i in range(x1, x2+1):
    for j in range(c):
        if cp_island[i][j] == 'X':
            y1 = min(y1, j)
            y2 = max(y2, j)

print(x1, x2, y1, y2)

for i in range(x1, x2+1):
    for j in range(y1, y2+1):
        print(cp_island[i][j], end='')
    print()