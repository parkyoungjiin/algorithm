
# 1. 이분탐색을 활용한 풀이 
import sys
input = sys.stdin.readline
#  N(1 ≤ N ≤ 500,000)
N = int(input())
card_list = sorted(list(map(int, input().split())))
#  M(1 ≤ M ≤ 500,000)
M = int(input())
check_list = list(map(int, input().split()))

def binary_search(check):
    start, end = 0, N-1 # index 감안해서 len-1
    while start <= end:
        mid = (start+end) // 2
        if card_list[mid] == check:
            return 1
        # 중간값 > 탐색값 -> 중간값을 end로 설정
        elif card_list[mid] > check:
            end = mid - 1
        # 중간값 < 탐색값 -> 중간값을 start로 설정한다.
        else:
            start = mid + 1
    return 0

for check in check_list:
    # 이진 탐색
    print(binary_search(check), end =' ')
    
    


# 2. 딕셔너리 사용한 코드
# import sys
# input = sys.stdin.readline
# #  N(1 ≤ N ≤ 500,000)
# N = int(input())
# card_list = list(map(int, input().split()))
# #  M(1 ≤ M ≤ 500,000)
# M = int(input())
# check_list = list(map(int, input().split()))
# dictionary = {n: 0 for n in card_list}
# for i in check_list:
#     if i in dictionary:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')

