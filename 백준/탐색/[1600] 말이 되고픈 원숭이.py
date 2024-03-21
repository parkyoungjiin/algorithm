import sys
input = sys.stdin.readline

k = int(input())
w, h = map(int, input().split())

d = [(-1,0), (1,0), (0,-1), (0,1)]
hd = [(-2,-1), (-1,-2), (-2,1), (1, -2), (1,2), (2,1), (-1,2), (2,-1)]

# def bfs():




maps = [list(map(int,input().split())) for _ in range(h)]
visited = [[[0] * (k + 1) for _ in range(w)] for _ in range(h)]

visited[0][0][0] = 1 
print(visited)

