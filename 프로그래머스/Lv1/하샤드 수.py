def solution(x):
    # x % x의 자리수 합 == 0 일 경우 하샤드 수
    sum_x = 0
    
    for i in str(x):
        sum_x += int(i)
    if x % sum_x == 0:
        return True
    else:
        return False

solution(10)
solution(11)
solution(12)