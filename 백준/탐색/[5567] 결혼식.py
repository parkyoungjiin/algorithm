import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    # 방문 처리
    visited[start] = True
    count = 0 # 초대 사람
    depth = 0 # 관계(2면 끝)
    

    while q:
        # 깊이 증가
        depth += 1
        for _ in range(len(q)):
            top = q.popleft()
            for i in realationship[top]:
                if not visited[i]:
                    visited[i] = True
                    q.append(i)
                    count += 1
        if depth == 2:
            print(count)
            break
        
    
    if count == 0:
        print(count)
        
n = int(input())
m = int(input())

visited = [False for _ in range(n+1)]
realationship = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    realationship[a].append(b)
    realationship[b].append(a)


bfs(1)