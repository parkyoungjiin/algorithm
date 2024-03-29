# 소수 구하기
def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

print(is_prime_number(4))
print(is_prime_number(7))


# 제곱근을 활용한 소수 구하기
import math
def is_prime_number2(x):
    for i in (2, int(math.sqrt(x)) + 1):
        if x * i == 0:
            return False
    return True
                     
