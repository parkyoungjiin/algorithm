from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int,input().split())
limit = 100001
time = [0] * limit

q = deque()
q.append(n)

while q:
    t = q.popleft()
    # 위치 도달한 경우 리턴.
    if t == k:
        print(time[t])
        break
    # 순간이동, -1, +1 순으로 해야 틀리지 않음(우선순위를 정하고 반복문 돌기)
    for i in (t * 2, t + 1, t - 1):
        # 범위 안이고, 방문하지 않은 경우 이동.
        if 0 <= i <= 100000 and time[i] == 0:
            # 0초(순간이동) -> 시간을 갱신 하지 말아야 함.
            if i == t * 2:
                time[i] = time[t]
                q.append(i) # 순간이동이 먼저 탐색되도록 appendleft
            # 1초(걷기) -> 시간 갱신
            else:
                time[i] = time[t] + 1
                q.append(i)

            



