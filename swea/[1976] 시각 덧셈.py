T = int(input())
for test_case in range(1, T + 1):
    
    time_list = list(map(int, input().split()))
    hour, minutes = time_list[0] + time_list[2], time_list[1] + time_list[3]
    # 반례 : 12 12 11 50
    # 처음에 시간을 더했을 때 12시간을 초과한 경우 12로 나머지연산을 진행해야 함.
    if hour > 12:
        hour %= 12
    
    if minutes >= 60:
        hour += minutes // 60
        minutes %= 60

    if hour > 12:
        hour %= 12
    print("#{}".format(test_case),hour, minutes)

    
    
