import sys
input = sys.stdin.readline
n = int(input())
high = []
stack = []
answer = 0
for _ in range(n):
    high.append(int(input()))

for i in high:
    # 1.stack이 있고 0번지보다 i값이 더 큰경우(짝이 되는 경우)
    while stack and stack[-1][0] < i:
        answer += stack.pop()[1]
    
    # 2. stack이 없다면 i를 넣는다. (현재 사람 추가)
    if len(stack) == 0:
        stack.append((i,1))
        continue
    
    # 3. 스택의 끝 값과 같은 경우
    if stack[-1][0] == i:
        cnt = stack.pop()[1]
        answer += cnt

        # 같은 키 보다 왼쪽이 있는 경우 top과 현재 사람이 볼 수 있기에 1추가.
        if stack:
            answer += 1
        # 현재 키인 사람, 같은 사람이 cnt 만큼 있기에 키 = h, 명수 = cnt += 1를 스택에 추가
        stack.append((i, cnt + 1))
    else:
        stack.append((i,1))
        answer += 1

print(answer)


        
        




