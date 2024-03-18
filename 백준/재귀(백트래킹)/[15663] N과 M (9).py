n, m = map(int, input().split())

numbers = sorted(list(map(int,input().split())))

result = []
visited = [False] * n

def dfs():
    if len(result) == m:
        print(*result)
        return
    
    before = 0    

    for i in range(n):
        # 방문하지 않은 경우(같은 수 출력 방지) -> visited && 이전 값이랑 다른 경우 (중복 수열 방지) -> before 변수
        if not visited[i] and before != numbers[i]:
            result.append(numbers[i])
            visited[i] = True
            # 변수 변경
            before = numbers[i]
            dfs()
            visited[i] = False
            result.pop()
    
    


        
    

dfs()



"""
if len(result) == m:
            print(*result)
        else:
            for j in range(i+1, len(numbers)):
                result.append(numbers[j])
                if len(result) == m:
                    print(*result)
                    result.pop()
        
        result.pop()
    print(result)
"""