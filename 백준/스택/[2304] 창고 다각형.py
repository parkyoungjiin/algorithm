import sys
input = sys.stdin.readline
# 기둥
pill = [0 for i in range(1001)]

n = int(input())

max_height = 0
max_idx = 0

height = 0
area = 0
for _ in range(n):
    l, h = map(int, input().split())
    pill[l] = h
    # 최고 높이 기둥 최신화(높이, 인덱스 같이 저장)
    if max_height < h:
        max_idx = l
        max_height = h

# 왼쪽부터 최고기둥까지
for i in range(max_idx + 1):
    height = max(height, pill[i]) # 기둥높이가 큰 경우 갱신
    area += height

height = 0
# 오른쪽부터 최고기둥까지
for i in range(1000, max_idx, -1):
    height = max(height, pill[i])
    area += height

print(area)

    