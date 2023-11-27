# A는 자기보다 작은 수만 먹는다.
# (1 ≤ N, M ≤ 20,000)
# 시간 제한 1초
# 이분탐색 문제!
import sys
input = sys.stdin.readline

def binarySearch(a):
    start, end = 0, M-1
    res = 0

    while start <= end:
        mid = (start+end) //2
        # 중앙값이 더 큰 경우
        # 포인터 조정
        if b_list[mid] > a:
            end = mid -1
        # 중앙값이 더 작은 경우
        else:
            start = mid +1 # why +1인지? -> mid보다 큰 번지부터 탐색해야 하기 때문.
            # mid 값을 res에 넣는다.
            res = mid  
    return res + 1

#테케
TC = int(input())

for i in range(TC):
    cnt = 0
    N, M = map(int,input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    for i in a_list:
        if i > b_list[0]:
            t = binarySearch(i)
            





    # 20,000까지이기에 여기서 20,000 * 20,000 반복을 하기에 시간 초과가 발생한 것으로 보인다.

    # for ac in a_list:
    #     for bc in b_list:
    #         # a의 요소와 b요소를 비교.
    #         if ac > bc:
    #             cnt += 1
    # print(cnt)        

