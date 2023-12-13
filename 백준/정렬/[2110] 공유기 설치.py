import sys
input = sys.stdin.readline

N, C = map(int,input().split())
house = []
for _ in range(N):
    house.append(int(input()))
house = sorted(house)

# 최소거리, 최대거리
# max_length = max(house) - min(house) 
# min_length = house[house.index(min(house)) + 1] - min(house)
start, end = 1, house[N-1] - house[0]
result = 0
# mid 값

if C == 2:
    print(house[N-1] - house[0])
else:
    while start < end:
        mid = (start + end) // 2
        target = house[0]
        cnt = 1
        for i in range(N):
            # 설치가 되는 경우
            if house[i] - target >= mid:
                cnt += 1
                target = house[i]
        # 공유기 개수가 남는 경우
        if cnt >= C:
            start = mid + 1
            result = mid # why result = mid?
        # 공유기 개수가 많은 경우
        else:
            # end = mid -1
            end = mid
    print(result)
    



