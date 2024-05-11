import sys
from collections import deque

input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    q = deque()
    n, m = map(int, input().split())
    # 중요도 입력
    temp = list(map(int,input().split()))
    for i in temp:
        q.append(i)

    # 값 저장
    count = 0

    while q:
        #최대값 
        best = max(q)
        # 뽑은 값
        temp = q.popleft()
        # 위치 조정 (m을 인덱스로 사용하여 앞의 자리를 뺼 때 마다 감소.)
        m -= 1

        # 뽑은 숫자가 가장 큰 경우 
        if temp == best:
            count += 1
            # m < 0인 경우 맨 앞이라는 뜻.
            if m < 0:
                print(count)
                break
            
        # 뽑은 숫자가 큰 경우 X
        else:
            q.append(temp)
            # 맨 앞에서 뽑히면 제일 뒤로.
            if m < 0:
                m = len(q) - 1 
            
            
            


    
    
