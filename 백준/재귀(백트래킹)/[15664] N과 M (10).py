import sys
input = sys.stdin.readline

n, m = map(int, input().split())

num_list = sorted(list(map(int, input().split())))

temp = []

visited = [False] * n

def dfs(start):
    if len(temp) == m:
        print(*temp)
        return 
    
    remember_num = 0
    for i in range(start, n):
        if not visited[i] and remember_num != num_list[i]:
            visited[i] = True
            temp.append(num_list[i])
            remember_num = num_list[i]
            dfs(i + 1)
            visited[i] = False
            temp.pop()

dfs(0)

