N,K = map(int,input().split())
print('N값:',N,'k값 :',K)
cnt = 0

# N이 1이되면 반복문 종료
while True:
    # 나눠 떨어지는 지 확인
    
    if N == 1:
        break
    elif N % K == 0:
        # 나머지가 0인경우 나눈다. + 횟수 증가
        N = N // K
        cnt += 1
    # 나눠 떨어지지 않을 경우
    else:
        N -= 1
        cnt += 1
    
print(cnt, N)



    
