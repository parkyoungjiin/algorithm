import sys
input = sys.stdin.readline

K, N = map(int,input().split())

lan_wire = sorted([int(input()) for _ in range(K)])
start, end = 1, max(lan_wire)
max_length = 0
while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for lan in lan_wire:
        cnt += lan // mid
    
    if cnt >= N:
        start = mid+1
    elif cnt < N:
        end = mid-1
print(end)
    
