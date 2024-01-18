import sys
input = sys.stdin.readline

n = int(input())
high = list(map(int,input().split()))

# 최대값을 저장할 리스트(스택)
stack = []

# 수신 인덱스 저장 리스트
answer = []

for i in range(n):
    index, h = i, high[i]
    if len(stack) == 0:
        stack.append([index, h])
        answer.append(0)
    else:
        if stack[-1][1] < h:
            stack.pop()
            answer.append(stack[-1][0] + 1)
        else:
            answer.append(stack[-1][0] + 1)
            stack.append([index, h])
print(answer)



