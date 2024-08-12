from collections import deque
import sys

input = sys.stdin.readline

def bfs():
    global cnt
    
    while q:
        x = q.popleft()
        # 종료조건
        if x == k:
            print(dist[x])
            return

        for nx in (x*2, x-1, x+1):
            if 0<=nx<=MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                q.append(nx)      

n, k = map(int, input().split())

q = deque()

q.append(n)
# cnt = 0
MAX = 10 ** 5
# 시간초 계산 리스트
dist = [0] * (MAX+1)


bfs()
