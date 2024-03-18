from collections import deque

a, target = map(int, input().split())

q = deque()
# q에 현재위치, cnt를 넣는다.
q.append((a,1))
while q:
    location, cnt = q.popleft()
    # 목표값 보다 크면 통과
    if location > target:
        continue
    # 목표값과 같아지면 출력 후 종료
    if location == target:
        print(cnt)
        break
    
    # 1. 곱하기(2)
    q.append((location * 2, cnt + 1))

    # 2. 1 붙이기 
    q.append((int(str(location) + "1") , cnt + 1))

else:
    print(-1)




    
