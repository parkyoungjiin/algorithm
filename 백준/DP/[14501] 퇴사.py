import sys

input = sys.stdin.readline

n = int(input())

schdule = [list(map(int, input().split())) for _ in range(n)]
print(schdule)

for i in range(n):
    for j in range(i+schdule[i][0], n+1):
        
               

# answer = [0] * n

# for _ in range(n):
#     t, p = map(int, input().split())

#     t_lst.append(t)
#     p_lst.append(p)

# for i in range(n):
#     idx = i
#     max_benefit = p_lst[idx]
#     while True:
#         idx += t_lst[idx]
#         if idx > n:
#             break
        
#         max_benefit += p_lst[idx]

#     answer[i] = max_benefit

# print(answer)
