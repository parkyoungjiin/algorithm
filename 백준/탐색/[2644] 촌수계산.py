# 사람 수
n = int(input())

# 계산해야하는 촌수
start, end= map(int, input().split())

family = [[] for i in range(n+1)]
visited = [False] * (n+1)
cnt = [0] * (n+1) # 촌수 계산 
# 관계 개수
m = int(input())
# family (관계) 그래프 내용 추가
for _ in range(m):
    parent, child = map(int,input().split())
    family[parent].append(child)
    family[child].append(parent)
# print(family)

# dfs 탐색
def dfs(s):
    # 방문하기
    visited[s] = True
    for i in family[s]:
        if not visited[i]:
            cnt[i] = cnt[s] + 1
            dfs(i)
    # print(cnt)

dfs(start)
 
if cnt[end] > 0:
    print(cnt[end])
else:
    print(-1)
    