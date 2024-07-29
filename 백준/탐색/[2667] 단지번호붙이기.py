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
    # 방문 후 0으로 변경(방문처리)
    house[x][y] = 0
    
    # 4방향 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 내 존재하고 1인 경우 
        if 0<=nx<n and 0<=ny<n and house[nx][ny] == 1:
            # 단지 내의 집 개수 1개 증가
            temp_house_cnt += 1
            # 추가 탐색
            dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if house[i][j] == 1:
            temp_house_cnt = 1
            dfs(i,j)
            # 탐색 종료 후 단지 개수 증가
            house_cnt += 1
            # 단지 내 집 개수를 배열에 추가
            house_cnt_arr.append(temp_house_cnt)

print(house_cnt)
# 오름차순 정렬
house_cnt_arr.sort()
for i in house_cnt_arr:
    print(i)

