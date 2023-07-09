# 1. N, M (행 ,열) 입력받기
N, M = map(int, input().split())

print(N, M)
# 2. 자연수 입력 받기

N_list = []
for i in range(N):
    N_list.append(list(map(int, input().split())))
result = []
for i in N_list:
    result.append(min(i))

result = max(result)

print(result)

