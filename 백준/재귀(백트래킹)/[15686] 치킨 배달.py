def dfs(cnt, i):
    global min_ans

    # 최대 치킨 수일 경우 return
    if cnt == m:
        ans = 0
        for h in house:
            hr, hc = h[0], h[1]
            dist = 2*n

            for c in select:
                cr, cc = c[0], c[1]
                tmp = abs(hr-cr) + abs(hc-cc)
                if tmp < dist:
                    dist = tmp
            ans += dist
        if ans < min_ans:
            min_ans = min(ans, min_ans)
            return
                
    # 고른 치킨 집 제외하고 dfs
    for idx in range(i, len(chickn)):
        select.append(chickn[idx])
        dfs(cnt+1, idx+1)
        select.pop()



import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

# 치킨집
chickn = []
# 집
house = []
#
select = []

# 최소 결과 값
min_ans = float('inf')
# 1인 경우 house, 2인 경우 chickn 배열에 위치 정보를 넣는다.
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chickn.append((i,j))
        elif graph[i][j] == 1:
            house.append((i,j))


for t in range(len(chickn)):
    dfs(0, t)
    
print(min_ans)
        
