import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

move = [[[0,0] for _ in range(m)] for _ in range(n)]
print(move)
