import sys
input = sys.stdin.readline
n = int(input())

n_list = sorted(list(map(int, input().split()))) # sorted 추가후 67퍼에서 틀림.
cnt = 0
# for i in n_list:
#     start, end = 0, len(n_list)-1
#     while start < end:
#         if n_list[start] + n_list[end] == i:
#             if n_list[start] == i:
#                 start += 1
#             elif n_list[end] == i:
#                 end -= 1
#             else:
#                 cnt += 1
#                 break
#             # if end != i:
#             #     cnt += 1
#             #     break
#             # elif end == i:
#             #     start += 1
#             #     break
#         elif n_list[start] + n_list[end] > i:
#             end -= 1
#         elif n_list[start] + n_list[end] < i:
#             start += 1
# print(cnt)

# 원소가 아닌, 인덱스로 접근해야 값이 같아도 수의 위치가 다른 것을 판별할 수 있다.
for i in range(n):
    goal = n_list[i]
    start = 0
    end = len(n_list)-1
    while start < end:
        if n_list[start] + n_list[end] == goal:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                cnt += 1
                break
        elif n_list[start] + n_list[end] > goal:
            end -= 1
        elif n_list[start] + n_list[end] < goal:
            start += 1

print(cnt)