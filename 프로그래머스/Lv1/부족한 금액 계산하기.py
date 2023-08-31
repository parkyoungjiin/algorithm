def solution(price, money, count):
    answer = 0
    for i in range(1, count+1):
        answer += i * price
    answer = answer - money
    # 부족할 때 양수
    if answer >= 0:
        return answer
    else:
        return 0
    


    

solution(3, 20, 4)
