# 1. N, K 입력 받기
N, K = map(int, input().split())

cnt = 0
# 2. 나눠지는 지 확인
while N != 1:
    if N % K == 0:
        N = N // K  
        cnt += 1
    else:
        N = N - 1
        cnt += 1

print(cnt)

# 1. 입력 받기
N, K = map(int, input().split())
# 2. target 변수를 활용하여 -1 작업을 계속 반복하지 않음.
target = 0
cnt = 0

target = (N // K) * K # K로 나눠지는 값을 찾아서 가장 가까운 수를 target 변수에 저장함.

cnt += (N-target)



    

