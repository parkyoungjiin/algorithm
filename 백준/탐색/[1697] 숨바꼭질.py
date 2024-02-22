from collections import deque
n, k = map(int,input().split())

array = [0] * 100001

def bfs():
    q = deque()
    # 시작점 넣고 시작.
    q.append(n)

    while q:
        x = q.popleft()
        # x가 동생 위치k와 같다면 종료.
        if x == k:
            print(array[x])
            break
        # 3방향 탐색
        for j in (x-1, x+1, x*2):
            # 방문X, 범위 내
            if 0<=j<=100000 and not array[j]: # 0
                array[j] = array[x] + 1
                q.append(j)

bfs()










