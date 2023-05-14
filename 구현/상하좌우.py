type = ['L', 'R', 'U', 'D']

# 첫째 줄 : 공간의 크기 N
N = int(input("공간 크기: "))
# 둘째 줄 : 이동할 계획서 (공백기준으로 분리)
plans = input("이동 계획서: ").split()
x,y = 1,1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 조건
# 1. N * N 을 벗어나는 움직임은 무시
# 2. 최종 도착지점을 return

# 1. 계획서를 for
for plan in plans:
    for i in range(len(type)):
        if plan == type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간 벗어나면 무시
    if nx > 1 or nx > N or ny > 1 or ny > N:
        continue
    x,y = nx, ny
print(x,y)
    
            
    

