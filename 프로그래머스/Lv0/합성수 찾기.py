"""
약수의 개수가 세 개 이상인 수를 합성수라고 합니다. 
자연수 n이 매개변수로 주어질 때 n이하의 합성수의 개수를 return하도록 solution 함수를 완성해주세요.

1~n까지 각각 나눴을 떄 2번 이상 나눠진 경우 count + 1 하기
약수 구하는 공식이 뭐지
약수 -> n을 나누었을 때 나머지가 0인 것

"""
def solution(n):
    answer = 0
    # 약수 개수 변수
    # 1~n 값에 대해 약수 계산한 후 약수가 3개 이상인 경우 answer을 1 증가하기.
    for i in range(1,n+1):
        cnt = 0
        for j in range(1,i+1):
            # 약수 계산 (나머지가 0인 경우)
            if i % j == 0:
                cnt += 1
        if cnt >= 3:
            answer += 1
    


    return answer

solution(10)