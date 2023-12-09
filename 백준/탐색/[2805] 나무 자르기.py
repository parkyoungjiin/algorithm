import sys
input = sys.stdin.readline
N, M = map(int,input().split())
high = sorted(list(map(int,input().split())))
start, end = 1, max(high)

while start <= end:
    sum_high = 0
    mid = (start + end) // 2
    for h in high:
        if h > mid:
            sum_high += h-mid
    # if sum_high == M:
    #     print(mid)
    #     break
    if sum_high >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)


        
   
            

