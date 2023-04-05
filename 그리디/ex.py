n, k = map(int,input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    # 몫 * k를 했을 때 k로 나눠 떨어지는 가장 가까운 수를 발견함.
    target =  (n // k) * k

    # result 는 총 연산 횟수를 저장하는 변수로
    # n-target을 통해 몇 번을 수행할 지를 계산하여 저장해줌. (ex. n(17)이 k(4)로 나눠 떨어지는 수가 될 때까지 빼주는 연산을 1번만 하면 되기에 1로 저장된다.)
    result += (n-target)

    # target을 n에 저장(-1를 수행한 이후 k로 나눠떨어지는 가장 가까운 수인 n이기 때문에 저장함.)
    n = target

    # N이 K 보다 작을 때 (더 이상 나눌 수 없을 때 ) 반복문 탈출
    if n<k :
        break
    result += 1 # k를 나누는 연산을 수행하므로 수행횟수 1번 추가
    n //= k  

# 마지막 남은 수에 대해 1씩 빼기
result += (n-1)
print(result)
