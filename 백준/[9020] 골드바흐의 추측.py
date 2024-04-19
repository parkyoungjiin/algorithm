import sys
input = sys.stdin.readline

max_val = 10000

prime = [True] * (max_val+1)

prime[0], prime[1] = False, False
# 에라토스테네스의 체 코드 (외우기)
for i in range(2, int(max_val**0.5)+1):
    if prime[i]:
        for j in range(i*i, max_val+1, i):
            prime[j] = False


tc = int(input())

for t in range(tc):
    prime_list = []

    n = int(input())

    diff = 10000
    answer = [0, 0]

    for i in range(2, n+1):
        if prime[i]:
            temp = n-i
            if prime[temp] and diff > abs(i-temp):
                diff=abs(i-temp)
                answer[0], answer[1] = i, temp
    
    answer.sort()
    print(*answer)


        
        

    


