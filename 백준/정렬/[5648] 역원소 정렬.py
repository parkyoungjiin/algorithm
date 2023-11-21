import sys
# read는 Ctrl + D까지 입력받음.
# readline은 한 줄을 읽음.
input = sys.stdin.read
# readline -> 

# *S -> *을 붙여 변수 선언 시 정해지지 않은 개수의 입력값을 넣는다.
li, *S = input().split()
print(li, S)
for i in range(len(S)):
    S[i] = S[i][::-1]
    print(S[i])

# 0제거 + 오름차순 정렬을 위해 int로 변환

S = [int(i) for i in S]
S.sort()
for i in S:
    print(i)



