import sys
input = sys.stdin.readline
triangle=[]
n = int(input())

for _ in range(n):
    triangle.append(list(map(int,input().split())))


for i in range(1, n):
    # j = 열(층 안에서 인덱스)
    for j in range(i+1):
         # 시작, 끝은 max 연산 X
        if j == 0:
            triangle[i][j] += triangle[i-1][j]
        elif j == i:
            triangle[i][j] += triangle[i-1][j-1]
        # 가운데 요소들 연산할 때는 겹치기에 Max로 큰 값을 저장. 
        else:
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
print(triangle)
print(max(max(triangle)))



