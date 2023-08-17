def solution(a, b, n):
    answer = 0
    empty_n = 0
    while n >= a:
        # 나머지 병이 존재하지 않을 때 
        if n % a == 0:
            # print('n:',n)
            n = n // a
            answer += n
        # 나머지 병이 존재할 때     
        else:
            # print('ns:',n)
            empty_n = n % a
            n = n // a
            answer += n
            n = n + empty_n

        
    return answer

solution(2,1,20)