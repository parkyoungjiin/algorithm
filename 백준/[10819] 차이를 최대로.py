import sys
from itertools import permutations

n = int(input())

arr = list(map(int, input().split()))
# 순열
t = list(permutations(arr, n))

answer = 0
for i in t:
    temp = 0
    for j in range(n-1): # [n-2] - [n-1] 공식이 있기에, n-1로 설정.
        temp += abs(i[j]-i[j+1])
    
    answer = max(answer, temp)

print(answer)
