def solution(n):
    answer = ''
    while n > 0:
        print(n)
        n, re = divmod(n, 3)
        # 나머지를 증감을 바로 하면 뒤집어서 출력된다.
        answer += str(re)

    # 뒤집어진 3진법을 10진법으로 변환하여 리턴.    
    return int(answer, 3)


solution(45)