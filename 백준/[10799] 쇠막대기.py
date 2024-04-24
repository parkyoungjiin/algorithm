import sys
input = sys.stdin.readline

pipe = list(input().rstrip())
temp = []
answer = 0
for i in range(len(pipe)):
    if pipe[i] == '(':
        temp.append('(')
    else:
        # 레이저
        if pipe[i-1] == '(':
            temp.pop()
            answer += len(temp)
        else:
            temp.pop()
            answer += 1
print(answer)


