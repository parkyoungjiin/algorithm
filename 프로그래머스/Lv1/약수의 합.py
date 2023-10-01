def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i==0:
            #약수일 경우 합하기
            answer+=i
    return answer