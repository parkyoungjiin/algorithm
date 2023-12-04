import sys
input = sys.stdin.readline

N = int(input())
N_list = sorted(list(map(int,input().split())))
M = int(input())
M_list = list(map(int,input().split()))
# print(N_list)

# for m in M_list:
#     start, end = 0, len(N_list)-1
#     mid = (start+end) // 2
    
#     if N_list[mid] > m:
#         start = mid + 1
#     elif N_list[mid] < m:
#         end = mid -1
    



# 딕셔너리 사용하여 통과한 코드
# answer = {m:0 for m in M_list}
# for n in N_list:
#     if n in answer:
#         answer[n] += 1

# for m in M_list:
#     if answer.get(m) == 0:
#         print(0, end=' ')
#     else:
#         print(answer[m], end=' ')
