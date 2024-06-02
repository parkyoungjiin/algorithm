import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

answer = [0] * n
for i, val in enumerate(arr): # val= 자신보다 키 큰 사람 수
    count = 0 # 키 큰 사람 count
    for j, ans in enumerate(answer):
        if ans == 0 and count < val:
            count += 1

        # 아무도 안채워졌고, count == val이 같아지면 앞에 키 큰 사람을 다 넣은 것이기에 현재 학생 넣기
        elif ans == 0 and count == val:
            answer[j] = i+1
            break

print(answer)

