import sys
input = sys.stdin.readline

N = int(input())

solution = list(map(int,input().split()))

start, end = 0, N-1
sol_sum = solution[start] + solution[end]
while start < end:
    temp_sum = solution[start] + solution[end]
    if abs(sol_sum) > abs(temp_sum):
        sol_sum = temp_sum
    
    # temp_sum = 0

    if temp_sum > 0:
        end -= 1
    else:
        start += 1
    

print(sol_sum)