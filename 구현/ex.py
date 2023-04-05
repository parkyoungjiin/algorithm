# 2차원 행렬 추출 코드
for i in range(5):
    for j in range(5):
        print('(',i,',',j,')', end='')
    print()


# 동, 북, 서, 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 현재 위치
x, y = 2, 2

for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    print(nx, ny)

# 상하좌우 문제
# 가장 왼쪽 위 좌표인 (1,1)부터 시작하여 가장 오른쪽 좌표인 (N,N)가 있다. N이 5일 경우 (1,1) ~ (5,5)인 정사각형 공간
# 계획서에 하나의 줄에 띄어쓰기 기준으로 L R U D을 작성하는데 공간을 벗어나는 경우는 무시된다.
# 계획서를 통해 최종 지점을 계산하는 코드를 작성하라.

# 1. 공간 크기
n = int(input())

# 2. 계획서 내용
plans = input().split()
# L R U D
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']
start, end = 1 ,1
# 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 확인
    for i in range(len(move_type)):
        if plan == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x, y = nx, ny
print(x, y)

print('-------------')


# 정수 N 입력할 경우 00시 부터 N시 59분 59초까지의 모든 시각 중 3이 하나라도 포함되는 모든 경우의 수를 구하라.
# 모든 시각의 경우를 하나씩 세서 풀어야 하는 문제
# 시, 분, 초를 3중 반복문을 통해 판별
N = int(input())

count = 0

for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                print(str(i) + str(j) + str(k))
                count += 1

# 왕실의 나이트
# L자 형태로만 움직일 수 있음.
# -> 수평(수직)으로 2 칸 이동 후 수직(수평)으로 1 칸 이동 
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 1. 현재 위치 입력받기
location = input()
# 2. 행은 숫자이므로 2번째 인덱스에 있는 값 !
row = int(location[1])
 
# 3. a~e 아스키 코드를 숫자로 변환하는 코드 !(ord는 문자열을 아스키코드로 변환)
column = int(ord(location[0])) - int(ord('a')) + 1 # 이 식을 통해 a=1, b=2, c=3으로 치환된다.

# 4. 경우의 수를 담을 변수
result = 0

# 5. 범위를 벗어나지 않고 이동할 수 있는 경우의 수를 계산
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_column >= 1 and next_row <=8 and next_column <=8:
        result += 1

print(result)
