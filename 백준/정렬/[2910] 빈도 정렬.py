import sys
input = sys.stdin.readline


N, C = map(int, input().split())
list_n = list(map(int, input().split()))
# 순서 인덱스
# dict_idx = {val:idx for idx, val in enumerate(list_n) if val not in }
# dict
dict_n = {}
for i in list_n:
    # 풀이 참고 부분
    if i not in dict_n:  
        dict_n[i] =0
    dict_n[i] += 1
    # num = list_n.count(i)
    # dict_n[i] = num
print(dict_n)
# 횟수 정렬 -> 순서 정렬
dict_n = sorted(dict_n.items(), key=lambda x:x[1], reverse=True)

for a, b in dict_n:
    # b = 횟수
    for j in range(b):
        print(str(a), end=" ")
# print(dict_n)

