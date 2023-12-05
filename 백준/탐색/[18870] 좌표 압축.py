import sys
input = sys.stdin.readline
N = int(input())
N_list = list(map(int,input().split()))
# 중복 제거 + 오름차순 정렬
N_list2 = sorted(list(set(N_list)))
# 인덱스를 사용하기 위해 dict 제작
N_dict ={N_list2[i] : i for i in range(len(N_list2))}
for n in N_list:
    print(N_dict[n], end = ' ')


