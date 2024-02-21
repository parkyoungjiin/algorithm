# 틀린 코드(메모리 초과)
# import sys

# from collections import deque

# n, k = map(int,input().split())
# limit = 100001
# visited = [[] for _ in range(limit)]

# q = deque()
# q.append(n)

# while q:
#     x = q.popleft()
#     if len(visited[x]) == 0:
#         visited[x].append(x)
#     # 동생 위치
#     if x == k:
#         print(len(visited[x])-1)
#         print(*visited[x])
#         break
    
#     for i in (x*2, x-1, x+1):
#         if 0 <= i < limit and len(visited[i]) == 0:
#             visited[i] = visited[x].copy()
#             visited[i].append(i)
#             q.append(i)


# 정답 코드(풀이 참조함)
import sys

from collections import deque

n, k = map(int,input().split())
limit = 100001
# {현 위치 : 시간}
time = {n:0}
# 경로 역추적을 위한 현재 인덱스의 이전 위치를 저장함.
visited = [[] for _ in range(limit)]

# 시간
cnt = 0

q = deque()
q.append(n)

# 경로 역추적 함수
def get_path(moved):
    path = []
    temp = moved
    for i in range(time[moved] + 1):
        path.append(str(temp))
        temp = visited[temp]
    return " ".join(path[::-1])


while q:
    x = q.popleft()
    cnt = time[x]
    # 동생 위치
    if x == k:
        print(cnt)
        print(get_path(x))
        break

    # 시간 증가
    cnt += 1
    for i in (x*2, x-1, x+1):
        # 범위 내 & 시간이 0초인 경우(방문X)
        if 0 <= i < limit and time.get(i, 0) == 0:
            # 시간 넣기
            time[i] = cnt
            # 부모 위치 넣기
            visited[i] = x
            q.append(i)
