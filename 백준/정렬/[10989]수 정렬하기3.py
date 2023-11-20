import sys
input = sys.stdin.readline()
N = int(input)
array_n = [0] * 10001


for _ in range(N):
    array_n[int(sys.stdin.readline())] += 1 # arr[5] += 1 0 -> 1
for a in range(10001):
    if array_n[a] != 0:
        for _ in range(array_n[a]):
            print(a)



# ------ 메모리 초과 코드 -----------
# input = sys.stdin.readline().strip()
# N = int(input)
# array_n = [0] * (N+1)

# for index in range(N):
#     i = int(sys.stdin.readline())
#     array_n[index] = i
# # print(array_n)
# array_n = sorted(array_n)
# print(array_n)
# for a in array_n:
#     if a != 0:
#         print(a)

