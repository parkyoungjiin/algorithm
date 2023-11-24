import sys
input = sys.stdin.readline
# 파리 개수
N, M = map(int, input().split())

# 파리채 크기 = M * M
# 최대한 많은 파리를 죽이려 한다.

# 파리 개수 행렬
area = [list(map(int,input().split())) for _ in range(N)]



