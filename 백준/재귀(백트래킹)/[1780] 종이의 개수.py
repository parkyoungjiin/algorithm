import sys
input = sys.stdin.readline

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
# for _ in range(n):
#     graph.append(list(map(int,input().split())))

cnt = [0, 0, 0]
def dfs(x, y, n):
    current_color = graph[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if current_color != graph[i][j]:
                # 색 다른 경우 3방향 재귀
                for a in range(3):
                    for b in range(3):
                        dfs(x + (n//3)*a, y + (n//3)*b, n//3)
                return
    
    if current_color == 1:
        cnt[1] += 1
    elif current_color == -1:
        cnt[0] += 1
    else:
        cnt[2] += 1
dfs(0, 0, n)
print(cnt)
