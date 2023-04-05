# 4-2
"""
1. 정수 N 입력받기
2. 00시 00분 00초부터 N시 59분 59초까지 모든 시각 중 3이 하나라도 포함되는 모든 경우의 수를 구하라

minutes, seconds는 반복이기에 N을 곱해주면 될듯함 !

"""

n = int(input())
# 이중 반복문을 통해 분, 초에 3이 하나라도 들어가는 경우의 수 계산
count = 0
for i in range(0,n+1,1):
    for j in range(0,60,1):
        for n in range(0,60,1):
                # 문자열을 연결해서 032035로 된 값에서 in 연산자로 해결!
                if '3' in str(i) + str(j) + str(n):
                    print(i, ': i 값', j, 'j값', n, 'n값')
                    count += 1


print(count)




