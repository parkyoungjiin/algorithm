import sys
input = sys.stdin.readline


max_val = 123456 * 2
isPrime= [True for _ in range(max_val+1)] # 소수 = True

for i in range(2, int(max_val**0.5)+1):
    # 소수인 경우 소수
    if isPrime[i]:
        #소수의 배수를 False
        for j in range(i*i, max_val+1, i):
            isPrime[j] = False


while True:
    n = int(input())

    if n == 0:
        break

    else:
        cnt = 0
        for i in range(n+1, (n * 2)+1):
            if isPrime[i]:
                cnt += 1
            
        if n == 1:
            print(1)
        else:
            print(cnt)

