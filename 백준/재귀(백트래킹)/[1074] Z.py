import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())
# 방문여부 저장 -> 시간 초과 발생(틀림)
# arr = [[0]*(2**n) for _ in range(2**n)]

# 분할 탐색
answer = 0
while n != 0:
    # 4등분을 위해 -1 해줌.
    n -= 1
    size = 2**n

    # 1사분면
    if r < size and c < size:
        pass

    # 2사분면
    elif r < size and c >= size:4
        # size * size -> 분할된 사분면의 총 원소(셀)의 수 계산.
        answer += size * size
        c -= size
    
    # 3사분면(행은 4등분 한 값보다 크고, 열은 4등분한 값보다 작은 경우)
    elif r >= size and c < size:
        answer+=size * size * 2 #1, 2사분면만큼 pass
        r-=size

    # 좌표가 4사분면에 속할 때
    else:
        answer+=size * size * 3 #1, 2, 3사분면만큼 pass
        r-=size
        c-=size
    

print(answer)


