import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [[False] * m for i in range(n)]

campus = []
for i in range(n):
    row = list(input().rstrip())
    # 도연 위치 저장
    if 'I' in row:
        start, end = i, row.index('I')

    campus.append(row)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

cnt = 0

q = deque([(start, end)])
visited[start][end] = True

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = dx[i] + x 
        ny = dy[i] + y

        if 0 <= nx < n and 0 <= ny < m:
            if campus[nx][ny] != 'X' and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
                if campus[nx][ny] == 'P':
                    cnt += 1

if cnt == 0:
    print('TT')
else:
    print(cnt)
        



        

