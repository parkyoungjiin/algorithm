def solution(number, limit, power):
    answer = 0
    divisor_cnt = 0
    for i in range(1, number+1): # 횟수
        if i == 1:
            divisor_cnt += 1
            answer += 1
            divisor_cnt = 0
        else:
            for div_i in range(1, i+1): # 
                if i % div_i  == 0:
                    divisor_cnt += 1

                # print(divisor_cnt)
                
            if divisor_cnt > limit:
                answer += power
                divisor_cnt = 0
            else:
                answer += divisor_cnt
                divisor_cnt = 0 
    return print(answer)

solution(5, 3, 2) # result = 10
solution(10, 3, 2) # result = 21


#  if divisor_cnt > limit:
#                 # 제한수치 초과 시 공격력 power
#                 answer += power
#                 divisor_cnt = 0
#             else:
#                 answer += divisor_cnt
#                 divisor_cnt = 0