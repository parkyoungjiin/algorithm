import sys
input = sys.stdin.readline

t = int(input())
def dfs(n):
    global count

    visited[n] = True
    cycle_list.append(n)

    if visited[student[n]] == True:
        if student[n] in cycle_list:
            count -= len(cycle_list[cycle_list.index(student[n]):])
        return
    else:
        dfs(student[n])



for _ in range(t):
    n = int(input())
    student = [0] + list(map(int,input().split()))
    print(student)
    visited = [0] * (n + 1)
    count = n

    for i in range(1, n+1):
        if not visited[i]:
            cycle_list = []
            dfs(i)
        
    print(count)



        
        
