# Breath First Search (BFS) 알고리즘
# -> 가장 가까운 노드들부터
from collections import deque

# graph 변수에 인접한 노드 정보를 저장
graph = [[], [2, 3, 8], [1,7], [1,4,5], [3,5], [3,4],[7],[2,6,8],[1,7] ]

def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    visited[start] = True
    while queue:
        #popleft -> deque 앞의 값 삭제 후 반환  / pop -> deque 뒤쪽 값 삭제
        # 큐 자료구조의 맨 앞의 값을 꺼내는 작업
        v = queue.popleft()
        print(v, end='')
        for i in graph[v]:
            # 꺼낸 v 노드의 인접한 값들 중 방문하지 않은 값들을 큐에 넣어줌.
            if not visited[i]:
                queue.append(i)
                # 방문 처리
                visited[i] = True

visited = [False] * 9
bfs(graph, 1, visited)
