import sys

input = sys.stdin.readline
def dfs(a, idx):
    global answer
    # 팀원이 반씩 충원된 경우
    if a == n // 2:
        start, link = 0, 0 # 각 팀의 점수
        for i in range(n):
            for j in range(n):
                # 방문한 경우 start
                if visited[i] and visited[j]:
                    start += lst[i][j]
                # 방문하지 않은 경우 link팀
                elif not visited[i] and not visited[j]:
                    link += lst[i][j]
        answer = min(answer, abs(start - link))
        return
    # 인원 나누기
    else:
        for i in range(idx, n):
            if not visited[i]:
                visited[i] = True
                dfs(a+1, i+1)
                visited[i] = False

n = int(input())
answer = 9999999
visited = [False] * (n+1)
lst = [list(map(int, input().split())) for _ in range(n)]

dfs(0,0)
print(answer)