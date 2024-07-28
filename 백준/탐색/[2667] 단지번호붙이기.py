import sys

input = sys.stdin.readline

n = int(input())

house = []

for i in range(n):
    house.append(list(map(int,input().rstrip())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

house_cnt = 0
house_cnt_arr = []

def dfs(x, y):
    global house_cnt
    global temp_house_cnt

    house[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<n and house[nx][ny] == 1:
            temp_house_cnt += 1
            dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if house[i][j] == 1:
            temp_house_cnt = 1
            dfs(i,j)
            house_cnt += 1
            house_cnt_arr.append(temp_house_cnt)

print(house_cnt)
house_cnt_arr.sort()
for i in house_cnt_arr:
    print(i)

