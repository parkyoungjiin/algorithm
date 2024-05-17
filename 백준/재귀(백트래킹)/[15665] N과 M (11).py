import sys
input = sys.stdin.readline

n, m = map(int, input().split())

num_list = sorted(list(map(int, input().split())))

temp = []
def dfs():
    if len(temp) == m:
        print(*temp)
        return
    
    remember_num = 0

    for i in range(n):
        if remember_num != num_list[i]:
            temp.append(num_list[i])
            remember_num = num_list[i]
            dfs()
            temp.pop()

dfs()