import sys
from collections import deque
input = sys.stdin.readline

n, w, l = map(int, input().split())

truck = deque(list(map(int,input().split())))
bridge = dict()
answer = 0
progress = 1
while truck:
    answer += 1
    # 트럭이 다리 길이를 넘은 경우 bridge에서 제거.
    if len(bridge) != 0:
        for truck_num, sec in bridge.items():
            if sec > w:
                bridge.pop(truck_num)
                break
    
    if len(bridge) == 0 or sum(bridge) + truck[0] <= l:
        t = truck.popleft()
    # w += 1
    # 트럭을 다리에 추가
    if sum(bridge.keys()) + t <= l and len(bridge) <= w:
        bridge[t] = 1
        # 트럭 초 증가
        if len(bridge) != 0:
            for truck_num, sec in bridge.items():
                bridge[truck_num] = sec + 1
        continue

    # 트럭 초 증가
    if len(bridge) != 0:
        for truck_num, sec in bridge.items():
            bridge[truck_num] = sec + 1

    

print(answer)
    # w는 다리 길이로 1로 초기화
    # if progress == w:
    #     progress = 1