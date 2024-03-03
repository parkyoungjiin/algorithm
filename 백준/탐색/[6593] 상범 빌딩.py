from collections import deque
import sys

input = sys.stdin.readline

l, r, c = map(int, input().split())

dz = [0, 0, 0, 0, 1, -1]
dr = [1, 0, -1, 0, 0, 0]
dc = [0, 1, 0, -1, 0, 0]



building = []
for _ in range(l):
        building.append([list(input().strip()) for _ in range(r)])
        temp = input()
print(building)
q = deque()
answer = 0

# 시작, 끝점 찾기
for i in range(l):
        for j in range(r):
                for k in range(c):
                        if building[i][j][k] == 'S':
                                q.append([i,j,k])
                        if building[i][j][k] == 'E':
                                end = (i,j,k)

while q:
        z, x, y = q.popleft()
        # 끝점인 경우
        if (z,x,y) == end:
                print('Escaped in {0} minutes(s).'.format(answer))
        
        for i in range(6):
                nz = z + dz[i]
                nr = r + dr[i]
                nc = c + dc[i]

                if 0 <= nz < l and 0 <= nr < r and 0 <= nc < c:
                        


