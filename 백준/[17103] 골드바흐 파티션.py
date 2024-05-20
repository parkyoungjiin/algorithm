import sys
input = sys.stdin.readline


check = [0] * 1000001
# 소수 = 1
check[0] = 1
check[1] = 1


prime = []
count = 0
for i in range(2, 1000001):
    if check[i] == 0:
        prime.append(i)
        for j in range(2*i, 1000001, i):
            check[j] = 1

tc = int(input())

for t in range(tc):
    n = int(input())
    for i in prime:
        if i >= n:
            break

        if not check[n-1] and i <= n-i:
            count += 1
    

