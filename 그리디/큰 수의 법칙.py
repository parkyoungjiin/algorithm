# 다양한 수로 이뤄진 배열이 있을 때, 주어진 수들을 M번 더하여 가장 큰수로 만드는 법칙.
# 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과해서 더해질 수 없다.
# 예를들어, k가 3일 때 5 5 5 5는 안되며 5 5 5 3 5 5 5는 가능하다.

# N = 배열 크기
# M = 더해지는 횟수
# K = 최대 반복횟수

N, M, K = map(int,input("띄어쓰기로 구분하여 숫자를 입력하시오 :").split())
# 배열의 크기 N 만큼 입력받기
data = list(map(int,input().split()))

data.sort()
# 제일 큰 값, 그 다음으로 큰 값 저장하기
first_value = data[-1]
second_value = data[-2]
result = 0

while True:
    for i in range(K):
        if M == 0:
            break
        result += first_value
        M -= 1
    if M == 0:
        break
    result += second_value # 두 번째로 큰 수를 한 번 더하기
    M -= 1
print(result)
