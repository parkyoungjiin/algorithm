import sys
input = sys.stdin.readline

N = int(input())
solution = list(map(int,input().split()))

left, right = 0, len(solution)-1
sum_value = solution[left] + solution[right]
sol1, sol2 = solution[left], solution[right]

while left < right:
    temp = solution[left] + solution[right]
    
    # 절대값이 작을 수록 0에 가까워짐.
    if abs(sum_value) > abs(temp):
        sum_value = abs(temp)
        sol1, sol2 = solution[left], solution[right]
    # break를 걸지 않으면 시간초과가 발생했음.
    if temp == 0:
        break
    elif temp > 0:
        right -= 1
    elif temp < 0:
        left += 1
    
print(sol1, sol2)


"""
while left < right:
    temp = solution[left] + solution[right]

    if temp > 0:
        right -= 1
    elif temp < 0:
        left += 1
    
    if left != right:
        if abs(sum_value) > abs(solution[left] + solution[right]):
            sol1, sol2 = solution[left], solution[right]
print(sol1, sol2)
"""



