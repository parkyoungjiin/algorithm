import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = sorted(list(map(int,input().split())))

# 출력 변수
result = []

def dfs(start):
    if len(result) == m:
        print(*result)
        return
    
    for i in range(start, n):
        result.append(numbers[i])
        dfs(i)
        result.pop() 


dfs(0)
