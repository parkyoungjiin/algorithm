"""
정수 N이 입력되면 00시 00분 00초 ~ N시 59분 59초까지의 
모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성
"""

# print(i for i in 33 in '3')
test_num = 33
print('3' in str(test_num))

N = int(input("정수를 입력하시오"))
# 03시, 13시에는 모든 초, 분에서 cnt가 올라가야 함.
minutes = 60
second = 60
cnt = 0
for n in range(0, N+1):
    for i in range(minutes):
        for j in range(second):
            if '3' in str(n) or '3' in str(i) or '3' in str(j):
                cnt += 1
print(cnt)