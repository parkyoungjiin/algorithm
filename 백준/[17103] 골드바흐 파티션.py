import sys
input = sys.stdin.readline

t = int(input())

# 에라토스테네스의 체 구하기
prime_arr = [True for _ in range(1000001)]

for i in range(2, int(1000000 ** 0.5)):
    if prime_arr[i]:
        for j in range(i*2, 1000001, i): #i를 제외한 배수 False 처리(소수가 아닌 것을 처리)
            prime_arr[j] = False

for _ in range(t):
    num = int(input())
    count = 0
    for k in range(2, num//2+1):
        if prime_arr[k] and prime_arr[num-k]:
            count += 1
    print(count)
        
