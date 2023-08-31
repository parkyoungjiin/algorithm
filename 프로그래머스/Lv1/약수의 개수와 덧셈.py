def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        div_cnt = 0
        for j in range(1, i+1):
            # 약수일 경우 div_cnt에 약수 개수를 증가
            if i % j == 0:
                div_cnt +=1
            # print(div_cnt)
        # 약수가 짝수일 때, 홀수 일 때 처리
        if div_cnt % 2 == 0:
            answer += i
        else:
            answer -= i
        
    return answer


solution(13, 17)


