# 왼 -> 오 하나씩 모든 숫자(0~9)를 확인하며 숫자 사이에 곱하기 혹은 더하기를 하여 가장 큰 수를 구하는 프로그램을 작성하라

# 0 혹은 1의 경우는 곱하기 보다는 더하기가 효율적임. 
# -> 그렇기에 연산을 수행할 때 2개의 수 중에서 하나라도 1이하인 경우에는 더하고 두 수가 모두 2 이상인 경우 곱하면 된다.


# 1. s변수에 문자열 입력받기
data = input()
# 2. 첫 번째에 위치한 문자를 정수형으로 변환하여 대입
result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <=1 or result <=1:
        result += num
    else:
        result *= num
print(result)








