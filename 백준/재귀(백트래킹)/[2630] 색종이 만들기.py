import sys

input = sys.stdin.readline

n = int(input())

paper = [list(map(int,input().split())) for _ in range(n)]

result = []

def solution(x, y, n):
    # 현재 컬러
    color = paper[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            #현재 컬러와 다른 컬러인 경우 4분할 진행
            if color != paper[i][j]:
                solution(x, y, n//2) # 1사분면
                solution(x, y+n//2, n//2) # 2사분면
                solution(x+n//2, y, n//2) # 3사분면
                solution(x+n//2, y+n//2, n//2) # 4사분면
                return
    
    if color == 0:
        result.append(0)
    else:
        result.append(1)

solution(0,0,n)

print(result.count(0))
print(result.count(1))



