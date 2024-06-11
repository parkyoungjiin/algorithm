import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

relation = [list(input().rstrip()) for _ in range(n)]

friend = [[0] * n for _ in range(n)] # 친구 관계를 0으로 초기화한 후 Y일 때 해당 번지에 1로 변경.

for i in range(n):
    for j in range(n):
        if relation[i][j] == 'Y':
            friend[i][j] = 1

print(friend)

def bfs(n, i):
    check = [0] * n
    check[i] = 1

    q = deque([(i,0)]) # q -> index, cnt

    count = 0

    while q:
        j, cnt = q.popleft()
        if cnt >= 2:
            continue
        
        for k in range(n):
            if not check[k] and friend[j][k]:
                count += 1
                check[k] = 1
                q.append((k, cnt+1))
    return count

for i in range(n):
    res = max(res, bfs(n, i))

print(res)