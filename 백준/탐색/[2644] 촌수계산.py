import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())

array = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int,input().split())
    array[x].append(y)
    array[y].append(x)

visited=[False for _ in range(n+1)]
# flag -> 관계가 있는 지 여부를 판단하는 변수
flag = False


def dfs(x, count):
    global flag
    visited[x] = True
    # 자식을 찾은 경우
    if x == b:
        flag = True
        print(count)
    
    # 못찾은 경우(재귀)
    for val in array[x]:
        if visited[val] == False:
            dfs(val, count+1)

dfs(a, 0)
if flag == False:
    print(-1)

