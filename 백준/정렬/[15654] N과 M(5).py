import sys
input = sys.stdin.readline

n,m = map(int, input().split())
numbers = sorted(list(map(int,input().split())))
visited = [False] * n
result = []
def dfs():
    for i in range(n):
        if len(result) == m:
            print(*result)
            return

        if not visited[i]:
            # 방문 처리
            visited[i] = True
            # 출력을 위해서 담아두기
            result.append(numbers[i])
            dfs()
            # 다른 노드에서도 돌 수 있기에 False 처리하기
            visited[i] = False
            # 다른 노드에서도 돌 수 있기에 출력 할 리스트 요소 삭제
            result.pop()


dfs()