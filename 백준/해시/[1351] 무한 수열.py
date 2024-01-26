import sys
input = sys.stdin.readline

n, p, q = map(int,input().split())

dict ={}
dict[0] = 1

def solutionNumber(num):
    if num in dict:
        return dict[num]

    else:
        dict[num] = solutionNumber(num // p) + solutionNumber(num // q)
        return dict[num]



print(solutionNumber(n))
# DP를 사용했을 때 메모리 초과 발생
# answer = [0 for _ in range(n+1)]

# answer[0] = 1
# answer[1] = 2
# answer[2] = 3
# for i in range(3, n+1):
    
#     answer[i] = answer[i//p] + answer[i//q]

# print(answer[n])
