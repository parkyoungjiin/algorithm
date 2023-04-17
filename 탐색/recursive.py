def recursive_function(i):
	if i == 100:
		return
	print(i, '번째 재귀함수에서', i + 1, '번째 재귀함수를 호출합니다.')
	recursive_function(i+1)
	print(i, '번째 재귀함수를 종료합니다.')

recursive_function(1)


# 팩토리얼 코드 구현 
# 1. 반복적으로 구현(반복문)
def factorial_iterative(n):
    result = 1
    for i in range(n + 1):
        result *= i
    return result

# 2. 재귀적으로 구현(재귀)
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1) # n = 5 -> 5 * 4! 이기에 재귀로 코드 구현.



# 최대공약수 계산
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
        