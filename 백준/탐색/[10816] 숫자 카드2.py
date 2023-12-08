import sys
input = sys.stdin.readline

N = int(input())
N_list = list(map(int,input().split()))
M = int(input())
M_list = list(map(int,input().split()))
# print(N_list)


# 딕셔너리 사용하여 통과한 코드 

answer = {m:0 for m in M_list} # {10:3 9:0 -5:0 2:1 3:2 4:0 5:0 -10:2}

for n in N_list:
    if n in answer: 
        answer[n] += 1 

for m in M_list:
    if answer.get(m) == 0:
        print(0, end=' ')
    else:
        print(answer[m], end=' ') 
