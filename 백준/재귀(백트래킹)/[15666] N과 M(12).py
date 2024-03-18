n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
# visited=[False] * n
result = []
def dfs(start):
    if len(result) == m:
        print(*result)
        return
    
    temp = 0
    
    for i in range(start, n):
        if temp != numbers[i]:
            result.append(numbers[i])
            temp = numbers[i]
            dfs(i)
            result.pop()
        
dfs(0)